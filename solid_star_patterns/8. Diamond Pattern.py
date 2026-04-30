'''
8.	Diamond Pattern
Input: n = 3
Output:
    *
  * * *
* * * * *
  * * *
    *
'''
n = 3 
for i in range(1,n+1):
    space=""
    for j in range(0,n-i):
        space+="  "
    star=""
    for k in range(1,2*i):
        star+="* "
    print(space+star)
for i in range(n-1,0,-1):
    space=""
    for j in range(0,n-i):
        space+="  "
    star=""
    for k in range(0,2*i-1):
        star+="* "
    print(space+star)
