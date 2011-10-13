#!/usr/bin/env python
from os import walk, makedirs
from sys import argv
from os.path import join, realpath, splitext, exists
from shutil import move
from stagger import read_tag, NoTagError

def safe_name(name):
    return name.replace('/', '-').replace('\\', '_')

if __name__ == "__main__":
    
    all_files = []
    
    start_path = argv[1]
    for root, _, files in walk(start_path):
        for file_ in files:
            all_files.append(
                realpath(join(start_path,root,file_)))

    for tagged in all_files:
        try:
            tag = read_tag(tagged)
            _, ext = splitext(tagged)

            counter = 0
            artist = safe_name(tag.album_artist or tag.artist or 'unknown') 
            album = safe_name(tag.album or 'unknown')
            extra = ""
            target_path = join(start_path, artist, album)

            while True:

                filename = safe_name("%02i - %s - %s - %s%s%s" % (
                            tag.track or 0,
                            tag.title[:150] or 'unknown',
                            tag.artist or tag.album_artist or 'unknown',
                            album,
                            extra,
                            ext
                        ))

                new_path = join(
                    target_path,
                    filename
                    )

                if tagged == new_path:
                    break

                if exists(new_path):
                    counter += 1
                    extra = "%02i" % counter
                    continue
                print(new_path)
                if not exists(target_path):
                    makedirs(target_path)
                move(tagged,new_path)
                break

        except NoTagError:
            continue
