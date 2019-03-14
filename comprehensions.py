#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:29:15 2019

@author: fannieklein
"""
#### LIST COMPREHENSIONS:
#
#list_of_words = ["This","is","A","LIST","oF","wORds"]
#
#new_list = []
#for word in list_of_words:
#    if len(word) > 2: 
#        new_list.append(word)

#def reverse_word(word):
#    return word[::-1]
#
#list_of_words = ["This","is","A","LIST","oF","wORds"]
#new_list = []
#for word in list_of_words:
#    if len(word) > 2:
#        new_list.append(reverse_word(word))

#list_of_words = ["This","is","A","LIST","oF","wORds"]
#new_list = []
#for word in list_of_words: 
#    if word == word.upper():
#        new_list.append(word.upper())

#new_list = [word.upper() for word in list_of_words if word == word.upper()]
#new_list = [reverse_word(word) for word in list_of_words if len(word) > 2]
#new_list = [word.lower() for word in list_of_words]
#new_list = [word.lower() for word in list_of_words if len(word) > 2]
#print(new_list)

### DICT COMPREHENSION:


#messed_up_users = {"testuser1":"Fakepassword",
#                  "mario":"H3reweg0",
#                  "thisisatest":"testpassword",
#                  "testtesttest":"chocolate",
#                  "luigi":"greenislife"}
#
#clean_users = {}
#for user, pwd in messed_up_users.items():
#    if 'test' not in user:
#        clean_users[user] = pwd
#
#clean_users = {user:pwd for user, pwd in messed_up_users.items() if "test" not in user}
#print(clean_users)


#stock = {'shoes':5,
#        'shirts':-2,
#        'bags':-5,
#        'hats':10}
#
#available = {}
#for product, amount in stock.items():
#    if amount < 0:
#        available[product] = amount
#
#available = {product:amount for product, amount in stock.items() if amount < 0}
#print(available)

#stock = {'shoes':5,
#        'shirts':-2,
#        'bags':-5,
#        'hats':10}
#
#commands = {}
#for product, amount in stock.items():
#    if amount > 0:
#        commands[product] = 0
#    else:
#        commands[product] = abs(amount)
#
#def transformation(amount): 
#    if amount > 0: 
#        return 0
#    return abs(amount)
#
#commands = {product:transformation(amount) for product, amount in stock.items()}
#print(commands)

words = ['we', 'are', 'the', 'words', 'of', 'this', 'beautiful', 'list']
new_list = [len(word) for word in words]
new_dict = {word.upper():length for word, length in zip(words, new_list)}
print(new_dict)
