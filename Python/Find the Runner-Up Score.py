"""
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.
"""

if __name__ == '__main__':
    n = int(input())
    array =list(map(int,input().split()))
    array=set(array) # Lo convertimos en un conjunto, esto permite eliminar los valores repeditos automaticamente
    array=list(array) #Le devolvemos su forma origianl
    array.sort(reverse=True)

    print(array[1])
    
