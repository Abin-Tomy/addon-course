student_a_hobbies = {'reading', 'gaming', 'painting', 'cooking', 'hiking'}
student_b_hobbies = {'gaming', 'swimming', 'cooking', 'photography', 'cycling'}

# Find common hobbies (intersection)
common_hobbies = student_a_hobbies.intersection(student_b_hobbies)
print("\nHobbies common to both students:")
print(common_hobbies)

# Find hobbies unique to Student A (difference)
unique_to_a = student_a_hobbies.difference(student_b_hobbies)
print("\nHobbies unique to Student A:")
print(unique_to_a)

# Find all hobbies (union)
all_hobbies = student_a_hobbies.union(student_b_hobbies)
print("\nAll hobbies from both students:")
print(all_hobbies)
