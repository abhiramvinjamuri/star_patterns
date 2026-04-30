'''
21.	Hollow Inverted Triangle (Right-Aligned)
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
        if i==0 or j==n-1 or i==j:
            star+="* "
        else:
            star+="  "
    print(star)
