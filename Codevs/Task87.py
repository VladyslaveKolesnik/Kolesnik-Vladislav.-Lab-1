# Reading two integers
a = int(input())
# Reading the second integer
b = int(input())

# Checking divisibility and printing the result
print(("no", "yes")[(a % b) == 0]) 