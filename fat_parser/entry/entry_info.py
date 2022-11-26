from typing import Optional

from entities import EntryType


class EntryInfo:
    def __init__(self):
        self.type: Optional[EntryType] = None
        self.name: Optional[int] = None
        self.attr: Optional[int] = None
        self.nt_res: Optional[int] = None
        self.crt_time_tenth: Optional[int] = None
        self.crt_time: Optional[int] = None
        self.crt_date: Optional[int] = None
        self.lst_acc_date: Optional[int] = None
        self.fat_cluster_hi: Optional[int] = None
        self.wrt_time: Optional[int] = None
        self.wrt_date: Optional[int] = None
        self.fat_cluster_lo: Optional[int] = None
        self.file_size: Optional[int] = None

    @property
    def cluster_pos(self) -> int:
        if self.fat_cluster_hi is None:
            return self.fat_cluster_lo
        return self.fat_cluster_lo + (self.fat_cluster_hi << 16)