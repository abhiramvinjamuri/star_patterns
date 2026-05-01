'''
11.	Right-Aligned Half Diamond
Input: n = 4
Output:
      *
    * *
  * * *
* * * *
  * * *
    * *
      *
'''
n = 4
for i in range(1,n+1):
    space=''
    for j in range(1,n-i+1):
        space+='  '
    star=''
    for k in range(1,i+1):
        star+="* "
    print(space+star)
for i in range(1,n):
    space=''
    for j in range(1,i+1):
        space+="  "
    star=''
    for k in range(1,n-i+1):
        star+="* "
    print(space+star)
        
        
    


    
    