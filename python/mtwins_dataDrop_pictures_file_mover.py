#!/usr/bin/env python3

import os
from os import makedirs as mkdirs
from os.path import join as pjoin
from glob import glob
from shutil import copyfile
from shutil import move as movefile
import argparse
import sys

parser = argparse.ArgumentParser()

# familyid command line input
parser.add_argument("-f", "--familyid", help="Print family ID.")
# wave command line input
parser.add_argument("-w", "--wave", help="print wave (2 or 3).")

# Actually parse the defined arguments
args = parser.parse_args()


# Directory where the original files are found
dDrop = f'/nfs/turbo/lsa-lukehyde-secure/MTwiNS/dataDrop/Wave{args.wave}/{args.familyid}/Pictures'
# Directory where the picture should go
fampic_loc = f'/nfs/turbo/lsa-lukehyde-secure/MTwiNS/Data/time{args.wave}/family_picture'
hair_loc = f'/nfs/turbo/lsa-lukehyde/MTwiNS/time{args.wave}/hair_cort'


# Must change to the directory in which glob will look
os.chdir(dDrop)

# Get just .jpg files in case there are pesky .DS_Store files or .Trash files
pictures = glob('*.jpg')

for file in sorted(pictures):
    # assign origin filepath
    old_file = pjoin(dDrop, file)

    # construct real target path, based on whether a hair or family picture
    if "hair" in file:
        # We only need the second and third items from the split
        # Example file looks like '911t1_hair.jpg'
        s, pic = file.split('_')

        # The first two characters of the twin will be the 't[12]' that we need
        s = s[len(s) - 2:]

        # Rename hair .JPG files
        file = f'{args.familyid}_hair_{s}.jpg'

        # Construct the real target path for hair picture files
        new_file = pjoin(hair_loc, file)
        
    elif "family" in file:
        # Construct the real target path for family picture file
        new_file = pjoin(fampic_loc, file)

    else:
        print('Something is wrong with the file name, check files in Picture folder')
        # Need to add more to this condition
        sys.exit()

    print(f'\nMoving {old_file}\n  to {new_file}')
    
    try:
        movefile(old_file, new_file)
    except:
        print("Something went wrong moving", os.path.basename(old_file),
              "to", os.path.basename(new_file))
        print("Investigate and fix it.  Quitting\n")
        sys.exit()

