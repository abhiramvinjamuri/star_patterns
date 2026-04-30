'''
14.	Decreasing Width Triangle
Input: n = 5
Output:
* * * * *
* * * *
* * *
* *
*
'''
n = 5 
for i in range(n,0,-1):
    star=""
    for j in range(i):
        star+="* "
    print(star)
