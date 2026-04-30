'''
16.	Hollow Square Pattern
Problem: Print a hollow square of stars of size n.
Input: n = 4
Output:
* * * *
*     *
*     *
* * * *
'''
n = 4
for i in range(1,n+1):
    star=""
    for j in range(1,n+1):
        if i==1 or i==n:
            star+="* "
        elif j==1 or j==n:
            star+="* "
        else:
            star+="  "
    print(star)
