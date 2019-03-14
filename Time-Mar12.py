#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:22:41 2019

@author: fannieklein
"""

import time

#print(time.time())

today = time.ctime(time.time())
#
#chosen_today = time.gmtime(time.time())
#
#today_struct = time.gmtime(time.time())
#
#print(today)
##print(chosen_today.tm_year)
##print("Today is the {} {} of the year {}".format(today_struct.tm_mon, today_struct.tm_mday, today_struct.tm_year))
#
#print("Hey....")
#time.sleep(5)
#print("Good Morning!!")


def today_date(): 
    today = time.gmtime(time.time())
    print("{}/{}-{}".format(today.tm_mday,today.tm_mon,today.tm_year))
    
#today_date()

def hello(): 
    while True: 
        print("Hello There....")
        time.sleep(5)

#hello()

def hour(): 
    hour = time.gmtime(time.time())
    while True: 
        print("{}".format(hour.tm_hour))
        time.sleep(5)
hour()