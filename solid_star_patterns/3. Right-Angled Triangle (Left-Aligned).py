'''
3.	Right-Angled Triangle (Left-Aligned)
Problem: Print a left-aligned right-angled triangle.
Input: n = 5
Output:
*
* *
* * *
* * * *
* * * * *
'''
n = 5
for i in range(1,n+1):
    star=''
    for j in range(1,i+1):
        star+='* ' 
    print(star)