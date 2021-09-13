#!/bin/sh
source /home/farm/develop/check_free_space/env/bin/activate
python3 /home/farm/develop/check_free_space/check_free_space.py
sleep 2
deactivate