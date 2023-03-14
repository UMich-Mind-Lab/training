#!/usr/bin/env python3

import os
from os import makedirs as mkdirs
from os.path import join as pjoin
from glob import glob
from shutil import copyfile
from shutil import move as movefile

# Placeholder variables for the family ID and wave.  These will eventually
# become command line arguments to the script.
fam  = '763'
wave = '3'

# Directory where the original files are found
dDrop = f'/nfs/turbo/lsa-lukehyde-secure/MTwiNS/dataDrop/Wave{wave}/{fam}/Interaction_Tasks'

# Directory where the MRI task files should go
lunch_loc = '/nfs/turbo/lsa-lukehyde-secure/MSU_Share_MTwiNS/time{wave}/lunch'
ht_loc = '/nfs/turbo/lsa-lukehyde-secure/MSU_Share_MTwiNS/time{wave}/interaction_tasks/hottopics'
ksads_loc = 'nfs/turbo/lsa-lukehyde-secure/MTwiNS/Data/time{wave}/clinical_interviews'

# Must change to the directory in which glob will look
os.chdir(dDrop)

# Get just .mp4 or .asf file in case there are pesky .DS_Store files or .Trash files
# figure out how to select multiple file types: some files are saved as .mp4
videos = glob('*.asf')

for file in sorted(videos):
    # Create the full path to the dataDrop location because we cannot inside the
    # f-string
    old_file = pjoin(dDrop, file)
    
    # Condition 1: select files with twin specific data (hottopics, ksads)
    if "t1" or "t2" in file:
        # e.g filename '763t1_hottopics.mp4' or '763t1_ksads.mp4'
        # or '763t1_ksads_parent.mp4'
        name = file.removesuffix('.mp4')
        name = file.split('_')
        # The first two characters of the twin will be the 't[12]' that we need
        s = name[0][-2:]
        # '.extend' the list {s} and ".asf" to correctly rename file 
        name.extend([s, ".asf"])
        # Replace familyid and twin number (e.g., 763t1) with fam variable
        name[0] = fam
        # Use list components to create new file name
        vid_file = "_".join(name)
        
        # Nested Condition 1: Select files with ksads video
        if "ksads" in file:
            # if it is a parent ksads, save the file in parent folder  
            if "parent" in file:
                new_file = pjoin(ksads_loc, "parent", vid_file)
            # if the ksads video name does not have parent in the name, save file in twin folder
            else:
                new_file = pjoin(ksads_loc, "twin", vid_file)
        # Nested Condition 2: select file with hottopics in the name
        elif "hottopics" in file:
            new_file = pjoin(ht_loc, vid_file)
        else:
            print("check hottopics and/or ksads file names, script did not work")
    
    # Condition 2: files with no twin specific data (should only be lunch files)
    elif "lunch" in file:
        new_file = pjoin(lunch_loc, file)
    
    # Condition 3: Error in finding tasks
    else:
        print(f' Error in finding file type in script for {fam} Wave {wave}')

       
    # For testing, only copy the files
    print(f'\nMoving {old_file}\n  to {new_file}')
    try:
        copyfile(old_file, new_file)
        # Comment or remove above line and uncomment following when ready to move.
        # movefile(old_file, new_file)
    except:
        print("Something went wrong moving", os.path.basename(old_file),
              "to", os.path.basename(new_file))
