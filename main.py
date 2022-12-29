from fat_parser.io_manager import IOManager
from fat_parser.parser import FatParser
from fat_parser.defragmentation import Defragmenter
import argparse


def main(arguments):
    action_type = arguments.action_type
    if action_type == "defragmentation":
        Defragmenter(FatParser(IOManager(arguments.filename))).defragmentation()
    elif action_type == "fragmentation":
        Defragmenter(FatParser(IOManager(arguments.filename))).fragmentation()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Defragmenter',
                                     description='Do (de)fragmentation')
    parser.add_argument("filename", help="name of FAT file")
    parser.add_argument("action_type", choices=["defragmentation", "fragmentation"],
                        help="Would you like to defragment or fragment your FAT file?")
    args = parser.parse_args()
    main(args)
