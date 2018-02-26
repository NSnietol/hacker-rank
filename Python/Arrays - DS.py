"""
An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, A, of size N ,
each memory location has some unique index, i (where 0<=i<B), that can be referenced as A[i](you may also see it written as Ai).

Given an array, A, of N integers, print each element in reverse order as a single line of space-separated integers.
Input Format

The first line contains an integer,N  (the number of integers in A). 
The second line contains N  space-separated integers describing A.

""" 


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(' '.join(str(e) for e in list(arr[-1::-1])))