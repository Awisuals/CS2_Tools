'''
Copyright (c) 2025 Antero Voutilainen
Created: 05 09 2025

Description: Helper script to download cs2 maps from refrag.
'''
from pathlib import Path
import requests

# location of this script
script_dir = Path(__file__).resolve().parent 

def format_maps(map_txt):
    """Formats maps with relevant file extension.
    Reads from txt.

    Args:
        map_txt (txt file): list of map names

    Returns:
        list: List of map strings with file ext.
    """
    
    # file next to the script
    file_path = script_dir / map_txt
    
    f = open(file_path, "r")
    maps = f.read().splitlines()
    f.close()
    file_ext = "_radar.svg"
    for i, map in enumerate(maps):
        maps[i] = map + file_ext
    return maps


def download_and_save_maps(map):
    """Request url and download + writes svg file from
    requested url.

    Args:
        map (string): name of the file downloaded
    """
    
    url = "https://play.refrag.gg/maps/" + map
    r = requests.get(url)

    with open(script_dir / map, "wb") as f:
        f.write(r.content)

    return


if __name__=='__main__':
    
    maps = format_maps("map_list.txt")
    print(maps)

    for i, map in enumerate(maps):
        download_and_save_maps(map)

