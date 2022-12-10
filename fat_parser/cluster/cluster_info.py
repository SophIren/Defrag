from __future__ import annotations
from typing import List, Optional, Iterable

from fat_parser.entry.entry_info import EntryInfo


class ClusterInfo:
    def __init__(self, entries: List[EntryInfo], connected_to: Optional[ClusterInfo] = None):
        self.entries = entries
        self.data_start_pos: Optional[int] = None
        self.fat_entry_num: Optional[int] = None
        self.connected_to: Optional[ClusterInfo] = connected_to

    def connect_to(self, cluster: ClusterInfo):
        self.connected_to = cluster

    def __iter__(self) -> Iterable[ClusterInfo]:
        current = self
        while current.connected_to is not None:
            yield current
            current = current.connected_to
        yield current

    @property
    def is_file_content(self) -> bool:
        if len(self.entries) > 0:
            return self.entries[0].is_file_content
        return False
