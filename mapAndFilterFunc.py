nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Multiply every element by 2

print(list(map(lambda x: x*2, nums)))

# Print only even numbers

print(list(filter(lambda x: x % 2 == 0, nums)))
