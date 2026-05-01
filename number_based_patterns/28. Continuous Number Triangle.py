'''28.	Continuous Number Triangle
Input: n = 4
Output:
1
2 3
4 5 6
7 8 9 10
'''
n = 4
num = 1
for i in range(1,n+1):
    row = ""
    for j in range(1,i+1):
        row += str(num) 
        num += 1
    print(row)