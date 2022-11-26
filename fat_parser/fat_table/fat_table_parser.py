from fat_parser.fat_table.fat_table_params import FatTableParams
from fat_parser.io_manager import IOManager
from fat_parser.image_info import ImageInfo


class FatTableParser:
    def __init__(self, io_manager: IOManager, image_info: ImageInfo, params: FatTableParams):
        self.image_info = image_info
        self.io_manager = io_manager
        self.params = params

    def get_next_cluster_pos(self, fat_entry_num: int, table_num: int) -> int:
        if self.params.ENTRY_LENGTH is None:
            raise ValueError

        start_sector = self.image_info.start_sector + (table_num - 1) * self.image_info.fat_size
        offset = fat_entry_num * self.params.ENTRY_LENGTH
        start_pos = start_sector * self.image_info.bs_info.bytes_per_sector + offset

        self.io_manager.seek(start_pos)
        return self.io_manager.read_int(self.params.ENTRY_LENGTH)

    def fat_entry_num_is_ending(self, fat_entry_num: int) -> bool:
        if self.params.ENDING_FAT_ENTRY_NUM is None:
            raise ValueError
        return fat_entry_num >= self.params.ENDING_FAT_ENTRY_NUM
