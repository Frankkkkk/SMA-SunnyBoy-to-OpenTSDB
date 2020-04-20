#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Frank@Villaro-Dixon.eu - DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE, etc.

import os
import requests
import time

SMA_SUNNYBOY_HOST = os.environ['SMA_SUNNYBOY_HOST']
OPEN_TSDB_HOST = os.environ['OPEN_TSDB_HOST']
OPEN_TSDB_METRIC = os.environ['OPEN_TSDB_METRIC']
OPEN_TSDB_POINT_NAME = os.environ['OPEN_TSDB_POINT_NAME']


def get_data_from_sunnyboy(sma_host):
    data = requests.get(f'http://{sma_host}/dyn/getDashLogger.json', verify=False)
    energies = data.json()['result']['0199-B32FB7BF']['7000']['1']
    return energies


def send_data_to_opentsdb(data):
    for d in data:
        try:
            pt = {
                "metric": OPEN_TSDB_METRIC,
                "timestamp": int(d['t']),
                "value": float(d['v']),
                "tags": {
                   "point": OPEN_TSDB_POINT_NAME,
                }
            }
            # XXX send an array instead of scalars
            r = requests.post('http://{OPEN_TSDB_HOST}/api/put', json=pt)
        except:
            print(f'No data for pt {d}. Maybe inverter was down')


if __name__ == '__main__':
    while True:
        e = get_data_from_sunnyboy('192.168.10.220')
        send_data_to_opentsdb(e)
        time.sleep(60 * 60)

# vim: set ts=4 sw=4 et:

