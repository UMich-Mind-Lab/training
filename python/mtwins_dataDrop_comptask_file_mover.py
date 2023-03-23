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
dDrop = f'/nfs/turbo/lsa-lukehyde-secure/MTwiNS/dataDrop/Wave{wave}/{fam}/Computer_Tasks'

# Directory where the computer tasks should go
computer = f'/nfs/turbo/lsa-lukehyde/MTwiNS/time{wave}/behavioral/tasks/computer'

# Must change to the directory in which glob will look
os.chdir(dDrop)

# Get just .jpg files in case there are pesky .DS_Store files or .Trash files
task_files = glob('*.mat')


for file in sorted(task_files):
    # assign origin filepath
    old_file = pjoin(dDrop, file)

    # We only need the second item from the split
    # Example file looks like '6567_bart_t1.mat'
    task = file.split('_')[1:2]

    # Create the real subject ID and create the directory
    taskDir = pjoin(computer, task, file)
    
    
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
