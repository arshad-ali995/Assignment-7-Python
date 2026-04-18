# TASK 1: List Operations (Intermediate)

# 1. Create a list of 6 numbers
my_list = [10, 25, 4, 38, 17, 42]

# 2. Print the list
print("List:", my_list)

# 3. Find maximum and minimum
print("Maximum number:", max(my_list))
print("Minimum number:", min(my_list))

# 4. Calculate sum
print("Sum of all elements:", sum(my_list))

# 5. Print only even numbers
print("Even numbers:")
for num in my_list:
    if num % 2 == 0:
        print(num)