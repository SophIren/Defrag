from enum import Enum


class EntryType(int, Enum):
    USED = "USED"
    EMPTY = "EMPTY"
    EMPTY_ENDING = "EMPTY_ENDING"
