"""
Task

You are given a N x M integer array matrix with space separated elements ( N = rows and  M= columns). 
Your task is to print the transpose and flatten results.

Input Format

The first line contains the space separated values of N  and M . 
The next N  lines contains the space separated elements of M columns.

Output Format

First, print the transpose array and then print the flatten.

"""
import numpy as np 


# Se crea una lista con los elementos Row y Columns
RowCol = list(map(int,input().split(' ')))

matriz = []
#Se agrega los elementos de cada linea para construir la matriz
for i in range( RowCol[0]):
    matriz.append(input().split(' '))

#Se crea un objeto de tipo numpy_array para poder usar los mètodos transpose y flatten
matriz = np.array(matriz).astype(np.int)
print(np.transpose(matriz))

print(matriz.flatten())
        