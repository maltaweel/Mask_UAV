#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
echo 'segment path set'

source ./run_segment.sh
python ./gui/segment_gui.py
