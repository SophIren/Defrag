class FatTableParams:
    ENDING_FAT_ENTRY_NUM = None
    ENTRY_LENGTH = None


class Fat16TableParams(FatTableParams):
    ENDING_FAT_ENTRY_NUM = 0xFFF8
    ENTRY_LENGTH: int = 2


class Fat32TableParams(FatTableParams):
    ENDING_FAT_ENTRY_NUM = 0x0FFFFFF8
    ENTRY_LENGTH: int = 4
