from enum import Enum
from typing import NamedTuple, List


class LocationType(Enum):
    """
    Enum for location type
    """
    DROP = 0  # Drop off location
    PICK = 1  # Pick up location
    OPEN = 2  # Other travel node or location


class Coordinates(NamedTuple):
    """
    Tuple for location coordinates
    """
    x: float    # x coordinate
    y: float    # y coordinate

    def get_euclidean_dist(self, coord: 'Coordinates') -> float:
        """
        Calculate euclidean distance between self and given coord.
        :param coord: Coordinate
        :return dist: float
        """
        dist = ((self.x - coord.x) ** 2 + (self.y - coord.y) ** 2) ** 0.5
        return dist


class Location(NamedTuple):
    """
    Tuple for location to be visited
    """
    type: LocationType
    coord: Coordinates


class Trip(NamedTuple):
    """
    Tuple for a trip
    """
    id: str
    # curr_location: Location
    pick_location: Location
    drop_location: Location


class LocationOutput(NamedTuple):
    """

    """
    trip_id: str
    type: LocationType


def trips_to_coordinates(trips: List[Trip]) -> List[Coordinates]:
    """
    List of trips to list of coordinates
    :param trips:
    :return:
    """
    return [
        coordinate
        for coordinates in [
            [trip.pick_location.coord, trip.drop_location.coord]
            for trip in trips
        ]
        for coordinate in coordinates
    ]