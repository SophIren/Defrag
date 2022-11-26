from typing import List

from entities import EntryType
from fat_parser.boot_sector import BSInfo
from fat_parser.cluster.cluster_info import ClusterInfo
from fat_parser.entry.entry_parser import EntryParser
from fat_parser.fat_table.fat_table_parser import FatTableParser
from fat_parser.io_manager import IOManager
from fat_parser.image_info import ImageInfo


class ClusterParser:
    def __init__(self, io_manager: IOManager, image_info: ImageInfo, fat_table_parser: FatTableParser):
        self.io_manager = io_manager
        self.fat_table_parser = fat_table_parser
        self.image_info = image_info
        self.entry_parser = EntryParser(io_manager)

    def parse(self, fat_entry_num: int) -> ClusterInfo:
        clusters = []
        while not self.fat_table_parser.fat_entry_num_is_ending(fat_entry_num):
            cluster_pos = self._fat_entry_num_to_data_pos(fat_entry_num)
            cluster = self._parse_single_cluster(cluster_pos, self.image_info.entries_per_cluster)
            if clusters:
                clusters[-1].connect_to(cluster)
            clusters.append(cluster)
            fat_entry_num = self.fat_table_parser.get_next_cluster_pos(fat_entry_num, 1)

        return clusters[0]

    def _fat_entry_num_to_data_pos(self, fat_entry_num) -> int:
        sector_num = self.image_info.data_start_sector + (fat_entry_num - 2) * self.image_info.bs_info.sectors_per_cluster
        return sector_num * self.image_info.bs_info.bytes_per_sector

    def _parse_single_cluster(self, cluster_start_pos: int, entries_count: int) -> ClusterInfo:
        fat_entry_pos = cluster_start_pos
        entries = []
        for _ in range(entries_count):
            entry = self.entry_parser.parse(fat_entry_pos)
            fat_entry_pos += EntryParser.ENTRY_SIZE
            if entry.type == EntryType.EMPTY:
                continue
            if entry.type == EntryType.EMPTY_ENDING:
                break
            entries.append(entry)

        return ClusterInfo(entries)