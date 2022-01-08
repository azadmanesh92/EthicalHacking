# -*- coding: utf-8 -*-
"""Untitled3.ipynb



Original file is located at
    https://colab.research.google.com/drive/1Am-tl80ZVQnsJ0cLZAPuanyu04kGOHzT

    -Mahsa
"""

number = int(input("input your password (zero to 9999)"))
guess = 0 #default guess
while (guess != number):
  print(guess)
  guess +=1
print("your pass is " + str(number))
