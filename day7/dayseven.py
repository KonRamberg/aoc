import time

with open('input.txt','r') as file:
    data = file.read()
grid = []
for line in data.strip().split('\n'):
    # Split the line at ": " and then split the rest of the line into integers
    parts = line.split(":")
    row = [int(parts[0])] + list(map(int, parts[1].strip().split()))
    grid.append(row)


def generate_equations(length): # Creates the combination of equations
    length -= 1 # length of combination is one less than amount of numbers in the current equation
    permutations = ['']
    
    for _ in range(length):
        new_permutations = []
        for perm in permutations:
           new_permutations.append(perm + "+")
           new_permutations.append(perm + "*")
           new_permutations.append(perm + "|") # This was added for part two which required concatenation
        permutations = new_permutations
    
    return permutations

total_calibration = 0

for numbers in grid: # One calibration at a time 
    expected_result = numbers[0] 
    equation_inputs = numbers[1:] # Numbers to use in equation
    equation_length = len(equation_inputs) 
    equation_combos = generate_equations(equation_length)
    
    for combo in equation_combos: # Iterate through the different combos
        result = equation_inputs[0]
        for i in range(1, equation_length): # Iterate through the numbers
            if result > expected_result:
                break
            if combo[i - 1] == '+':
                result += equation_inputs[i]
            elif combo[i - 1] == '*':
                result *= equation_inputs[i]
            elif combo[i - 1] == '|':
                result = int(str(result) + str(equation_inputs[i])) # Concatenation support added for part 2 
        if result == expected_result: # Only reached if one of the combinations ended in with an expected result
            total_calibration += result
            break
    
print(f"The equations have a total calibration of {total_calibration}!")

