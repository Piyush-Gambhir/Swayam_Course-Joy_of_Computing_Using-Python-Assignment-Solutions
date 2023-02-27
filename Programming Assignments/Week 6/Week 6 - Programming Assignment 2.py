"""
Problem Statement:
Romeo and Juliet love each other. Romeo wants to send a message to Juliet and also don't want anyone to read it without his permission. So, he shifted every lower-case letter in the sentence by -2 position and every upper-case letter by -3 position. (If the letter is c, after shifting to by -2 position it changes to a, and for D new letter will be A).

But the letter is too long, and Romeo does not have enough time to encrypt his whole letter. Write a program to help Romeo that prints the encrypted message. You can assume there are no special characters except spaces and numeric value.

Input:
A string S 

Output: 
Encrypted string 

Example:
Input
Hello Juliet

Output
Ecjjm Gsjgcr

Explanation
H is shifted by -3 position and changed to E. 'e' is shifted by -2 position and changed to c and so on.
"""

S = input()

encrypted_message = ''

for char in S:
    if char.islower():
        if (ord(char)-2 < ord('a')):
            encrypted_message += chr(ord(char)-2+26)
        else:
            encrypted_message += chr(ord(char)-2)
    elif char.isupper():
        if (ord(char)-3 < ord('A')):
            encrypted_message += chr(ord(char)-3+26)
        else:
            encrypted_message += chr(ord(char)-3)
    else:
        encrypted_message += char

print(encrypted_message, end='')
