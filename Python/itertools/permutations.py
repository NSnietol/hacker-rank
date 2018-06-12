"""
https://www.hackerrank.com/challenges/itertools-permutations/problem

Task

You are given a string S. 
Your task is to print all possible permutations of size  K of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string  S and the integer value K .

Constraints

 
The string contains only UPPERCASE characters.

Output Format

Print the permutations of the string S on separate lines.
"""

from itertools import permutations

values = input().split(' ')
result = list(permutations(list(values[0]), int(values[1])))
result.sort()
for i in  result:
    print("".join(i))