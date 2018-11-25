from itertools import combinations
n=int(input())
#values = input().split(" ")
values = "a z e i o a f g h k".split(" ")

values = "".join(values)
print(values)
k = 5
#int( input())
#

aux = ["a","b","c","d","e","f","g","h","i","j", "k","m","n","o","p","q","r","s","t","u","v","w","y","z"]

print("Size values :", len(values))
print("Size vocabulario: ", len(aux))
print("Size Combinacion : ", len(list(combinations(values,k))))

print("Auxiliar ", aux[:k])
cont=0
for i in list(combinations(values,k)):
    for j in aux[:k]:
        print(i)
        if j in i:
             cont+=1
             break
print(cont/len(list(combinations(values,k))))
