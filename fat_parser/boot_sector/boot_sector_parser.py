from boot_sector_params import BSParams
from fat_parser.io_manager import IOManager


class BootSectorParser:
    def __init__(self, io_manager: IOManager, bs_params: BSParams):
        self.io_manager = io_manager
        self.bs_params = bs_params

    def parse_common_fields(self):
        self.bs_params.jump_boot = self.io_manager.read_int(8)
        self.bs_params.oem_name = self.io_manager.read_int(2)
        self.bs_params.bytes_per_sector = self.io_manager.read_int(1)
        self.bs_params.reserved_sectors_count = self.io_manager.read_int(2)
        self.bs_params.num_of_fats = self.io_manager.read_int(1)
        self.bs_params.root_entries_count = self.io_manager.read_int(2)
        self.bs_params.total_sectors_16 = self.io_manager.read_int(2)
        self.bs_params.media = self.io_manager.read_int(1)
        self.bs_params.fat_size_16 = self.io_manager.read_int(2)
        self.bs_params.sectors_per_track = self.io_manager.read_int(2)
        self.bs_params.num_of_heads = self.io_manager.read_int(2)
        self.bs_params.hidden_sectors_count = self.io_manager.read_int(4)
        self.bs_params.total_sectors_32 = self.io_manager.read_int(4)
    
    def parse_fat16_fields(self):
        self.bs_params.drive_number = self.io_manager.read_int(1)

        self._parse_fat_fields()
    
    def parse_fat32_fields(self):
        self.bs_params.fat_size_32 = self.io_manager.read_int(4)
        self.bs_params.ext_flags = self.io_manager.read_int(2)
        self.bs_params.version = self.io_manager.read_int(2)
        self.bs_params.root_cluster = self.io_manager.read_int(4)
        self.bs_params.fs_info = self.io_manager.read_int(2)
        self.bs_params.backup_bs_sector = self.io_manager.read_int(2)
        self.io_manager.read_int(12)
        self.bs_params.drive_number = self.io_manager.read_int(1)

        self._parse_fat_fields()

    def _parse_fat_fields(self):
        self.io_manager.read_int(1)
        self.bs_params.boot_sig = self.io_manager.read_int(1)
        self.bs_params.volume_id = self.io_manager.read_int(4)
        self.bs_params.volume_label = self.io_manager.read_int(11)
        self.bs_params.sys_type = self.io_manager.read_int(8)
