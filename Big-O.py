# O(1) Complexity
def multiply_numbers(n):
    return n * n
print(multiply_numbers(100)) 

# O(n) Complexity
def print_items(n):
    for i in range(n):
        print(i)   
print_items(10)

# O(2n) Complexity it is also O(n) complexity
def print_items(n):
    for i in range(n):
        print(i)
    for i in range(n):
        print(i)
print_items(10)

# O(n^2) Complexity
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
print_items(10)

# non dominant terms
def print_items(n):
    for i in range(n):                     # it is O(n^2) complexity
        for j in range(n):
            print(i, j)
    for k in range(n):                     # it is O(n) complexity
        print(k)    
print_items(10)

# Space Complexity
def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)
sum(3) # O(n) space complexity



def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total += pair_sum(i, i+1)
    return total
def pair_sum(a, b):
    return a + b
pair_sum_sequence(3) # O(1) space complexity