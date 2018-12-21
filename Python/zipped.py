"""
zip([iterable, ...])

This function returns a list of i tuples. The th tuple contains the th element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.


Task

The National University conducts an examination of  N students in X subjects. 
Your task is to compute the average scores of each student.


Input format
The first line contains N  and X separated by a space. 
The next X lines contains the space separated marks obtained by students in a particular subject.

Output Format

Print the averages of all students on separate lines.
The averages must be correct up to  decimal place.

References : https://www.hackerrank.com/challenges/zipped/problem

"""


length, num = map(int,input().split(" "))

lista = []
for i in range(num):
    lista.append(list(map(float,input().split(" "))))

for i in list(zip(*lista)):
    print(sum(i)/num)

