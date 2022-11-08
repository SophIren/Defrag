from fat_parser import BootSectorParser
from fat_parser import IOManager
from raw_image_info import RawImageInfo

from entities import FatType


class RawFatParser:
    def __init__(self, io_manager: IOManager):
        self.io_manager = io_manager
        self.raw_info = RawImageInfo(io_manager)
        self.bs_parser = BootSectorParser(io_manager, self.raw_info.bs_params)

    def parse(self):
        self.bs_parser.parse_common_fields()
        if self.raw_info.fat_type == FatType.FAT32:
            self.bs_parser.parse_fat32_fields()
        else:
            self.bs_parser.parse_fat16_fields()
