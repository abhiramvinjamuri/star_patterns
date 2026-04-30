'''
18.	Hollow Right-Angled Triangle (Left-Aligned)
Input: n = 5
Output:
*
* *
*   *
*     *
* * * * *
'''
n = 5 
for i in range(1,n+1):
    star=""
    for j in range(1,i+1):
        if i==1 or i==n:
            star+="* "
        elif j==1 or j==i:
            star+="* "
        else:
            star+="  "
    print(star)
