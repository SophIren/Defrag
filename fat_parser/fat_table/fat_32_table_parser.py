from fat_parser.fat_table.fat_table_parser import FatTableParser
from fat_parser.io_manager import IOManager
from fat_parser.raw import ImageInfo


class Fat32TableParser(FatTableParser):
    ENDING_FAT_ENTRY_NUM = 0x0FFFFFF8
    ENTRY_LENGTH: int = 4

    def __init__(self, io_manager: IOManager, image_info: ImageInfo):
        super(Fat32TableParser, self).__init__(io_manager, image_info)
