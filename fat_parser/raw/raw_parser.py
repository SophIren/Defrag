from fat_parser.boot_sector import BSParser, BSInfo
from fat_parser.io_manager import IOManager
from fat_parser.raw import RawImageInfo

from entities import FatType


class RawFatParser:
    def __init__(self, io_manager: IOManager):
        self.io_manager = io_manager

        bs_info = BSInfo()
        self.raw_info = RawImageInfo(bs_info)
        self.bs_parser = BSParser(io_manager, bs_info)

    def parse(self):
        self.bs_parser.parse_common_fields()
        if self.raw_info.fat_type == FatType.FAT32:
            self.bs_parser.parse_fat32_fields()
        else:
            self.bs_parser.parse_fat16_fields()
