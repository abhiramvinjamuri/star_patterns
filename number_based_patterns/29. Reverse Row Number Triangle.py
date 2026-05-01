'''29. Reverse Row Number Triangle
Input: n = 5
Output:
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
n = 5 
for i in range(1,n+1):
    num=''
    for j in range(i,0,-1):
        num+=str(j) + " "
    print(num)
        