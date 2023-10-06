from cmath import sqrt
import math
import sys
from operator import truediv
arr = [4, 2,59, 55, 45, 7, 1, 9, 3, 8, 63, 3, 3, 5,9,10, 35, 68, 29, 79, 5, 15]
#Xuât tất cả các số lẻ không chia hết cho 5
for i in arr:
    if i % 2 != 0 and i % 5 != 0:
            print(f"Các số lẻ ko chia hết cho 5 là {i}")

# Xuất tất cả các số Fibonacci
def isPerfectSquare(num):
    n = int(math.sqrt(num))
    return (n * n == num)

def checkFib(array, n):
    count = 0
    for i in range(n):
        if (isPerfectSquare(5 * array[i] * array[i] + 4) or
                isPerfectSquare(5 * array[i] * array[i] - 4)):
            print("\nDãy Fibonacci là",array[i], " ", end="")
            count = count + 1
            
    if (count == 0):
        print("None present")

n = len(arr)
checkFib(arr, n)

# Tìm số nguyên tố lớn nhất
def Prime(arr, n):
    max_val = max(arr)
    prime = [True for i in range(max_val + 1)]
    prime[0] = False
    prime[1] = False
    for p in range(2, math.ceil(math.sqrt(max_val))):
        if (prime[p] == True):
            for i in range(2 * p, max_val + 1, p):
                prime[i] = False
    maximum = -10**9
    for i in range(n):
        if (prime[arr[i]] == True):
            maximum = max(maximum, arr[i])
    print("\nSố nguyên tố lớn nhất là : ", maximum)
n = len(arr)
Prime(arr, n)

# Tìm số Fibonacci bé nhất:
