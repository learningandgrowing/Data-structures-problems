#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 23:14:15 2019

@author: satyam
"""
def checkAB(s, i, last):
    if i == len(s):
          return True
    if i == 0 and s[i] == 'a':
        return checkAB(s,i+1,'a')
    if i < len(s) - 1 and s[i]=='b' and s[i+1]=='b' and last=='a':
        return checkAB(s,i+2,'b')
    if last=='b'and s[i]=='a':
        return checkAB(s,i+1,'a')
    if last=='a'and s[i]=='a':
        return checkAB(s,i+1,'a')
    return False
        
        

    
       
    
s = input()
print(checkAB(s, 0, 'a'))

    
    