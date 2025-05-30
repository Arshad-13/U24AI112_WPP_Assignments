# Roy wanted to increase his typing speed for programming contests so, his friend advised him to
# type the sentence “The quick brown for jumps over the lazy dog” repeatedly because it is a
# pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)
# After typing the sentence several times, Roy became bored with is. So he started to look for other
# pangrams.
# Given a sentence s, tell Roy if it is a pangram or not.

# Input Format:
# Input consists of a line containing s.
# Output Format:
# Output a line containing pangram if s is a pangram, otherwise output not pangram
# Sample Input #00
# we promptly judged antique ivory buckles for the next prize
# Sample Output #00
# pangram
# Sample Input #01
# we promptly judged antique ivory buckles for the prize
# Sample Output #01
# not pangram
# Explanation
# In the first test case the answer is pangram because the sentence contains all the letters.

s = input("Enter the sentence: ")
s = s.lower()
s = s.strip()
for i in range(97,123):
    if chr(i) not in s:
        print("not pangram")
        break
    else:
        print("pangram")
        break