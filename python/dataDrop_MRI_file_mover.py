#!/usr/bin/env python3

import os
from os import makedirs as mkdirs
from os.path import join as pjoin
from glob import glob
from shutil import copyfile
from shutil import move as movefile

# Placeholder variables for the family ID and wave.  These will eventually
# become command line arguments to the script.
fam  = '6486'
wave = '2'
ses  = '1'

# Directory where the original files are found
dDrop = f'/nfs/turbo/lsa-lukehyde-secure/MTwiNS/dataDrop/Wave{wave}/{fam}/MRI'

# Directory where the MRI task files should go
events = '/nfs/turbo/lsa-lukehyde/MTwiNS/mri/eventLogs'

# Must change to the directory in which glob will look
os.chdir(dDrop)

# Get just .mat file in case there are pesky .DS_Store files or .Trash files
task_files = glob('*.mat')

for file in sorted(task_files):
    # We only need the second and third items from the split
    # Example file looks like '6567_faces_t1.mat'
    task, twin = file.split('_')[1:3]

    # The first two characters of the twin will be the 't[12]' that we need
    twin = twin[:2]

    # Create the real subject ID and create the directory
    subj = f"sub-{fam}{twin}"
    taskDir = pjoin(events, subj, f"ses-{ses}")

    # Create the file names and add the full directory paths to them
    # We do not want to fail if it is already there, but we do want to fail
    # if it cannot be created.
    try:
        mkdirs(taskDir, exist_ok=True)
    except:
        print(f"Failed to create {taskDir}.  Quitting.")
        sys.exit()

    # Construct the real target path for this task file
    new_file = pjoin(taskDir, f'sub-{fam}{twin}_ses-{ses}_task-{task}_events.mat')
    # Create the full path to the dataDrop location because we cannot inside the
    # f-string
    old_file = pjoin(dDrop, file)

    # For testing, only copy the files
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
