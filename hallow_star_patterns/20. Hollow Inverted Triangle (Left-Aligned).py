'''
20.	Hollow Inverted Triangle (Left-Aligned)
Input: n = 5
Output:
* * * * *
*     *
*   *
* *
*
'''
n = 5 
for i in range(n):
    star=""
    for j in range(n):
        if j==0 or i==0 or i+j==n-1:
            star+="* "
        else:
            star+="  "
    print(star)
