# Problem:
# Given two lists of Character:
#   S: a list of character in which we want to count occurrences.
#   Q: a list of query characters.
# For each number in M, find how many times it occurs in N.

S = "azyzyyzaaaag"
Q = ["d","a","y","x"]

hashList = [0] * 26


for ch in S:
    index = ord(ch) - ord('a')
    hashList[index] += 1

for ch in Q:
    index = ord(ch) - ord('a')
    print(hashList[index])