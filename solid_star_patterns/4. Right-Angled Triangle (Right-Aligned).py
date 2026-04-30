'''
4.	Right-Angled Triangle (Right-Aligned)
Input: n = 5
Output:
        *
      * *
    * * *
  * * * *
* * * * *
'''
n = 5
for i in range(1, n + 1):
    space = ""
    star = ""
    for j in range(1, n - i + 1):
        space += "  "   
    # stars
    for k in range(1, i + 1):
        star += "* "
    print(space + star)