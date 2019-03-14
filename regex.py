#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:10:12 2019

@author: fannieklein
"""
import re


#my_string = "jyrvbjhdbjfvercnbjehrf.http:\\www.facebook.comhbadjhbsjefb\https:\\www.twitter.com"
#regex = re.search(r"https?:\\w{3}.[a-z]+.com", my_string)
#
#my_emails = "klein.fannie@gmail.com,akatarinaklein@gmail.com"
#email = re.findall(r"[a-z.?]+.?@gmail.com", my_emails)
#
#print(regex)
#print(email)

#file = r"/Users/fannieklein/Downloads/equality.txt"
#with open(file, "r") as f:
#    find_all = re.findall(r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", f.read())
#    print(''.join(find_all))

number = input("Please give me your number!\n>>>")

is_number = re.search(r"^[0-9]{10}$", number)
if not is_number: 
    print("This is not a number, try again")
else:
    print("This is a number")