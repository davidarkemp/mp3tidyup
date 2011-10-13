#!/usr/bin/env python
from os import walk, rmdir
from sys import argv
from os.path import join, realpath

def safe_name(name):
    return name.replace('/', '-').replace('\\', '_')

if __name__ == "__main__":
    
    all_files = []
    
    start_path = argv[1]
    for root, _, files in walk(start_path):
        if not files and not _:
            all_files.append(realpath(join(start_path,root)))

    for empty in all_files:
        try:
            print(empty)
        except:
            pass
        try:
            rmdir(empty)
        except:
            pass
