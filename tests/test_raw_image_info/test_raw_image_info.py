from entities import FatType
from fat_parser.boot_sector import BSInfo
from fat_parser.image_info import ImageInfo


def test_fat_32_type(fat_32_bs_info: BSInfo):
    image_info = ImageInfo(fat_32_bs_info)
    assert image_info.fat_type == FatType.FAT32


def test_fat_16_type(fat_16_bs_info: BSInfo):
    image_info = ImageInfo(fat_16_bs_info)
    assert image_info.fat_type == FatType.FAT16
