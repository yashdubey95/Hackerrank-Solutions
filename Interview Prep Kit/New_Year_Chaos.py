# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 13:42:24 2019

@author: yashd
"""

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    places_shifted = {}
    times_shifted = 0
    for index in range(len(q)):
        places_shifted[q[index]] = 0
    for i in range(len(q)):
        swapped = False
        for j in range(len(q)-1):
            if q[j] > q[j+1]:
                places_shifted[q[j]] += 1
                q[j],q[j+1] = q[j+1],q[j]
                swapped = True
            else:
                j += 1

            if places_shifted[q[j-1]] > 2:
                print("Too Chaotic")
                return
            else:
                continue
        if swapped == False:
            break
    times_shifted = sum(places_shifted.values())
    print(times_shifted)
    return
    
    
if __name__ == '__main__':
    #q = [5,1,2,3,7,8,6,4]
    q = [1,2,5,3,7,8,6,4]
    #q = [1,2,5,3,4,7,8,6]
    #q = [2,5,1,3,4]
    print(minimumBribes(q))

