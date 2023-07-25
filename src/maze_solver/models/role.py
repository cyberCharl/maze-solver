from enum import IntEnum, auto

# Role extends the IntEnum class from std library
# Only 1 of the following can be selected at once


class Role(IntEnum):

    ONE = 0
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()
