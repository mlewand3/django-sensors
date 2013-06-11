#! /bin/bash

# Where am I?
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source "$DIR/../env/bin/activate"

python "$DIR/read-sensors.py"