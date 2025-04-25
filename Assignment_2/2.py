# Write a program that repeatedly asks the user to enter product names and prices. Store all
# of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a
# product name and print the corresponding price or a message if the product is not in the
# dictionary.

x = input("Enter a product name: ")
y = input("Enter the price: ")
d = {x: y}
while True:
    x = input("Enter a product name: ")
    if x == "":
        break
    y = input("Enter the price: ")
    d[x] = y
while True:
    x = input("Enter a product name to view its price: ")
    if x == "":
        break
    if x in d:
        print(d[x])
    else:
        print("Product not found")