#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:26:25 2019

@author: fannieklein
"""

import threading
import time

def rabbit(event): 
    pos = 0
    while event.is_set() == False:
        time.sleep(1)
        pos += 1
    print("I did {} meters".format(pos))

def turtle(event): 
    pos = 0
    while event.is_set() == False: 
        time.sleep(2)
        pos += 1
    print("I did {} meters".format(pos))

race_event    = threading.Event()
rabbit_thread = threading.Thread(target=rabbit, args=[race_event])
turtle_thread = threading.Thread(target=turtle, args=[race_event])           

print("GO!")

rabbit_thread.start()
turtle_thread.start()

time.sleep(10)
race_event.set()