#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 20:04:33 2019

@author: fannieklein
"""
my_list = [1,3,4,5,6]

#my_new_list = list(map(lambda n:n+1, my_list))

my_new_list = list(filter(lambda n:n>1, my_list))





print(my_new_list)
