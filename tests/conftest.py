import sys

import pytest
import os

from fat_parser.io_manager import IOManager


@pytest.fixture()
def fat_images_path() -> str:
    return os.path.join(os.path.dirname(__file__), "fat_images")


@pytest.fixture()
def fat_32_image_file_name() -> str:
    return "fat32.img"


@pytest.fixture()
def fat_16_image_file_name() -> str:
    return "fat16.img"


@pytest.fixture()
def fat_32_io_manager(fat_images_path: str, fat_32_image_file_name: str) -> IOManager:
    return IOManager(
        os.path.join(fat_images_path, fat_32_image_file_name)
    )


@pytest.fixture()
def fat_16_io_manager(fat_images_path: str, fat_16_image_file_name: str) -> IOManager:
    return IOManager(
        os.path.join(fat_images_path, fat_16_image_file_name)
    )
