#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 17:40:24 2019

@author: fannieklein
"""

# =============================================================================
# my_dict = {"name": "Eyal", "age":20,} # key: value
# =============================================================================

#Exercises:
# 1. Person
# =============================================================================
# person = {
#         "first": "Fannie",
#         "last": "Klein",
#         "Age": "28",
#         "City": "Tel Aviv"
#         }
# print("The first name is {} and the last name is {}".format(person["first"],person["last"]))
# 
# 
# =============================================================================

#
# =============================================================================
# def a_and_b(nb):    
#     before = nb - 1
#     after = nb + 1
#     
#     return before, after
# 
# answer1, answer2 = a_and_b(5)
# print(answer1, answer2)
# =============================================================================
    # =============================================================================
# ==============
# 1: Capitals exercise:

# =============================================================================
# country_capital = {
#         "Sweden": "Stockholm",
#         "France": "Paris",
#         "Israel": "Jerusalem"
#         }
# 
# =============================================================================
# =============================================================================
# for key, value in country_capital.items(): 
#     print("The capital of {} is {}".format(key, value))
# =============================================================================
    
# =============================================================================
# for key in country_capital.keys(): 
#     print("The country is {}".format(key))
# =============================================================================
    
# =============================================================================
# for value in country_capital.values(): 
#     print("The City is {}".format(value))
# =============================================================================

# =============================================================================
# def whats_your_age(): 
#     age = input("What is your age?\n>>> ")
#     
#     try:    
#         age = int(age)
#     except ValueError: 
#         age = 0
#     
#     print("You are {} years old".format(age))
#     age += 1
#     print("The next year, you will be {} years old".format(age))
# 
# whats_your_age()
# =============================================================================


#Exercise:
# =============================================================================
# 1 : User input checking
# Write a function that ask two persons for their ages, and then returns who is 
# older. Don't let them input something that is not an integer.
# 
# def person(): 
#     age1 = input("What is your age?\n>>> ")
#     age2 = input(" and what is your age?\n>>> ")
#     
#     try:    
#         age1 = int(age1)
#         age2 = int(age2)
#     except: 
#         print("You need to enter a number!\n>>>")
#         return False
#     
#     if age1 > age2: 
#         print("{} is older than {}".format(age1, age2))
#     else:
#         print("{} is older than {}".format(age2, age1))
#     
#     age1 += 1
#     age2 += 1
# person()
#     
# =============================================================================
my_list_1 = ['France', 'Italy', 'England']
my_list_2 = ['Paris', 'Roma', 'London']


def my_function (my_list_1, my_list_2): 
    new_dict = {}
    i = 0
    while i == len(my_list_1) and i == len(my_list_2):  
        country = my_list_1[i]
        city = my_list_2[i]
        new_dict[country]=city
        i += 1
    return new_dict

newdict = my_function(my_list_1, my_list_2)


print(newdict)
        
   

