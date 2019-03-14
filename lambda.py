#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:20:40 2019

@author: fannieklein
"""

#Exercise 1:
mylist =[" hello"," itsme ","heyy "," i love python "]
mylist = list(map(lambda s: s.strip(), mylist))
#print(mylist)

#Explanattion of Exercise 1:
#This function should use map function --> map applies to every element. First we build:
#map(lambda s: s.strip(), mylist) --> The map applies to every element of the list,
# s --> every string: I want to STRIP every string in my list 
# --> then the argument is that I want this done inside mylist
# returning this will be an object. We need to set the map object to a list, therefor add
# list(map(lambda s: s.strip(), mylist))


#Exercise 2:
people = {"eyal":20, "JOHN":10, "PaBlo":23, "reX":11}
legal_people = {k.lower():v for k, v in people.items() if v > 18}
#print(legal_people)

#Exercise 3:
marks = [("John",46), ("Ethan",22), ("Sean",60)]
marks.sort(key = lambda t: t[1])
#print(marks)

#Cope one list to a new list without a whole yadyada function
my_list   = [3,2,43455,6,23,456546567]
my_list_2 = [x for x in my_list]
#print(my_list_2)

string = "This is a string"
rev_s = " ".join([w[::-1] for w in string.split(" ")])
#print(rev_s)

## joining a list --> need to know every word, to know every word we need split it