'''
26.	Increasing Number Triangle
Problem: Print numbers from 1 to n in triangle form.
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
    num=''
    for j in range(1,i+1):
        num+=str(j)
    print(num)