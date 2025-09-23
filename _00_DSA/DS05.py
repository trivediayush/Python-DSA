# Problem:
# Given two lists of integers:
#   N: a list of numbers in which we want to count occurrences.
#   M: a list of query numbers.
# For each number in M, find how many times it occurs in N.

# Constraints:
# - Numbers in N and M are non-negative integers.
# - For the hashing approach, numbers in M should not exceed the size of the hash table.
# - Brute-force approach is allowed but may be slow for large lists.
# - The lists can contain duplicates.

N = [3,5,6,2,1,4,7,8,3,4,2,11,343,12,453,2,3,2]
M = [1,2,3,4,5,6,7,8,9,10]

print("Brute Force Approach:")
# Brute-force method: For each number in M, count its occurrences in N
for num in M:
    count = 0
    for x in N:
        if x == num:
            count += 1
    print(count)

print("\nHashing Approach:")
# Hashing method: Create a hash table (direct-address table) to store counts

# Step 1: Find maximum value in N to size the hash table
max_val = max(N)

# Step 2: Initialize hash table with zeros
HashList = [0] * (max_val + 1)

# Step 3: Count occurrences of each number in N
for num in N:
    HashList[num] += 1

# Step 4: Lookup counts for numbers in M
for num in M:
    if num < 0 or num > max_val:  # handle out-of-range numbers
        print(0)
    else:
        print(HashList[num])
