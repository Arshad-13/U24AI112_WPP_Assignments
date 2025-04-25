# Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of
# numbers. Check the validity of your equivalence classes. [Hint: the union of all equivalence
# classes should be the original set/list.]

def create_equivalence_classes(n):
    # Initialize an empty list to store equivalence classes
    equivalence_classes = {0: [], 1: [], 2: [], 3: [], 4: []}
    
    # Loop through the numbers from 1 to n and classify them based on modulo 5
    for i in range(1, n + 1):
        remainder = i % 5
        equivalence_classes[remainder].append(i)
    
    return equivalence_classes

def check_validity(equivalence_classes, n):
    all_numbers = set(range(1, n + 1))
    union_of_classes = set()

    for remainder in equivalence_classes:
        union_of_classes.update(equivalence_classes[remainder])

    return union_of_classes == all_numbers

# Main function
def main():
    n = 10000 
    equivalence_classes = create_equivalence_classes(n)

    print("Equivalence classes for modulo 5:")
    for remainder in equivalence_classes:
        print(f"[{remainder}] = {equivalence_classes[remainder][:10]}...") 

    if check_validity(equivalence_classes, n):
        print(f"\nThe equivalence classes are valid, and their union covers the entire set from 1 to {n}.")
    else:
        print(f"\nThe equivalence classes are NOT valid.")

if __name__ == "__main__":
    main()