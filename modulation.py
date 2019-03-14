#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 20:00:56 2019

@author: fannieklein
"""

class InputField():     
    
    def __init__(self,
                 max_lenght):   
        
        self.max_lenght = max_lenght
        
    def get_user_input(self):   
        userinput = input("[INPUT]>>> ")
        return userinput[:self.max_lenght]
    
    def display_input(self):    
        print(self.get_user_input())