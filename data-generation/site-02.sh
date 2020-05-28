#!/bin/sh
python3 traffic_generator.py 127.0.0.1 T-1 region-04.csv &
python3 traffic_generator.py 127.0.0.1 T-2 region-05.csv &
python3 traffic_generator.py 127.0.0.1 T-3 region-06.csv &