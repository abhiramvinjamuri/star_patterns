'''31. Right-Aligned Number Triangle
Input: n = 5
Output:
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
'''
n = 5
for i in range(1,n+1):
    space=''
    for j in range(1,n-i+1):
        space+="  "
    num=''
    for k in range(1,i+1):
        num+= " "+str(k)
    print(space+num)
    