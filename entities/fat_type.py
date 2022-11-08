import enum


class FatType(str, enum):
    FAT12 = "FAT12"
    FAT16 = "FAT16"
    FAT32 = "FAT32"
