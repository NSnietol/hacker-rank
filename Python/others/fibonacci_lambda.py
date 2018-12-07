"""

A list on a single line containing the cubes of the first N fibonacci numbers.

Reference
https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=30-day-campaign
"""
cube = lambda x:x *x*x # complete the lambda function 

def fibonacci(n):
    # 0 1 1 2 3 5 8 13 21 
    # return a list of fibonacci numbers
    resp = []
    if(n==0):
        return resp
    a = 0
    b = 1
    resp.append(a)
    for i in range(1,n):
        a,b = b , a+b
        resp.append(a)
    return resp

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))