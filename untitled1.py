# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15nWT4tN30i8SIO4YXFR2toK6AdOoR45j

This is an ethical password hacking practice.  - Mahsa
"""

flag = 0

import hashlib

pass_hash = input('Enter md5 hash: ') 
wordlist = input("file name: ")

"""Let's open the dictionary of probable passwords:"""

try:
  pass_file = open (wordlist,"r")
except:
  print("No file found")           #trying to open the file that contains that dict
  quit()

"""encode a word from dict into encoded format:"""

for word in pass_file:
  enc_wrd=word.encode("utf-8")
  # hash to hex format:
  digest = hashlib.md5(enc_wrd.strip()).hexdigest() #word to md5 format & strip it from white spaces (strip func) + ...
  # ... hexadecimal format (hexdigest inbuilt lib)

  # Now we want to compare our hash with input hashes
  if digest == pass_hash:
    print("password has been found")
    print("password is " + word)
    flag = 1
    break

"""If the pass is not in the dict: flag == 0

"""

if flag == 0:
  print("pass is not in the list")

"""Well there you go!"""