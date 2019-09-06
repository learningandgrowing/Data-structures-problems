.#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:58:55 2019

@author: satyam
"""
def replacePi(s):
    if len(s)==0:
        return s
    
    str = replacePi(s[1:])
    if s[0] == 'p' and s[1] == 'i':
        return '3.14' + str[2:]
    else:
        return s[0] + str
print(replacePi(input()))
