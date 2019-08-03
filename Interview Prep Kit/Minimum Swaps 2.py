# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 10:33:52 2019

@author: yashd
"""

def minimumSwaps(arr):
    swaps = 0
    correct = [i+1 for i in range(len(arr))]
    dic = {arr:correct-1 for (arr,correct) in zip(arr,correct)}
    for i in range(len(correct)-1):
        if correct[i] != arr[i]:
            var = dic[correct[i]]
            arr[i],arr[var] = arr[var],arr[i]
            dic[arr[i]], dic[arr[var]] = i, var 
            swaps += 1            
    
    return swaps
    

if __name__ == '__main__':
#    arr = [4,3,1,2]
    arr = [1, 3, 5, 2, 4, 6, 7]
#    arr = [2, 31, 1, 38, 29, 5, 44, 6, 12, 18 ,39, 9, 48, 49, 13, 11, 7, 27, 14, 33, 50, 21, 46, 23, 15, 26, 8, 47, 40, 3, 32, 22, 34, 42, 16, 41, 24, 10, 4, 28, 36, 30, 37, 35, 20, 17, 45, 43, 25,19]
#         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41  42, 43, 44, 45, 46, 47, 48, 49, 50]
#    arr = [8, 45, 35, 84, 79, 12, 74, 92, 81, 82, 61, 32, 36, 1, 65, 44, 89, 40, 28, 20, 97, 90, 22, 87, 48, 26, 56, 18, 49, 71, 23, 34, 59, 54, 14, 16, 19, 76, 83, 95, 31, 30, 69, 7, 9, 60, 66, 25, 52, 5, 37, 27, 63, 80, 24, 42, 3, 50, 6, 11, 64, 10, 96, 47, 38, 57, 2, 88, 100, 4, 78, 85, 21, 29, 75, 94, 43, 77, 33, 86, 98, 68, 73, 72, 13, 91, 70, 41, 17, 15, 67, 93, 62, 39, 53, 51, 55, 58, 99, 46]
    print(len(arr))
    res = minimumSwaps(arr)
    print(res)