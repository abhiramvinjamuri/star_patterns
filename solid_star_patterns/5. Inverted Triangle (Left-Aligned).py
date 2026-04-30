'''
5.	Inverted Triangle (Left-Aligned)
Input: n = 5
Output:
* * * * *
* * * *
* * *
* *
*
'''
n = 5 
for i in range(n+1,0,-1):
    star=""
    for j in range(i):
        star+="* "
    print(star)
