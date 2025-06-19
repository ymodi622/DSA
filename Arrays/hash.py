import numpy as np

# Input the number of elements
n = int(input("Enter number of elems: "))
arr = np.zeros(n, dtype=int)  # Ensure array is of integer type

# Populate the array
for i in range(n):
    elem = int(input(f"Enter element {i}: "))
    arr[i] = elem

# Define the size of the hash array
hash_size = 13  # Ensure this matches the range of possible elements
hashArr = np.zeros(hash_size, dtype=int)  # Integer hash array

# Perform hashing
for i in range(n):
    if 0 <= arr[i] < hash_size:  # Validate the range
        hashArr[arr[i]] += 1
    else:
        print(f"Element {arr[i]} is out of hash range (0-{hash_size - 1}).")

# Query the hash array
n2 = int(input("Enter number of queries: "))
for i in range(n2):
    q = int(input("Enter number to find: "))
    if 0 <= q < hash_size:
        print("Result:", hashArr[q])
    else:
        print(f"Query {q} is out of hash range (0-{hash_size - 1}).")
print(hashArr)      