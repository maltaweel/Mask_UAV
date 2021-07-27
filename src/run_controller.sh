export PYTHONPATH=$PYTHONPATH:$(pwd)
echo 'path set'

source ./run_controller.sh
python ./gui/controller.py

