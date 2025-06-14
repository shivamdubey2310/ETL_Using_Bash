#!/bin/bash

set -e    # For exiting on error
NOW=`date '+%F %H:%M:%S'`;  # A variable for current date and time

# For Distinguishing every run in pipeline
echo "-------------------------------------------------------------------" >> logs/pipeline.log
echo "$NOW - INFO - Starting Pipeline" >> logs/pipeline.log


# Logging and calling Extraction.sh
echo "$NOW - INFO - Starting extraction" >> logs/pipeline.log
BashScripts/./Extraction.sh
echo "$NOW - INFO - Completed extraction" >> logs/pipeline.log


# Logging and calling Transform.py
echo "$NOW - INFO - Starting Transformation" >> logs/pipeline.log
python3 PythonScripts/Transform.py
echo "$NOW - INFO - Completed Transformation" >> logs/pipeline.log


# Logging and calling CreateTable.py
echo "$NOW - INFO - Starting CreateTable" >> logs/pipeline.log
python3 PythonScripts/CreateTable.py
echo "$NOW - INFO - Completed CreateTable" >> logs/pipeline.log


# # Logging and calling Load.sh
echo "$NOW - INFO - Starting Loading" >> logs/pipeline.log
BashScripts/./Load.sh
echo "$NOW - INFO - Completed Loading" >> logs/pipeline.log


# End of the pipeline
echo "$NOW - INFO - Pipeline run successfully" >> logs/pipeline.log
echo "-------------------------------------------------------------------" >> logs/pipeline.log