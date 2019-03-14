#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:30:37 2019

@author: fannieklein
"""
import json

class MenuManager(): 

        
    def __init__(self):          
        with open("menu.json", "r") as f: 
            self.menu = json.load(f) 
            
            
    def add_item(self,name,price,spice,gluten): 
        new_item = {"name":name,
                  "price":price,
                  "spice_level":spice,
                  "gluten_index":gluten}
        self.menu["items"].append(new_item)
#        print(self.menu)
    
    
    def remove_item(self,name): 
        for dish in self.menu["items"]:
            if dish["name"] == name:
                self.menu["items"].remove(dish)
                print("You have now removed {} from the menue".format(name))
                print(self.menu)
                return True
        else:
            print("The dish you entered doesnt exist in the menue")
            return False
               
    
    def save_to_file(self): 
        with open("menu.json", "w") as f: 
            json.dump(self.menu, f, indent = 4)
            
#    def update_item_from_menu(self,name)
        
        

my_menu = MenuManager()
#my_menu.remove_item("Soup")
#print(my_menu.menu)