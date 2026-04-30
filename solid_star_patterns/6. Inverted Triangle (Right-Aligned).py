'''
6.	Inverted Triangle (Right-Aligned)
Input: n = 5
Output:
* * * * *
  * * * *
    * * *
      * *
        *
'''
n = 5 
for i in range(n,0,-1):
    space=''
    for j in range(0,n-i,1):
        space+='  '
    star=''
    for k in range(0,i):
        star+='* '
    print(space+star)