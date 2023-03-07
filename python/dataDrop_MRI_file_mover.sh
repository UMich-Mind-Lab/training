#!/bin/bash

module purge
module load anaconda-3.7
python3 dataDrop_MRI_file_mover.py "$@"

