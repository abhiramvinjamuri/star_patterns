'''
17.	Hollow Rectangle Pattern
Problem: Print a hollow rectangle of m rows and n columns.
Input: m = 4, n = 5
Output:
* * * * *
*       *
*       *
* * * * *
'''
n = 4 
m = 5 
for i in range(1,n+1):
    star=""
    for j in range(1,m+1):
        if i==1 or i==n:
            star+="* "
        elif j==1 or j==m:
            star+="* "
        else:
            star+="  "
    print(star)
