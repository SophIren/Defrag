from typing import Optional

from entities import FatType
from fat_parser.boot_sector import BSInfo


class RawImageInfo:
    def __init__(self, bs_params: BSInfo):
        self.bs_params = bs_params

    @property
    def start_sector(self) -> int:
        return self.bs_params.reserved_sectors_count

    @property
    def fat_size(self) -> int:
        single_fat_size = self._get_existing_param(self.bs_params.fat_size_16, self.bs_params.fat_size_32)
        return single_fat_size * self.bs_params.num_of_fats

    @property
    def total_sectors_count(self) -> int:
        return self._get_existing_param(self.bs_params.total_sectors_16, self.bs_params.total_sectors_32)

    @classmethod
    def _get_existing_param(cls, param1: Optional[int], param2: Optional[int]) -> int:
        """
        If both exist, param1 will be returned
        """

        if cls._param_exists(param1):
            return param1
        if cls._param_exists(param2):
            return param2
        raise ValueError("At least one parameter must exist")

    @staticmethod
    def _param_exists(param: Optional[int]) -> bool:
        return param is not None and param != 0

    @property
    def root_dir_start_sector(self) -> int:
        if self.bs_params.root_entries_count == 0:
            return 0
        return self.start_sector + self.fat_size

    @property
    def root_dir_sectors_count(self) -> int:
        if self.bs_params.root_entries_count == 0:
            return 0
        return (
                           32 * self.bs_params.root_entries_count + self.bs_params.bytes_per_sector - 1) // self.bs_params.bytes_per_sector

    @property
    def data_start_sector(self) -> int:
        return self.root_dir_start_sector + self.root_dir_sectors_count

    @property
    def data_sectors_count(self) -> int:
        return self.total_sectors_count - self.data_start_sector

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
