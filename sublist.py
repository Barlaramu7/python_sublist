nested = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]

# Assume first element as both largest and smallest
largest = nested[0][0]
smallest = nested[0][0]

# Loop through each element in the nested list
for i in nested:
    for j in i:
        if j > largest:
            largest = j
        if j < smallest:
            smallest = j

print("Largest number:", largest)
print("Smallest number:", smallest)
