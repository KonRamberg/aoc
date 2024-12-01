file_name ="input.txt"

first_list = []
second_list = []

with open(file_name) as file: 
    for line in file:
        numbers = line.split()
        first_list.append(int(numbers[0])) 
        second_list.append(int(numbers[1]))

first_list.sort() # Lists are sorted in ascending order
second_list.sort()

total_dist = 0
listsize = len(first_list)

for number in range(listsize): 
    current_dist = max(first_list[number], second_list[number]) - min(first_list[number], second_list[number]) # Distance of the two smallest unchecked numbers of both lists
    total_dist += current_dist

similarity_score = 0
num_count = 0

for number in first_list:
    num_count = second_list.count(number) # How many times number from the first list appears in the second list
    similarity_score += (number * num_count) # Similarity score is the sum of prodcuts between numbers in the first list and occurences in second list

print(f"Calculated distance: {total_dist}")       
print(f"Similarity score: {similarity_score}")

