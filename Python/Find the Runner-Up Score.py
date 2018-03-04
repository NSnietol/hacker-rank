"""

Python 3.x
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.


Input Format

The first line contains n. The second line contains an array []  of n  integers each separated by a space.

URL=https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

"""

if __name__ == '__main__':
    n = int(input())
    array =list(map(int,input().split()))
    array=set(array) # Lo convertimos en un conjunto, esto permite eliminar los valores repeditos automaticamente
    array=list(array) #Le devolvemos su forma origianl
    array.sort(reverse=True)

    print(array[1])
    
