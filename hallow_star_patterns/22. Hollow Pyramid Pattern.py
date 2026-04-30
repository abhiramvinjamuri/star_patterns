'''
22.	Hollow Pyramid Pattern
Input: n = 4
Output:
      *
    *   *
  *       *
* * * * * * *
'''
n = 4 
for i in range(1,n+1):
    star=''
    for j in range(1,n+4):
        if i==n or i+j==5 or j-i==3:
            star+="* "
        else:
            star+="  "
    print(star)
