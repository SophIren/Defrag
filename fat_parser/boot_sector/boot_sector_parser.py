from fat_parser.boot_sector import BSInfo
from fat_parser.io_manager import IOManager


class BSParser:
    def __init__(self, io_manager: IOManager, bs_info: BSInfo):
        self.io_manager = io_manager
        self.bs_info = bs_info

    def parse_common_fields(self):
        self.bs_info.jump_boot = self.io_manager.read_int(3)
        self.bs_info.oem_name = self.io_manager.read_int(8)
        self.bs_info.bytes_per_sector = self.io_manager.read_int(2)
        self.bs_info.sectors_per_cluster = self.io_manager.read_int(1)
        self.bs_info.reserved_sectors_count = self.io_manager.read_int(2)
        self.bs_info.num_of_fats = self.io_manager.read_int(1)
        self.bs_info.root_entries_count = self.io_manager.read_int(2)
        self.bs_info.total_sectors_16 = self.io_manager.read_int(2)
        self.bs_info.media = self.io_manager.read_int(1)
        self.bs_info.fat_size_16 = self.io_manager.read_int(2)
        self.bs_info.sectors_per_track = self.io_manager.read_int(2)
        self.bs_info.num_of_heads = self.io_manager.read_int(2)
        self.bs_info.hidden_sectors_count = self.io_manager.read_int(4)
        self.bs_info.total_sectors_32 = self.io_manager.read_int(4)

        self.bs_info.unchecked_fat_size_32 = self.io_manager.read_int(4)
        self.io_manager.rollback(4)
    
    def parse_fat16_fields(self):
        self.bs_info.drive_number = self.io_manager.read_int(1)

        self._parse_fat_fields()
    
    def parse_fat32_fields(self):
        self.bs_info.fat_size_32 = self.io_manager.read_int(4)
        self.bs_info.ext_flags = self.io_manager.read_int(2)
        self.bs_info.version = self.io_manager.read_int(2)
        self.bs_info.root_cluster = self.io_manager.read_int(4)
        self.bs_info.fs_info = self.io_manager.read_int(2)
        self.bs_info.backup_bs_sector = self.io_manager.read_int(2)
        self.io_manager.read_int(12)
        self.bs_info.drive_number = self.io_manager.read_int(1)

        self._parse_fat_fields()

    def _parse_fat_fields(self):
        self.io_manager.read_int(1)
        self.bs_info.boot_sig = self.io_manager.read_int(1)
        self.bs_info.volume_id = self.io_manager.read_int(4)
        self.bs_info.volume_label = self.io_manager.read_int(11)
        self.bs_info.sys_type = self.io_manager.read_int(8)
