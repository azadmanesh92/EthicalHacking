# -*- coding: utf-8 -*-
"""Untitled3.ipynb


Original file is located at
    https://colab.research.google.com/drive/1Am-tl80ZVQnsJ0cLZAPuanyu04kGOHzT

    - Mahsa
"""

import random
#character = "0123456789qazwsxedcrfvtgbyhnujmik,ol.p;/[']=-`~!@#$%^&*()_+|}{POIUYTREWQASDFGHJKL:?><MNBVCXZ"
character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list (character) #This will break all the char.s in the string up.
password = input("input your password: ")
guess = ""  #default: empty string
while (guess!= password):
  guess = random.choices(character_list,k=len(password))
  print(guess)
  guess="".join(guess )
  print(guess)
print("Your password is " + guess)
