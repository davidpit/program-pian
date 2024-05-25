import random

# Create a list with numbers 1 through 20 manually
numbers_list = [   11, 13]

# Check if there are still numbers in the list
if numbers_list:
    # Generate a random index
    index = random.randint(0, len(numbers_list) - 1)
    
    # Get and print the random number
    random_number = numbers_list.pop(index)
    print("Generated:", random_number)
else:
    print("No more numbers to generate.")
