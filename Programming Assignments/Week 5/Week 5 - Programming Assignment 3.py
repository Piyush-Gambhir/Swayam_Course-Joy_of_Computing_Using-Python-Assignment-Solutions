"""
Problem Statement:
Write a Python function that takes a string s as input and returns the length of the largest streak of 0s in the string. For example, if the input string is "10001000110000000001", the function should return 6.

Input 
The input string s is guaranteed to contain only 0s and 1s.

Output
The function should return an integer, representing the length of the largest streak of 0s in the input string.
Your program should also print the result.

Sample output
largest_zero_streak("10101010") => 1
largest_zero_streak("10000010001") => 5
largest_zero_streak("1111") => 0
largest_zero_streak("0000") => 4
largest_zero_streak("00000000001111111111") => 10
"""


def largest_zero_streak(s):
    max_streak = 0
    current_streak = 0
    for char in s:
        if char == '0':
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
    return max_streak


input_string = input()
print(largest_zero_streak(input_string), end='')
