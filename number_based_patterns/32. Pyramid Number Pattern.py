'''32. Pyramid Number Pattern
Input: n = 4
Output:
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1

'''
n = 4
for i in range(1,n+1):
    space=''
    for j in range(1,n-i+1):
        space+="  "
    num_left=''
    for k in range(1,i+1):
        num_left+=" "+str(k)
    num_right=''
    for m in range(1,i):
        num_right+=" "+str(i-m)
    print(space+num_left+num_right)

    