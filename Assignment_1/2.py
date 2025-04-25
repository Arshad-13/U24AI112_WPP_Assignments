# Write a program that generates 100 random integers that are either 0 or 1. Then find the
# longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
# zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

def count_zeros(arr):
    count = 0
    max_count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    return max_count

arr = [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0]
print(count_zeros(arr))