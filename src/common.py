from enum import Enum
from typing import NamedTuple

class LocationType(Enum):
    DROP = 0
    PICK = 1

class Coordinate(NamedTuple):
    x: float
    y: float

    def get_euclidean_dist(self, coord: 'Coordinate'):
        dist = ((self.x - coord.x) ** 2 + (self.y - coord.y) ** 2) ** 0.5
        return dist

class Location(NamedTuple):
    type: LocationType
    coord: Coordinate

class Trip(NamedTuple):
    id: str
    pick_location: Location
    drop_location: Location

