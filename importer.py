#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Frank@Villaro-Dixon.eu - DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE, etc.

import os
import requests
import time

SMA_SUNNYBOY_HOST = os.environ['SMA_SUNNYBOY_HOST']
#OPEN_TSDB_HOST = os.environ['OPENTSDB_HOST']
#OPEN_TSDB_METRIC = os.environ['OPEN_TSDB_METRIC']
#OPEN_TSDB_TAGS = json.loads(os.environ['OPEN_TSDB_TAGS'])

def get_data_from_sunnyboy(sma_host):
    data = requests.get(f'http://{sma_host}/dyn/getDashLogger.json', verify=False)
    energies = data.json()['result']['0199-B32FB7BF']['7000']['1']
    return energies

def send_data_to_opentsdb(data):
    pts = []
    for d in data:
        pt = {
            "metric": "energy.electricity.cumulative",
            "timestamp": int(d['t']),
            "value": float(d['v']),
            "tags": {
               "point": "solar.roof.production"
            }
        }
        print(pt)
        r = requests.post('http://192.168.10.52:4242/api/put', json=pt)
        print(r)
        print(r.status_code)




if __name__ == '__main__':
    e = get_data_from_sunnyboy('192.168.10.220')
    send_data_to_opentsdb(e)
#while True:
#    data = get_data_from_sunnyboy(SMA_SUNNYBOY_HOST)
#    send_data_to_opentsdb(data)
#    time.sleep(10m)


# vim: set ts=4 sw=4 et:

