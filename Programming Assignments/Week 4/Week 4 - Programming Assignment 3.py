"""
Problem Statement:
Write a program that takes a number `n` as input and prints a pyramid of numbers with `n` rows.

Example:
If n = 5, the program should output the following
    1
   232
  34543
 4567654
567898765

If n = 8, the program should output the following
       1
      232
     34543
    4567654
   567898765
  67890109876
 7890123210987
890123454321098
"""

n = int(input())

for i in range(1, n+1):
    # print spaces
    for j in range(1, n-i+1):
        print(" ", end="")
    # print left half of the row
    for j in range(i, 2*i):
        print(j % 10, end="")
    # print right half of the row
    for j in range(2*i-2, i-1, -1):
        print(j % 10, end="")
    # move to the next line
    if (i != n):
        print()
