# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function()

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # your code here
    student_list = ['kevin', 'stefan', 'julie']
    first_student = student_list[1]
    last_student = student_list[-1]
    return first_student, last_student
# Call the function and print the result
first_student, last_student = manage_students()
print('Exercise 1: First Student:', first_student, ', Last Student:', last_student)

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    foods = ('onion', 'celery', 'carrot', 'garlic')
    last_two_foods = foods[-2:]
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())
