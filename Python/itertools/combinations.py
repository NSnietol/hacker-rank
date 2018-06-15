"""
https://www.hackerrank.com/challenges/itertools-combinations/problem
Task

You are given a string S. 
Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value K separated by a space.

Constraints

0<k<len(s)
 
The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.
"""
from itertools import combinations

values,n=input().split(' ')

for i in range(1,int(n)+1):
    for x in list(combinations(sorted(values),i)):
        print("".join(x))