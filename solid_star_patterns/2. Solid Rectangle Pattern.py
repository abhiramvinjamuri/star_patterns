'''
2.	Solid Rectangle Pattern
Problem: Print a solid rectangle of m rows and n columns.
Input: m = 3, n = 5
Output:
* * * * *
* * * * *
* * * * *
'''

m = 3
n = 5
for i in range(1,m+1): 
    star=''
    for j in range(1,n+1):
        star+='* '
    print(star)
