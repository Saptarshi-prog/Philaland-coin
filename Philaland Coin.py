# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:47:09 2020

@author: saptarshi
"""

import math
arr = []

T= int(input())
for i in range(T):
    n=int(input())
    q= 1 + math.floor(math.log(n,2))
    arr.append(q)
    
for i in range(T):
    print(arr[i])