"""
Problem Statement:
Write a function whole(N) which takes a number N and return the sum of first N whole number. Write the program using recursion.

Input:
N

Output:
sum of whole numbers till N

Example:
Input
3

Output
6

Explanation 
Sum of first 3 natural numbers are 0+1+2+3 = 6
"""

def whole(N):
    if N == 0:  # base case
        return 0
    else:
        return N + whole(N-1)  # recursive case

N = int(input())
print(whole(N), end='')
