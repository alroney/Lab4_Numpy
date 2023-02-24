# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 09:39:36 2022

@author: Andrew
Description: This is a script that would turn an string input into hash values.
"""

import hashlib
import os

#input a message to encode
while True:
    print('Enter a message to encode:')
    message = input()
    
    # encode it to bytes using UTF-8 encoding
    message = message.encode()
    
    # hash with MD5 (very weak)
    print("MD5:",hashlib.md5(message).hexdigest())
    
    # Lets try a stronger SHA-2 family
    print("SHA-256:",hashlib.sha256(message).hexdigest())
    print("SHA-512:",hashlib.sha512(message).hexdigest())
    
    
    #For copying
    print("\n\n")
    print(hashlib.md5(message).hexdigest())
    print(hashlib.sha256(message).hexdigest())
    print(hashlib.sha512(message).hexdigest())
    print("\n\n")
    
    input("\n\nENTER to continue")
    os.system('cls')


