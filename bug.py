def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (potential error case):
my_numbers = [1, 2, 3, 0]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = [1,2,3,'a']
result = calculate_average(my_numbers)
print(f"The average is: {result}")