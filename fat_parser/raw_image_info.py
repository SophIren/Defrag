from boot_sector import BSParams
from io_manager import IOManager


class RawImageInfo:
    def __init__(self, io_manager: IOManager):
        self.io_manager = io_manager
        self.bs_params = BSParams()
