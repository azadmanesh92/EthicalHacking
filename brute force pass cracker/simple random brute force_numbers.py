# -*- coding: utf-8 -*-
"""Untitled3.ipynb



Original file is located at
    https://colab.research.google.com/drive/1Am-tl80ZVQnsJ0cLZAPuanyu04kGOHzT

    -Mahsa
"""

'''  import random
while (True):
   # so that it runs forever
   print(random.randint(0.9999)) #prints a random number in this range '''

import random
number = int(input("input your password (zero to 9999)"))
guess = 0 #default guess
while (guess != number):
  guess = random.randint(0,9999)
  print(guess)
print("your pass is " + str(number))
