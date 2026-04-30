'''
1.Solid Square Pattern
Problem: Print a solid square of stars of size n.
Input: n = 4
Output:
* * * *
* * * *
* * * *
* * * *
'''
n = 4 
for i in range(1,n+1):
    star=''
    for k in range(1,n+1):
        star+='* '
    print(star)