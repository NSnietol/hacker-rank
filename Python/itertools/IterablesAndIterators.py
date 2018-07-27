from itertools import combinations
n = int(input())

lista = input().split(' ')

length = int(input())

aux = ""
for i in range(1,n+1):
    aux+=str(i)

print(aux)
print (list(combinations(aux,length)))