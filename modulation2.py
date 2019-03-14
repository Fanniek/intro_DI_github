#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 20:04:47 2019

@author: fannieklein
"""
import modulation

class PasswordInputField(modulation.InputField):    
    def __init__(self,
                 max_lenght):   
        super().__init__(max_lenght)
        
    def display_input(self):    
        userinput = self.get_user_input()
        print("*"*len(userinput))
        
pwd = PasswordInputField(10)
pwd.display_input()