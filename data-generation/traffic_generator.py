from __future__ import absolute_import

from mqtt import MqttPublishHandler
import sys
import time
import csv
import os

'''     
0 - car_make
1 - car_model
2 - engine_on
3 - otonomo_id
4 - geocoding_city
5 - time
6 - latitude
7 - longitude
8 - heading
9 - speed
10 - provider
11 - geocoding_country_long
12 - geocoding_state
13 - geocoding_town
14 - ignition
15 - geocoding_suburb
16 - geocoding_road
'''

mqtt_address = str(sys.argv[1])
pub_topic = str(sys.argv[2])
source_file = str(sys.argv[3])

# mqtt_address = "127.0.0.1"
# pub_topic = "T-1"
# source_file = "region-01.csv"

mqttph = MqttPublishHandler(mqtt_address, source_file, 'mqtt-pub', 'mqtt-pub') #host, client id, username & password
#mqttph = MqttPublishHandler('127.0.0.1', '1', 'mqtt-pub', 'mqtt-pub') #host, client id, username & password
mqttph.connect()


dirpath = os.path.dirname(os.path.abspath(__file__))
source_file = dirpath+"/regional-data/"+source_file


def publish(message):
    #print (message)
    mqttph.publish(pub_topic, message)

with open(source_file) as sample:
    csv1 = csv.reader(sample, delimiter=',')
    header = next(csv1, None)
    gen_time = "1558346400000"
    start_timer = time.time()
    end_timer = time.time()
    delay = 0
    for line in csv1:
        count = 0
        message = line[12] +":"+ str(time.time()) +":"+ line[6] +":"+ line[7] +":"+ line[0] +":"+ line[1] +":"+ line[2] \
                  +":"+ line[3] +":"+ line[4] +":"+ line[5] +":"+ line[2] +":"+ line[8] +":"+ line[8] +":"+ line[10] +":"+ line[11] \
                  +":"+ line[13] +":"+ line[14] +":"+ line[15] +":"+ line[16]
        #message = line
        # I don't remember what the lines indicated
        if line[5] == gen_time:
            count += 1
            publish(message)
        else:
            time_diff = float(line[5]) - float(gen_time)
            time.sleep(time_diff/1000) # by seconds divided by 1000 is real time
            gen_time = line[5]

end_timer = time.time()

# print ("start_time: %f" %start_timer)
# print ("end_time: %f" %end_timer)

mqttph.disconnect()


