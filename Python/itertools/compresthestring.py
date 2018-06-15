"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
 Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string S.

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  S denote integers between  0 and 9.



"""


from itertools import groupby

values = input()

for x,h in groupby(values):
    print( ((len(list(h))),int(x)),end=" ")

