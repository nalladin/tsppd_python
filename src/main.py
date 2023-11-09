from pprint import pprint
from typing import List
import numpy as np
import pulp

from common import Trip, LocationType, LocationOutput, trips_to_coordinates
import trials


def find_path(trips: List[Trip]) -> List[LocationOutput]:

    coordinates = trips_to_coordinates(trips)
    num_coord = len(coordinates)

    problem = pulp.LpProblem("TSPPD")

    xss = [
        [pulp.LpVariable(f"x({i},{j})", cat="Binary") if i != j else None
         for j in range(num_coord)]
        for i in range(num_coord)
    ]   # Binary decision variable for travel from coordinates i to coordinates j

    ts = [
        pulp.LpVariable(f"t({i})", cat="Integer", lowBound=1, upBound=num_coord)
        for i in range(num_coord)
    ]   # Integer variable

    objective = pulp.lpSum(
        coordinates[i].get_euclidean_dist(coordinates[j]) * xss[i][j]
        for i in range(num_coord)
        for j in range(num_coord)
        if i != j
    )

    problem += objective

    for i in range(num_coord):
        problem += pulp.lpSum(xss[i][j] for j in range(num_coord) if i != j) == 1
        problem += pulp.lpSum(xss[j][i] for j in range(num_coord) if i != j) == 1

        # A weak constraint to remove partial circuits
        for j in range(num_coord):
            if j not in (0,i):
                problem += ts[i] - ts[j] + (num_coord - 1) * xss[i][j] <= num_coord - 2

    # Time constraints for pickups and dropoffs to ensure pick before drop
    for i in range(0, num_coord, 2):
        problem += ts[i] + 1 <= ts[i+1]

    status = pulp.LpStatus[problem.solve()]

    print(f'Status: {status}')
    print('Objective: {}'.format(objective.value()))

    if status != "Optimal":
        raise RuntimeError("No solution found!")

    ways = (np.array([[x.value() if x is not None else 0 for x in xs] for xs in xss]) > 0.5)

    indices = [0]

    while True:
        index = np.argwhere(ways[indices[-1], :])[0][0]

        if index == 0:
            break

        indices.append(index)

    return [
        LocationOutput(trips[index // 2].id, LocationType.PICK)
        if index % 2 == 0
        else LocationOutput(trips[index // 2].id, LocationType.DROP)
        for index in indices
    ]

def main():
    for trips in trials.trips:
        pprint(find_path(trips))


if __name__ == "__main__":
    main()