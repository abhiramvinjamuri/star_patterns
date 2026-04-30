'''
12.	Sandglass Pattern
Input: n = 4
Output:
* * * *
  * * *
    * *
      *
    * *
  * * *
* * * *
'''
n = 4 
for i in range(n,0,-1):
    space=""
    for j in range(n-i):
        space+="  "
    star=""
    for k in range(i):
        star+="* "
    print(space+star)
for i in range(1,n+1):
    space=""
    for j in range(n-i):
        space+="  "
    star=""
    for k in range(i):
        star+="* "
    print(space+star)