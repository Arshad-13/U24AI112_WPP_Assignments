# Given a word w, rearrange the letters of w to construct another word s in such a way that s is
# lexicographically greater than w.
# Input Format:
# The first line of inputs contains t, number of test cases. Each of the next t lines contains w.
# Constraints:
# 1 <= t <= 105
# 1 <= |w| <= 100
# w will contain only lower-case English letters and its length will not exceed 100.
# Output Format:
# For each test case, output a string lexicographically bigger than w in a separate line. In case of
# multiple possible answers print the lexicographically smallest one and if no answer exists, print
# no answer.
# Sample Input:
# 3
# ab
# bb
# hefg
# Sample Output:
# ba
# no answer
# hegf

x = int(input())
for i in range(x):
    w = input()
    w = list(w)
    n = len(w)
    i = n - 1
    while i > 0 and w[i-1] >= w[i]:
        i -= 1
    if i <= 0:
        print('no answer')
        continue
    j = n - 1
    while w[j] <= w[i-1]:
        j -= 1
    w[i-1], w[j] = w[j], w[i-1]
    w[i:] = reversed(w[i:])
    print(''.join(w))