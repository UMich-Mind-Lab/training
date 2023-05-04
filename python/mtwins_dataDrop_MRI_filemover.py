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
dDrop = f'/nfs/turbo/lsa-lukehyde-secure/MTwiNS/dataDrop/Wave{args.wave}/{args.familyid}/MRI'
# Directory where the MRI task files should go
raw = f'/nfs/turbo/lsa-lukehyde/rawdata_DONOTmodify/mtwins/behavioral/time{args.wave}/mri_tasks'

# Must change to the directory in which glob will look
os.chdir(dDrop)

# Get just .mat file in case there are pesky .DS_Store files or .Trash files
task_files = glob('*.mat')

for file in sorted(task_files):
    if 'gonogo' in file:
        # assign task to gng
        gng_task = 'gng'

        # Construct the real target path for this task file
        new_file = pjoin(raw, gng_task, file)
        # Construct path to the dataDrop location
        old_file = pjoin(dDrop, file)
    else:
        # We only need the second and third items from the split Example
        # file looks like '6567_faces_t1.mat'
        task = file.split('_')[1]

        # Construct the real target path for this task file
        new_file = pjoin(raw, task, file)
        # Construct path to the dataDrop location
        old_file = pjoin(dDrop, file)

    print(f'\nMoving {old_file}\n to {new_file}')
   
    try:
        movefile(old_file, new_file)
    except:
        print("Something went wrong moving", os.path.basename(old_file),
              "to", os.path.basename(new_file))
        print("Investigate and fix it.  Quitting\n")
        sys.exit()
