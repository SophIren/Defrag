from entities import FatType
from fat_parser.boot_sector import BSInfo
from fat_parser.raw import RawImageInfo


def test_fat_32_type(fat_32_bs_info: BSInfo):
    image_info = RawImageInfo(fat_32_bs_info)
    assert image_info.fat_type == FatType.FAT32


def test_fat_16_type(fat_16_bs_info: BSInfo):
    image_info = RawImageInfo(fat_16_bs_info)
    assert image_info.fat_type == FatType.FAT16
