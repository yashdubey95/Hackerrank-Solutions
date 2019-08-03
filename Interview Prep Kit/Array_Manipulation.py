# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:20:34 2019

@author: yashd
"""



# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    a = [0]*n
    for i in queries:
        first = i[0]-1
        last = i[1]
        incr = i[2]
        a[first] += incr
        a[last] -= incr
    max,sum = 0, 0
    for j in a:
      sum += j
      if sum > max:
          max = sum
    return max
    

if __name__ == '__main__':

    n = 10
    queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]  
    result = arrayManipulation(n, queries)

