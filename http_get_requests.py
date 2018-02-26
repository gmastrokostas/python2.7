#!/usr/bin/python
import requests
import threading


def get_thrasher():

    req_get  = requests.get('http://192.168.56.101/')

threads = []

for counter_1 in range(10):
    thrd = threading.Thread(target=get_thrasher())
    thrd.start()
    threads.append(thrd)

for counter_2 in threads:
    counter_2.join()
