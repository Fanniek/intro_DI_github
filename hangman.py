#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:19:12 2019

@author: fannieklein
"""
import random
import requests

def clean_word(word): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in word: 
        if letter.lower() not in alphabet: 
            return False
    return True
    
req = requests.get(r"https://raw.githubusercontent.com/dwyl/english-words/master/words.txt")

myfile  = "words-list.txt"
content = req.text

wordslist     = content.split("\n")
clean_words   = [word.upper() for word in wordslist if clean_word(word)]
clean_content = "\n".join(clean_words)

with open(myfile, "w") as f: 
    f.write(clean_content)

print("Finished!")

class HangmanGame(): 
    
    def __init__(self,
                 words_file): 
        self.words_file = words_file
        self.life       = 8
        
    def pick_word(self,
                  file): 
        
        words         = open(file, "r").readlines()
        random_line_n = random.randint(1, len(words)-1)
        myword        = words[random_line_n]
        
        return myword
    
    def play(self): 
        self.secret_word = self.pick_word(self.words_file)
        self.public_word = ['*' for letter in self.secret_word]
        while True: 
            self.player_turn()
            if self.check_for_end(): 
                break
            
        
    def player_turn(self): 
        print(" ".join(self.public_word))
        user_letter = input("Choose a letter: ")
        if self.check_letter(user_letter): 
            self.found_letter(user_letter)
            print("Yeah, {} is in the word !".format(user_letter))
        else: 
            self.life -= 1
            print("Oh no, {} is not in the word ({} lifes left)".format(user_letter, self.life))
        
    def check_letter(self,
                     letter): 
        if letter.upper() in self.secret_word: 
            return True
        return False
    
    def found_letter(self,
                     letter_found): 
        letter_found = letter_found.upper()
        for ix, letter in enumerate(self.secret_word): 
            if letter == letter_found: 
                self.public_word[ix] = letter
                
    def check_for_end(self): 
        # loose
        if self.life < 0: 
            print("Sorry, you loose.. The word was {}".format(self.secret_word))
            return True       
        # win
        if '*' not in self.public_word:
            print("Congrats! You won with {} lifes!".format(self.life))
            return True
        
        return False
    
    def play_again(self): 
        again = input("Do you want to play again ;[Y/N]\n>>> ")
        if again.lower() == "y":
            self.play()
        else:
            print("Good Bye!")
            
            
hangman = HangmanGame('words-list.txt')
hangman.play()