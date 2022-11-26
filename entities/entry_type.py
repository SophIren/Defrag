from enum import Enum


class EntryType(str, Enum):
    USED = "USED"
    EMPTY = "EMPTY"
    EMPTY_ENDING = "EMPTY_ENDING"
