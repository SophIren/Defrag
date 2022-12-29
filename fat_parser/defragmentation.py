import random

from fat_parser.io_manager import IOManager
from fat_parser.parser import FatParser
from math import inf
from typing import List
from fat_parser.cluster.cluster_info import ClusterInfo


class Defragmenter:
    def __init__(self, fat_parser: FatParser):
        self.fat_parser = fat_parser
        self.io_manager = fat_parser.io_manager
        self.clusters_info = fat_parser.parse()

    @staticmethod
    def get_chain_start_position(chain: List[ClusterInfo]) -> int:
        min_pos = inf
        for cluster in chain:
            if min_pos > cluster.data_start_pos:
                min_pos = cluster.data_start_pos
        return min_pos

    def write_position_in_fat_tables(self, cluster: ClusterInfo, current_pos: int) -> None:
        for fat_number in range(1, self.fat_parser.bs_info.num_of_fats + 1):
            self.fat_parser.fat_table_parser.write_cluster_start_pos(cluster.fat_entry_num, fat_number, current_pos)

    def defragmentation(self) -> None:
        for chain in self.clusters_info:
            if len(chain) == 1:
                continue
            current_pos = self.get_chain_start_position(chain)
            for i in range(len(chain)):
                self.io_manager.seek(current_pos)
                for entry in chain[i].entries:
                    if entry._bytes is None:
                        self.io_manager.read(32)
                        continue
                    self.io_manager.write_bytes(entry._bytes)
                last_pos = self.fat_parser.image_info.cluster_size * (i + 1) + current_pos
                self.write_position_in_fat_tables(chain[i], current_pos)
                current_pos = last_pos

    def fragmentation(self):
        for chain in self.clusters_info:
            if len(chain) == 1:
                continue
            current_pos = self.get_chain_start_position(chain)
            index = 1
            while chain:
                cluster = random.choice(chain)
                self.io_manager.seek(current_pos)
                for entry in cluster.entries:
                    if entry._bytes is None:
                        break
                    self.io_manager.write_bytes(entry._bytes)
                last_pos = self.fat_parser.image_info.cluster_size * (index + 1) + current_pos
                self.write_position_in_fat_tables(cluster, current_pos)
                current_pos = last_pos
                index += 1
                chain.remove(cluster)


if __name__ == '__main__':
    Defragmenter(FatParser(IOManager('../tests/fat_images/fat32.img'))).fragmentation()
