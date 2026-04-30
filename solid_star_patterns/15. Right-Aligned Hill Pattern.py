'''
15.	Right-Aligned Hill Pattern
Input: n = 4
Output:
      *
    * *
  * * *
* * * *
'''
n = 4
for i in range(1,n+1):
    space=""
    for j in range(n-i):
        space+="  "
    star=""
    for k in range(i):
        star+="* "
    print(space+star)
