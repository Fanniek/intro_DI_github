#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:21:33 2019

@author: fannieklein
"""
import re
import json

def read_word_list(): 
    with open("engmix.txt", "r") as f: 
        words = f.readlines()
        lines = map(str.strip, words)
#        words = words.strip()
        return lines
    
#words = ["hey hello haaay","hallo","came","bye","hey","shalom"]
   
def search(text): 
    new_words = []
    for word in read_word_list(): 
        text1 = re.findall(text,word)
        if len(text1) != 0: 
            new_words.append(word)
    return new_words  

def save_search(text,results): 
    last_search = {"search_text":text,
                   "results":results}
    with open("last_search.json", "w") as f:
        json.dump(last_search, f, indent = 4)
        
def display_menu(): 
    choice_user = input("Please enter:\n (a) If you want to make a new search\n (b) If you want to see previous search\n (c) If you want to exit\n>>> ")    
    if choice_user   == "a": 
        search_word = input("Enter a word\n>>> ")
        if re.match("^[a-zA-Z]*$", search_word): 
            save_search(search_word, search(search_word)) 
        else: 
            print("You can only use letters, no numbers or special characters. Try Again!")  
#            search_word = input("Enter a word\n>>> ")                    
    elif choice_user == "b": 
        save_search()
    elif choice_user == "c":
        return choice_user
        
    
#def show_results(): 
            
      

    
#print(read_word_list())
#search("hello")
#save_search("ame", search("ame"))
display_menu()





            
