'''33. Even Number Triangle
Input: n = 5
Output:
2
2 4
2 4 6
2 4 6 8
2 4 6 8 10
'''
n = 5
for i in range(1,n+1):
    num=''
    for j in range(1,i*2+1):
        if int(j)%2==0:
            num+=str(j)+" "
    print(num)

    