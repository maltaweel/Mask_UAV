#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
echo 'path set'

source ./run_training.sh
python ./gui/train_gui.py
