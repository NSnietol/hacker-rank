"""
itertools.product()

This tool computes the cartesian product of input iterables. 
It is equivalent to nested for-loops. 
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).



Task

You are given a two lists A and B. Your task is to compute their cartesian product A X B.

Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format

The first line contains the space separated elements of list A. 
The second line contains the space separated elements of list B.

Both lists have no duplicate integer elements.

Constraints

 0<A<30
 0<b<30

Output Format

Output the space separated tuples of the cartesian product.
"""

from itertools import product

a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
print( *list(product(a,b)))