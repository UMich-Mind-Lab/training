#!/usr/bin/env python3

import os
from os import makedirs as mkdirs
from os.path import join as pjoin
from glob import glob
from shutil import copyfile
from shutil import move as movefile

# Placeholder variables for the family ID and wave.  These will eventually
# become command line arguments to the script.
fam  = '911'
wave = '2'

# Directory where the original files are found
dDrop = f'/nfs/turbo/lsa-lukehyde-secure/MTwiNS/dataDrop/Wave{wave}/{fam}/Pictures'

# Directory where the picture should go
fampic_loc = f'/nfs/turbo/lsa-lukehyde-secure/MTwiNS/Data/time{wave}/family_picture'
hair_loc = f'/nfs/turbo/lsa-lukehyde/MTwiNS/time{wave}/hair_cort'

# Must change to the directory in which glob will look
os.chdir(dDrop)

# Get just .JPG files in case there are pesky .DS_Store files or .Trash files
pictures = glob('*.JPG')

for file in sorted(pictures):
    # assign origin filepath
    old_file = pjoin(dDrop, file)

    # construct real target path, based on whether a hair or family picture
    if "hair" in file:
        # We only need the second and third items from the split
        # Example file looks like '911t1_hair.JPG'
        s, pic = file.split('_')

        # The first two characters of the twin will be the 't[12]' that we need
        s = s[length - 2:]

        # Rename hair .JPG files
        hair_file = f'{fam}_hair_{s}.JPG'

        # Construct the real target path for hair picture files
        new_file = pjoin(hair_loc, hair_file)

    else:
        # Construct the real target path for family picture file        
        new_file = pjoin(fampic_loc, file)

    print(f'\nMoving {old_file}\n  to {new_file}')
    try:
        copyfile(old_file, new_file)
        # Comment or remove above line and uncomment following when ready to move.
        # movefile(old_file, new_file)
    except:
        print("Something went wrong moving", os.path.basename(old_file),
              "to", os.path.basename(new_file))
        print("Investigate and fix it.  Quitting\n")
        sys.exit()
