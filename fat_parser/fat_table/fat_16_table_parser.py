from fat_parser.fat_table.fat_table_parser import FatTableParser
from fat_parser.io_manager import IOManager
from fat_parser.raw import ImageInfo


class Fat16TableParser(FatTableParser):
    ENDING_FAT_ENTRY_NUM = 0xFFF8
    ENTRY_LENGTH: int = 2

    def __init__(self, io_manager: IOManager, image_info: ImageInfo):
        super(Fat16TableParser, self).__init__(io_manager, image_info)
