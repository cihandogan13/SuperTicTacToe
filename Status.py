from enum import Enum

class Status(Enum):
    NOT_RESOLVED = 1
    ILLEGAL_MOVE = 2
    RESOLVED = 3
    FINISHED = 4
    FIRST_MOVE = 5
    TIE = 6