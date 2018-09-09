#!/usr/bin/python
#coding=utf-8


# 斐波拉契算法
# F0 = 0
# F1 = 1
# F(n) = F(n - 1) + F(n - 2)
# input n, what's the value of F(n)

import sys

print(sys.argv)
print(sys.argv[1])
userInputInteger = int(sys.argv[1])
print('userInputInteger', userInputInteger)

# 1.递归算法，算法复杂度 复杂度是O(2^n) 这种递归可以看成是是一棵二叉树，题目相当于是求二叉树中的总结点个数
# https://www.nowcoder.com/questionTerminal/fd57dad14d224881a929d6739741fe50
def fibonacciRecursive(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1

    theVResult = fibonacci(n-1) + fibonacci(n-2)
    n = n - 1

    return theVResult

# 2.利用循环，非递归算法，算法复杂度o(n)
def fibonacciFor(n):
    forResult = 0
    preForResult = 0
    prePreForResult = 0
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    
    for i in range(0, n):
        if (i == 2) :
            prePreForResult = 0
            preForResult = 1
            forResult = 1
            
        prePreForResult = preForResult
        preForResult = forResult
        forResult = preForResult + prePreForResult
        print(forResult)
    
    return forResult

# result = fibonacciRecursive(userInputInteger)
result = fibonacciFor(userInputInteger)



# print ('result', result)