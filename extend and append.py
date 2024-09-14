list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using append to add list2 to list1
list1.append(list2)
print(list1)  # Output: [1, 2, 3, [4, 5, 6]]

# Using extend to add list2 to list1
list1 = [1, 2, 3]  # Reset list1
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]