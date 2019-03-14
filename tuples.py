#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:48:26 2019

@author: fannieklein
"""
#Exercise 1:

me_list = ["Fannie", "Klein", 28]

me_tuple =tuple(me_list)
print(me_tuple)

print(me_tuple[0])
print(me_tuple[1])
print(me_tuple[2])

#Unpack into variables
first_name, last_name, age = me_tuple

print(first_name)
print(last_name)
print(age)

#Exercise2:

me_list =[("name", "Fannie"),
          ("age", 28),
          ("Hobbies", ["eating", "coding", "eating"]) ]

me_dict = {}

for key, value in me_list: 
    me_dict[key] = value

print(me_dict)

