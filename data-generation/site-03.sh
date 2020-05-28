#!/bin/sh
python3 traffic_generator.py 127.0.0.1 T-1 region-07.csv &
python3 traffic_generator.py 127.0.0.1 T-2 region-08.csv &
python3 traffic_generator.py 127.0.0.1 T-3 region-09.csv &
python3 traffic_generator.py 127.0.0.1 T-4 region-10.csv &