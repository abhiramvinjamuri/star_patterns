'''
7.	Centered Pyramid Pattern
Input: n = 4
Output:
      *
    * * *
  * * * * *
* * * * * * *
'''
n = 4
for i in range(1,n+1):
    space=""
    for j in range(0,n-i):
        space+='  '
    star=''
    for k in range(1, 2*i):
        star+='* '
    print(space+star)
