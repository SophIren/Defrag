from fat_parser.io_manager import IOManager
from fat_parser.parser import FatParser

FatParser(IOManager('tests/fat_images/fat32.img')).parse()
