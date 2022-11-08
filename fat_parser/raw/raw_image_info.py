from fat_parser import BSParams
from fat_parser import IOManager

from entities import FatType


class RawImageInfo:
    def __init__(self, io_manager: IOManager):
        self.io_manager = io_manager
        self.bs_params = BSParams()

    @property
    def start_sector(self) -> int:
        return self.bs_params.reserved_sectors_count

    @property
    def total_sectors(self) -> int:
        if self.bs_params.total_sectors_16 == self.bs_params.total_sectors_32 == 0:
            raise ValueError("BPB_TotSec16 and BPB_TotSec32 both must not be zero")

        if self.bs_params.total_sectors_16 == 0:
            return self.bs_params.num_of_fats * self.bs_params.total_sectors_16
        if self.bs_params.total_sectors_32 == 0:
            return self.bs_params.num_of_fats * self.bs_params.total_sectors_32

        raise ValueError("Either BPB_TotSec16 or BPB_TotSec32 must be zero")

    @property
    def root_dir_start_sector(self) -> int:
        if self.bs_params.root_entries_count == 0:
            return 0
        return self.start_sector + self.total_sectors

    @property
    def root_dir_sectors_count(self) -> int:
        if self.bs_params.root_entries_count == 0:
            return 0
        return (32 * self.bs_params.root_entries_count + self.bs_params.bytes_per_sector - 1) // self.bs_params.bytes_per_sector

    @property
    def data_start_sector(self) -> int:
        return self.root_dir_start_sector + self.root_dir_sectors_count

    @property
    def data_sectors_count(self) -> int:
        return self.total_sectors - self.data_start_sector

    @property
    def clusters_count(self) -> int:
        return self.data_sectors_count // self.bs_params.sectors_per_cluster

    @property
    def fat_type(self) -> FatType:
        if self.clusters_count <= 4085:
            return FatType.FAT12
        if self.clusters_count <= 65525:
            return FatType.FAT16
        return FatType.FAT32
