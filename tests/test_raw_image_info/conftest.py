import pytest

from fat_parser.io_manager import IOManager
from fat_parser.boot_sector import BSInfo, BSParser


@pytest.fixture()
def fat_32_bs_info(fat_32_io_manager: IOManager) -> BSInfo:
    bs_info = BSInfo()
    parser = BSParser(fat_32_io_manager, bs_info)
    parser.parse_common_fields()
    parser.parse_fat32_fields()
    return parser.bs_info


@pytest.fixture()
def fat_16_bs_info(fat_16_io_manager: IOManager) -> BSInfo:
    bs_info = BSInfo()
    parser = BSParser(fat_16_io_manager, bs_info)
    parser.parse_common_fields()
    parser.parse_fat16_fields()
    return parser.bs_info
