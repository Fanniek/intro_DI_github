#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 18:56:16 2019

@author: fannieklein
"""
#
# =============================================================================
# class Car():    
#     def __init__(self,
#                  year,
#                  model):   
#         self.year  = year
#         self.model = model
#         
#         self.kilometer       = 0
#         
#     def description(self):  
#         print("This is a {} from {}".format(self.model, self.year))
#         
#     def turn_on(self):  
#         print("VROOM")
# 
# class ElectricCar(Car): 
#     
#     def __init__(self,
#                  year,
#                  model,
#                  voltage):  
#         super().__init__(year,model)
#         self.voltage = voltage
#         
#     def turn_on(self):  
#         print("...")
# 
# 
# my_tesla = ElectricCar(2014, "tesla", 400)
# # my_tesla.description()   ## We have define a description in CAR class :D 
# my_tesla.turn_on()    
# ============================================================================

class Animals():    
   #animal_type = "Dog","Cat","Parrot"
    def __init__(self,
                animal,
                name,
                age,
                food): 
        self.animal = animal
        self.name   = name
        self.age    = age
        self.food   = food
        
    def Family(self):   
        animal_type = input("Enter an animal to find out more information\n>>>")
        if animal_type == "Dog":
            print("The dog belongs to the Canidae family, lets find out more\n")
        else:
            print("Sorry, we dont like other animals besides DOGS, byebye!\n")
        
# =============================================================================
#         def login(self):   
#         password = input("Please enter your password\n>>>")
#         if password == "Bollplan":
#             self.user_logged = True
#             print("Your password is OK, you are now logged in!\n")
#         else:   
#             print("Your password is wrong, you will now get kicked out!\n")
# =============================================================================

class Canidae(Animals):     
    def __init__(self, characteristics, name):    
        self.characteristics = characteristics
        self.name            = name
        
    def description(self):   
        print("This is a {} whose name is {}. {} is {} years old and only eats {}".format(self.animal,
                                                                                         self.name,
                                                                                         self.name,
                                                                                         self.age,
                                                                                         self.food))
    
class Dog(Canidae):  
    
    def __init__(self,
                 animal,
                 name,
                 age,
                 food): 
        
        super().__init__(animal,name)
        self.age =
        
my_dog = Dog("dog", "Fluffy", 12, "Steak")
my_dog.description()
    