# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 00:19:34 2019

@author: yashd
.
"""

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    res = []
    j = 0
    for i in range(4):
        for j in range(4):
            sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            res.append(sum)
    return max(res)
        
            
if __name__ == '__main__':
    
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    result = hourglassSum(arr)

    
