"""
Problem Statement:
write a Python program that finds the Greatest Common Divisor (GCD) of two numbers. Your program should take two input numbers from the user, and use a function named 'gcd' to find the GCD of those two numbers. Your program should then print out the GCD of the two numbers as the output.
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a = int(input())
b = int(input())

print(gcd(a, b), end='')
