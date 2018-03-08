"""
TASK
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.


Input Format

The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer ,N the number of other sets.
The next 2*N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.


Output Format

Output the sum of elements in set A.
  
"""


n=input()
elements= set(input().split(' '))
numOperation=int(input())
        


for i in range(numOperation):
    
    operation=input().split(' ')[0]
    if(operation=='update'):
     
        elements.update(set(input().split(' ')))
    
    elif(operation=='intersection_update'):
        elements.intersection_update(set(input().split(' ')))
        
    elif(operation=='difference_update'):
        elements.difference_update(set(input().split(' ')))
        
    elif(operation=='symmetric_difference_update'):

        elements.symmetric_difference_update(set(input().split(' ')))
  
    

print((sum(list(map(int, elements)))))
        
        