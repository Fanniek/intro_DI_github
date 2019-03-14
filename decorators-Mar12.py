#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:01:01 2019

@author: fannieklein
"""
import time

#def my_decorator(my_func): 
#    def wrapper(): 
#        my_func()
#        my_func()
#        my_func()
#    return wrapper
#
#@my_decorator
#def first_name(): 
#    print("Fannie")
#
#first_name()


#def run_again_deco (func): 
#    def wrapper(): 
#        while True:
#            user_input = input("Do you want to run the code again? Y/N\n>>> ")
#            if user_input.lower() == "y": 
#                func()
#            else:
#                print("bye")
#                break
#    return wrapper
#
#@run_again_deco
#def my_func(): 
#    print("hey")
#    
#my_func()

    
#def time_deco(func): 
#    def wrapper(*args, **kwargs): 
#        start_time = time.time()
#        func()
#        end_time = time.time()
#        combine_time = end_time - start_time
#        print("It took {} sec for {} to run".format(combine_time, func.__name__))
#    return wrapper
#
#@time_deco
#def my_func(): 
#    for i in range(50000000):
#        i += 1
#        
#@time_deco
#def my_2_func(): 
#    for i in range(50000000):
#        i += 1
#
#@time_deco
#def my_3_func(): 
#    for i in range(50000000):
#        i += 1
#
#my_func()
#my_2_func()
#my_3_func()


#def few_sec_deco(func): 
#    def wrapper(*args, **kwargs): 
#        while True: 
#            time.sleep(5)
#            func()
#            break
#    return wrapper
#
#@few_sec_deco
#def my_func(): 
#    print("....goooooood morning, vieeetnaaaaam!")
#    
#my_func()

        
        
    

