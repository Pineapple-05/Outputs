random_str = "djnmdhvbnmbndhbfjsbjfdbjhbvdfjvnfndjbndjifdj"

counts = {}

for letter in random_str:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

print(counts)