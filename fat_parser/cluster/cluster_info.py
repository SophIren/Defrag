from __future__ import annotations
from typing import List, Optional, Iterable

from fat_parser.entry.entry_info import EntryInfo


class ClusterInfo:
    def __init__(self, entries: List[EntryInfo], connected_to: Optional[ClusterInfo] = None):
        self.entries = entries
        self.connected_to: Optional[ClusterInfo] = connected_to

    def connect_to(self, cluster: ClusterInfo):
        self.connected_to = cluster

    def __iter__(self) -> Iterable[ClusterInfo]:
        current = self
        while current.connected_to is not None:
            yield current
            current = self.connected_to
        yield current
