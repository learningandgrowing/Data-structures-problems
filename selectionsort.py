#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 04:32:36 2019

@author: satyam
"""

def selectionsort(arr):
    l = len(arr)
    for i in range(l - 1):
        minindex = i
        for j in range(i+1,l):
            if arr[j] < arr[minindex]:
                minindex = j
                
        arr[i],arr[minindex] = arr[minindex],arr[i]
arr = list(int(x) for x in input().strip().split())
selectionsort(arr)
print(arr)