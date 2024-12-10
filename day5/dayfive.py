with open('input.txt','r') as file:
    content = file.read()

# Split the content into the two sections (pairs and lists)
rule_data, list_data = content.strip().split("\n\n")

# Parse pairs into a 2D array (list of lists)
rules = [list(map(int, line.split('|'))) for line in rule_data.strip().split('\n')]

# Parse lists into a 2D array (list of lists)
updates = [list(map(int, line.split(','))) for line in list_data.strip().split('\n')]

rule_mapping = {}
rule_rows = len(rules)

for i in range(rule_rows): # Map the rules in a dict, the key is a number and the values have less priority
    key = rules[i][0]
    value = rules[i][1]
    if key not in rule_mapping: 
        rule_mapping[key] = []
    rule_mapping[key].append(value)

total_sum = 0
update_rows = len(updates) 
invalid_updates = []

for i in range(update_rows): # Iterate through the updates
    update_length = len(updates[i])
    current_update = updates[i]
    valid = True
    
    for j in range(update_length - 1): # Iterate through an update
        key = current_update[j] # The current number will be the current key 
        
        for n in range(j + 1, update_length): # The numbers after a current number in an update
            value = current_update[n]
            if value not in rule_mapping[key]: # If a value is not mapped to the current number, a rule is broken and the update is invalid
                valid = False
                break
        
        if not valid:
            break
    
    if valid: 
        middle_index = update_length // 2
        middle_value = current_update[middle_index]
        total_sum += middle_value
    else:
        invalid_updates.append(current_update)


invalid_rows = len(invalid_updates)
sorted_sum = 0

for i in range(invalid_rows):  # Iterate through invalid updates
    current_update = invalid_updates[i]
    update_length = len(current_update)
    j = 0
    while j < update_length - 1: # The current number being checked in the update
        key = current_update[j]
        valid = True
        for n in range(j + 1, update_length): # Iterate through the numbers appearing after the current number we are checking
            value = current_update[n]

            if value not in rule_mapping[key]: # This means the number that isnt mapped for the key should appear earlier in the updates
                current_update[n], current_update[j] = current_update[j], current_update[n] # Swap the numbers
                valid = False
                break # Break of out iteration
        
        if valid:
            j+=1 # The update follows the rules in regards to this number
        else:
            j = 0 # Restart the iteration from the start
        
for update in invalid_updates:
    update_length = len(update)
    middle_index = update_length // 2
    sorted_sum += update[middle_index]

print(f"The sum of the middle values in the valid updates is {total_sum}")
print(f"The sum of the middle values if the previous invalid updates is {sorted_sum}")
        
