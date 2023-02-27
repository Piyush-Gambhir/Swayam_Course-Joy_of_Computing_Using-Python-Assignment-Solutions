"""
Problem Statement: 
Write a program that takes a number `n` as input and prints the sum of the squares of the first `n` positive integers.

Example:
If n = 4, the program should output 30 (1^2 + 2^2 + 3^2 + 4^2 = 30)
"""

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i**2
print(sum, end="")
