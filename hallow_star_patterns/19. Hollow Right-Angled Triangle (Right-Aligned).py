'''
19.	Hollow Right-Angled Triangle (Right-Aligned)
Input: n = 5
Output:
        *
      * *
    *   *
  *     *
* * * * *
'''
n = 6
for i in range(n):
    star=""
    for j in range(n):
        if i==(n-1) or j==(n-1) or i+j==(n-1):
            star+="* "
        else:
            star+="  "
    print(star)
