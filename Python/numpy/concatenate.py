"""
You are given two integer arrays of size N X P and M X P ( N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0 .

Input Format

The first line contains space separated integers N , M and P. 
The next N lines contains the space separated elements of the  P columns. 
After that, the next  M lines contains the space separated elements of the P columns.

Output Format

Print the concatenated array of size(N+M)X P.


"""

import numpy as np
data = list(map(int,input().split(' ')))

array1=[]
array2=[]
for i in range(data[0]):
    array1.append(list(map(int,input().split(' '))))
    
for i in range(data[1]):
    array2.append(list(map(int,input().split(' '))))

num_array=np.concatenate((np.array(array1),np.array(array2)),axis=0 )
print(num_array)