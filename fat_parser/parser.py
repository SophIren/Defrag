from entities import FatType
from fat_parser.boot_sector import BSParser, BSInfo
from fat_parser.cluster.cluster_parser import ClusterParser
from fat_parser.fat_table.fat_table_params import Fat32TableParams, Fat16TableParams
from fat_parser.fat_table.fat_table_parser import FatTableParser
from fat_parser.image_info import ImageInfo
from fat_parser.io_manager import IOManager


class FatParser:
    def __init__(self, io_manager: IOManager):
        self.io_manager = io_manager

        self.bs_info = BSInfo()
        self.bs_parser = BSParser(io_manager, self.bs_info)
        self.image_info = ImageInfo(self.bs_info)

        self.bs_parser.parse_common_fields()
        if self.image_info.fat_type == FatType.FAT32:
            self.bs_parser.parse_fat32_fields()
            fat_table_params = Fat32TableParams()
        else:
            self.bs_parser.parse_fat16_fields()
            fat_table_params = Fat16TableParams()

        self.fat_table_parser = FatTableParser(io_manager, self.image_info, fat_table_params)
        self.cluster_parser = ClusterParser(io_manager, self.image_info, self.fat_table_parser)

    def parse(self):
        if self.image_info.fat_type == FatType.FAT32:
            root_dir_start = self.bs_info.root_cluster
        else:
            root_dir_start = self.image_info.root_dir_start_sector // self.image_info.bs_info.sectors_per_cluster

        root_chain = self.cluster_parser.parse(root_dir_start)
        stack = [root_chain]
        while stack:
            current_chain = stack.pop()
            for cluster in current_chain:
                for entry in cluster.entries:
                    if entry.attr.directory and not entry.is_auxiliary:
                        new_chain = self.cluster_parser.parse(entry.fat_entry_start)
                        stack.append(new_chain)
                print(list(map(lambda entry: entry.name, cluster.entries)))
