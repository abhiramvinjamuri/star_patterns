'''
10.	Left-Aligned Half Diamond
Input: n = 4
Output:
*
* *
* * *
* * * *
* * *
* *
*
'''
n = 4 
for i in range(1,n+1):
    star=""
    for j in range(1,i+1):
        star+="* "
    print(star)
for i in range(n-1,0,-1):
    star=""
    for j in range(0,i):
        star+="* "
    print(star)
