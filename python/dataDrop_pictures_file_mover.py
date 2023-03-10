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
    if "hair" in filename:
        new_file = pjoin(hair_loc, file)

    else:
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
