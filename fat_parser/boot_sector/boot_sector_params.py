from typing import Optional


class BSParamsCommon:
    def __init__(self):
        self.jump_boot: Optional[int] = None
        self.oem_name: Optional[int] = None
        self.bytes_per_sector: Optional[int] = None
        self.sectors_per_cluster: Optional[int] = None
        self.reserved_sectors_count: Optional[int] = None
        self.num_of_fats: Optional[int] = None
        self.root_entries_count: Optional[int] = None
        self.total_sectors_16: Optional[int] = None
        self.media: Optional[int] = None
        self.fat_size_16: Optional[int] = None
        self.sectors_per_track: Optional[int] = None
        self.num_of_heads: Optional[int] = None
        self.hidden_sectors_count: Optional[int] = None
        self.total_sectors_32: Optional[int] = None


class BSParamsFat32:
    def __init__(self):
        self.fat_size_32: Optional[int] = None
        self.ext_flags: Optional[int] = None
        self.version: Optional[int] = None
        self.root_cluster: Optional[int] = None
        self.fs_info: Optional[int] = None
        self.backup_bs_sector: Optional[int] = None


class BSParamsFat:
    def __init__(self):
        self.drive_number: Optional[int] = None
        self.boot_sig: Optional[int] = None
        self.volume_id: Optional[int] = None
        self.volume_label: Optional[int] = None
        self.sys_type: Optional[int] = None
        self.boot_code: Optional[int] = None
        self.boot_sign: Optional[int] = None


class BSParams(BSParamsFat, BSParamsFat32, BSParamsCommon):
    def __init__(self):
        super().__init__()
