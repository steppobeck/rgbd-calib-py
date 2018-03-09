#!/bin/bash

# get directory of script
DIR="$( cd "$( dirname "$0" )" && pwd )"

# if not, this path will be used
GUACAMOLE=/opt/guacamole/master
AVANGO=/opt/avango/master

# schism
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/schism/current/lib/linux_x86

# avango
export LD_LIBRARY_PATH=$AVANGO/lib:$LD_LIBRARY_PATH:/opt/lamure/install/lib:/opt/Awesomium/lib
export PYTHONPATH=$AVANGO/lib/python3.5:$AVANGO/examples:/home/steppo/Desktop/my-git/rgbd-calib-py/lib

# guacamole
export LD_LIBRARY_PATH="$LOCAL_GUACAMOLE/lib":$GUACAMOLE/lib:$LD_LIBRARY_PATH


# run program
cd "$DIR" && env DISPLAY=:0.0 python3.5 ./main.py $1


