from boot_sector import BootSectorParser
from io_manager import IOManager
from raw_image_info import RawImageInfo


class RawFatParser:
    def __init__(self, io_manager: IOManager):
        self.io_manager = io_manager
        self.raw_info = RawImageInfo(io_manager)
        self.bs_parser = BootSectorParser(io_manager, self.raw_info.bs_params)
