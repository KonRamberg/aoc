file_name = "input.txt"

with open(file_name) as file:
    corrupted_data =  file.read()

string_index = 0
start = 0
multiplications = 0

while True: # Find mul(int,int), multiply integers add to sum
    mul_index = corrupted_data.find("mul(",start) # Find newest "mul()" 
    
    if mul_index == -1: # No more multiplication 
        break
    
    comma_index = corrupted_data.find(",", mul_index) # Finds index of next ","
    parenthesis_index = corrupted_data.find(")", comma_index) #Finds index of next "parenthesis"
    
    if (corrupted_data[mul_index+4:comma_index].isdigit() and corrupted_data[comma_index+1:parenthesis_index].isdigit()): # Check if integers between parenthesis of "mul(,)"
        firstnumber = int(corrupted_data[mul_index+4:comma_index])
        secondnumber = int(corrupted_data[comma_index+1:parenthesis_index])
        multiplications += firstnumber * secondnumber
    start = mul_index + 1

string_index = 0
start = 0
do_multiplications = 0
do = True

while True: # Identical to above but with do flag
    mul_index = corrupted_data.find("mul(", start)
    if mul_index == -1:
        break
    do_index = corrupted_data.rfind("do()", start, mul_index) # Finds last "do()" appearance in the range
    do_not_index = corrupted_data.rfind("don't()", start, mul_index) # Finds last "don't()" appearance in the range
    
    if do_not_index > do_index: # Do not index higher than do index, 
        do = False
    elif do_not_index < do_index:
        do = True

    if not do: # Skip to next iteration
        start = mul_index + 4
        continue
    
    comma_index = corrupted_data.find(",", mul_index)
    parenthesis_index = corrupted_data.find(")", comma_index)
    if (corrupted_data[mul_index+4:comma_index].isdigit() and corrupted_data[comma_index+1:parenthesis_index].isdigit() and do): # Checks do flag too
        firstnumber = int(corrupted_data[mul_index+4:comma_index])
        secondnumber = int(corrupted_data[comma_index+1:parenthesis_index])
        do_multiplications += firstnumber * secondnumber
    start = mul_index + 1

print(f"All multiplications: {multiplications}")
print(f"All multiplications with do: {do_multiplications}")

