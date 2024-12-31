def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle the case where no numeric values exist
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage:
my_numbers = [1, 2, 3, 0]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = [1,2,3,'a']
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = ['a','b','c']
result = calculate_average(my_numbers)
print(f"The average is: {result}") 