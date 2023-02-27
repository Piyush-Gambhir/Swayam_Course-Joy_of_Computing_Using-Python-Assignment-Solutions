"""
Problem Statement: 
Write a Python program that calculates the dot product of two lists containing the same number of elements. The program should take two lists of integers as input from the user, and then call a function named dot_product to find the dot product of the two lists. The dot_product function should take two lists a and b as input, and should return the dot product of those two lists.

Your program should first prompt the user to enter the two lists of integers, which should be entered as strings separated by spaces. Your program should then convert the input strings into lists of integers. Your program should then call the dot_product function with the two lists as arguments, and store the resulting dot product in a variable named result. Finally, your program should print out the dot product of the two lists as the output.

You can assume that the two input lists will always contain the same number of elements. Your program should output an error message and exit gracefully if the two lists have different lengths.

In your implementation, you should define the dot_product function using a loop to calculate the dot product of the two input list
"""


def dot_product(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


list1 = input().split(" ")
list2 = input().split(" ")

list1 = [int(i) for i in list1]
list2 = [int(i) for i in list2]

if len(list1) != len(list2):
    print("Error: Lists have different lengths")
    exit()

result = dot_product(list1, list2)
print(result, end='')
