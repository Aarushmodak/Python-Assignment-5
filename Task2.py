# Task 2: Demonstrate List Slicing 

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_5_elements = l1[0:5]

print(f"Original list: {l1}")

print(f"Extracted first five elements: {first_5_elements}")

first_5_elements.sort(reverse=True)
print(f"Reversed extracted elements: {first_5_elements}")
