from entities import EntryType
from fat_parser.entry.entry_info import EntryInfo
from fat_parser.io_manager import IOManager


class EntryParser:
    ENTRY_SIZE = 32

    def __init__(self, io_manager: IOManager):
        self.io_manager = io_manager

    def parse(self, entry_start_pos: int) -> EntryInfo:
        entry_info = EntryInfo()
        self.io_manager.seek(entry_start_pos)

        type_mark = self.io_manager.read_int(1)
        entry_info.type = self.get_type(type_mark)
        self.io_manager.rollback(1)

        entry_info.name = self.io_manager.read_int(11)
        entry_info.attr = self.io_manager.read_int(1)
        entry_info.nt_res = self.io_manager.read_int(1)
        entry_info.crt_time_tenth = self.io_manager.read_int(1)
        entry_info.crt_time = self.io_manager.read_int(2)
        entry_info.crt_date = self.io_manager.read_int(2)
        entry_info.lst_acc_date = self.io_manager.read_int(2)
        entry_info.fat_cluster_hi = self.io_manager.read_int(2)
        entry_info.wrt_time = self.io_manager.read_int(2)
        entry_info.wrt_date = self.io_manager.read_int(2)
        entry_info.fat_cluster_lo = self.io_manager.read_int(2)
        entry_info.file_size = self.io_manager.read_int(4)

        return entry_info

    @staticmethod
    def get_type(mark: int):
        if mark == 0xe5:
            return EntryType.EMPTY
        if mark == 0x00:
            return EntryType.EMPTY_ENDING
        return EntryType.USED
