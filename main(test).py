from fat_parser.io_manager import IOManager
from fat_parser.parser import FatParser
from fat_parser.defragmentation import Defragmenter

Defragmenter(FatParser(IOManager('tests/fat_images/fat32.img'))).defragmentation()
