from enum import Enum


class FatType(str, Enum):
    FAT12 = "FAT12"
    FAT16 = "FAT16"
    FAT32 = "FAT32"
