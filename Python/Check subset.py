"""
You are given two sets,  A and B . 
Your job is to find whether set  is a subset of set .

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

The first line will contain the number of test cases, T. 
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.

Output Format

Output True or False for each test case on separate lines.

"""


n=int(input())

for i in range(n):
    input()
    A=set(input().split(" "))
    input()
    B=set(input().split(" "))
    print(A.issubset(B))