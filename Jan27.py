#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:32:37 2019

@author: fannieklein
"""
#Class exercise 27th Jan : "class"

# =============================================================================
# class Dog():   ##is all the dogs 
#     animal_type = "Dog" ##this belongs in the class
#     dog_number  = 0
#     ## __init__ can ony be created once
#     ##innit is a function that "calls" itself. You do not use like in sit function
#     def __init__(self, name, age): ##do this function on this object (self --> dog everytime im creating a function inside a class - I need to give argument to be SELF
#         Dog.dog_number += 1
#         self.dog_name = name
#         self.dog_age  = age
#         print("New dog joined with the name: {}".format(name))
#         print("and he is {} years old".format(age))
# 
#     def sit(self):  
#         print("{} is sitting".format(self.dog_name))
#         
#     def presentation(self): 
#         print("Voff, My name is {}, and I am {} years old. I know how to sit".format(self.dog_name, self.dog_age))
# 
#     def new_year(self): ## this adds everytime +1 when asking for the function 
#         self.dog_age += 1
#         
#     def howmanydogs(self):  
#         return Dog.dog_number
#      
# my_dog = Dog("Rex", 10) ##Object
# neighbor_dog = Dog("Fluffy", 15)  ## new object inside DOGS folder
# 
# my_dog.sit()
# 
# my_dog.presentation()
# my_dog.new_year()
# my_dog.presentation()
# 
# print(my_dog.animal_type)
# 
# print(my_dog.howmanydogs())
# =============================================================================
# =============================================================================
# print(my_dog.dog_age)  ## print just the age if I want that.
# =============================================================================
import datetime

# module: print(datetime.date.today())

class Tweet(): 
    
    
    def __init__(self,
                 content,
                 author,
                 date=str(datetime.date.today())): 
        self.tweet_content = content
        self.tweet_author  = author
        self.tweet_date    = date
        
    def __str__(self):  
        return self.tweet_content
# =============================================================================
# 
# =============================================================================

class User(): 
    
    
    def __init__(self,
                 name,
                 pwd,
                 email,
                 admin=False,
                 logged_in=False):  
        
        print("New user joined!")
        self.user_name   = name
        self.user_pwd    = pwd
        self.user_email  = email
        self.user_admin  = admin
        self.user_logged = logged_in
        
        
        self.user_tweet  = []
    
    def login(self):   
        password = input("Please enter your password\n>>>")
        if password == "Bollplan":
            self.user_logged = True
            print("Your password is OK, you are now logged in!\n")
        else:   
            print("Your password is wrong, you will now get kicked out!\n")
            
    def logout(self):   
        self.user_logged =  False
        print("Logged out!")
        
# =============================================================================
#     def add_tweet(self, tweet): 
#         today = str(datetime.date.today())
#         self.user_tweet.append(tweet)
#         print("{} ({})".format(today, tweet))
# =============================================================================
        
    def add_tweet(self,tweet): 
        my_tweet = Tweet(tweet, self.user_name)
        self.user_tweet.append(my_tweet)
        
        
        #### THIS IS IMPORTANT --> LEARN IT
    def read_tweets(self):   
        for element in self.user_tweet: 
            print(">>>",element,"<<<",
                  "Written at: ",element.tweet_date, 
                  "By: ",element.tweet_author)
        

my_user = User("Fannie", "Bollplan", "klein.fannie@gmail.com", admin=True) ##Object
my_user.login()

my_user.add_tweet("My first Tweet!!")
my_user.add_tweet("This is my 2nd tweet!!")

my_user.read_tweets()

# =============================================================================
# my_user.user_tweet[0]
# =============================================================================
# =============================================================================

# =============================================================================
