# Watson gives two integers A & B to Sherlock and asks if he can count the number of square
# integers between A and B (both inclusive).
# A square integer is an integer which is the square of any integer.
# For example: 1,4,9,16 are some of the square integers as they are squares of 1,2,3,4 respectively.
# Input Format:
# First line contains T, the number of test cases. T test case follow, each in a newline.
# Each test case contains two space separated integers denoting A and B.
# Output Format:
# For each test case, print the required answer in a new line.
# Constraints:
# 1 <= T <=100
# 1 <= A <= B <= 109
# Sample Input
# 2
# 3 9
# 17 24
# Sample Output
# 2
# 0
# Explanation
# In the first test case, 4 and 9 are the square numbers.
# In the second test case no square number exist between 17 and 24(both inclusive).
import math as m

x = int(input("Enter the number of test cases: "))
for i in range(x):
    a = int(input("Enter the start of range: "))
    b = int(input("Enter the end of range: "))   
    for j in range(a,b+1):
        if m.sqrt(j) == int(m.sqrt(j)):
            print(j)
        
