#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:53:54 2019

@author: fannieklein
"""

def get_store(stores, city):
   for store in stores:
       if store['city'].lower() == city.lower():
           return store

def display_colors(shoe):
   print("This shoe is available in the following colors:")
   for color in shoe['color_available']:
       print('-',color)

def choose_store():
   stores = json['stores']
   print("Available stores:")
   for store in stores:
       print(store['city'])

   store = input("Choose a store\n>>> ")
   return store.lower()

def choose_brand():
   print("Here are the available brands:")
   products = json['products']
   for product in products:
       print(product['brand'])

   brand = input("Choose a brand\n>>>")
   for product in products:
       if product['brand'] == brand:
           return product['id']

def check_for_availability(item_id, wanted_store):
   stores   = json['stores']
   my_store = get_store(stores, wanted_store)
   shoes_available = my_store['shoes_available']

   for shoe in shoes_available:
       if shoe['id'] == item_id:
           if shoe['num available'] > 0:
               display_colors(shoe)
           else:
               print("This shoe isnt available")



item_id = choose_brand()
store = choose_store()
check_for_availability(item_id, store)