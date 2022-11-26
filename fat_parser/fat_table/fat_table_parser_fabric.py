from entities import FatType
from fat_parser.fat_table.fat_table_parser import FatTableParser
from fat_parser.fat_table.fat_16_table_parser import Fat16TableParser
from fat_parser.fat_table.fat_32_table_parser import Fat32TableParser
from fat_parser.io_manager import IOManager
from fat_parser.raw import ImageInfo


class FatTableFabric:
    @staticmethod
    def create(fat_type: FatType, io_manager: IOManager, image_info: ImageInfo) -> FatTableParser:
        if fat_type == FatType.FAT32:
            return Fat32TableParser(io_manager, image_info)
        if fat_type == FatType.FAT16 or fat_type == FatType.FAT12:
            return Fat16TableParser(io_manager, image_info)
