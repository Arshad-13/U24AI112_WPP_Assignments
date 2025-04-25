# Create the following lists using a for loop.
# (a) A list consisting of the integers 0 through 49
# (b) A list containing the squares of the integers 1 through 50.
# (c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.

list1 = [x for x in range(50)]
list2 = [x*x for x in range(50)]
list3 = [(chr(64 + x)) *x for x in range(1,27)]
print(f"{list1}\n{list2}\n{list3}")