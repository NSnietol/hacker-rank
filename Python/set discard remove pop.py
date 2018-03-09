"""
Task
You have a non-empty set s, and you have to execute  N commands given in N lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer n, the number of elements in the set s . 
The second line contains  n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9. 
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.


Output Format

Print the sum of the elements of set  on a single line.

"""

n = int(input())

s = set(map(int, input().split())) 
for i in range(int(input())):
    operation=input().split(' ')
    
    if(operation[0]=='pop'):
        try:
            s.pop()
        except KeyError:
            pass
        
    elif(operation[0]=='discard'):
        s.discard(int(operation[1]))
        
    elif(operation[0]=='remove'):
        try:
            s.remove(int(operation[1]))
        except KeyError:
            pass

print(sum(map(int,list(s))))