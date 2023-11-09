from common import Coordinates, Location, LocationType, Trip
from typing import List

trips: List[List[Trip]] = [
    [
        Trip(
            "trip_1",
            Location(LocationType.PICK, Coordinates(0,0)),
            Location(LocationType.DROP, Coordinates(1,0))
        ),
        Trip(
            "trip_2",
            Location(LocationType.PICK, Coordinates(0,1)),
            Location(LocationType.DROP, Coordinates(1,1))
        )
    ],
    [
        Trip(
            "trip_3",
            Location(LocationType.PICK, Coordinates(0,0)),
            Location(LocationType.DROP, Coordinates(10,10))
        ),
        Trip(
            "trip_4",
            Location(LocationType.PICK, Coordinates(0, 0)),
            Location(LocationType.DROP, Coordinates(10, 10))
        ),
        Trip(
            "trip_5",
            Location(LocationType.PICK, Coordinates(0,0)),
            Location(LocationType.DROP, Coordinates(10,10))
        )
    ]
]