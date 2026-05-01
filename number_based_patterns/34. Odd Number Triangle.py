'''34. Odd Number Triangle
Input: n = 5
Output:
1
1 3
1 3 5
1 3 5 7
1 3 5 7 9
'''
n = 5
for i in range(1,n+1):
    num=''
    for j in range(1,i*2+1):
        if int(j)%2!=0:
            num+=str(j)+" "
    print(num)

    