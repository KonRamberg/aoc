with open('input.txt','r') as file:
    content = file.read()

grid = [list(line) for line in content.strip().split('\n')]


num_rows = len(grid)
num_cols = len(grid[0])


for i in range(num_rows): # Finds the guards starting position in the grid
    for j in range(num_cols):
        if grid[i][j] == "^":
            starting_row = i 
            starting_col = j

row = starting_row
col = starting_col

while True: # Breaks out if guard leaves the mapped area
    
    while grid[row][col] != "#" and row > 0: # Move upwards in the grid until either about to leave or hits obstacle
        grid[row][col] = "X"
        row -= 1
    if grid[row][col] != "#" and row == 0: # Guard is leaving the area
        grid[row][col] = "X" # Mark the final position before breaking out
        break
    row += 1 # If the guard hits the obstacle, he takes one step backs before turning 90 degrees to the right

    while grid[row][col] != "#" and col < num_cols - 1: # Move to the right
        grid[row][col] = "X"
        col += 1
    if grid[row][col] != "#" and col == num_cols - 1:
        grid[row][col] = "X"
        break
    col -= 1

    while grid[row][col] != "#" and row < num_rows - 1: # Moves downwards
        grid[row][col] = "X"
        row += 1
    if grid[row][col] != "#" and row == num_rows - 1:
        grid[row][col] = "X"
        break
    row -= 1
   
    while grid[row][col] != "#" and col > 0: # Moves to the left
        grid[row][col] = "X"
        col -= 1
    if grid[row][col] != "#" and col == 0:
        grid[row][col] = "X"
        break
    col += 1

visited_pos = []

for i in range(num_rows): # List of all visited positions
    for j in range(num_cols):
        if grid[i][j] == "X":
            visited_pos.append((i,j)) 

n_visited = len(visited_pos)     
obstruction_pos = 0       


infinity_obstacle = 0 

for i in range(n_visited): # For all visited positions
    row = starting_row
    col = starting_col
    iteration = 0
    current_tuple = visited_pos[i]
    grid[current_tuple[0]][current_tuple[1]] = "#" # Current obstacle test placement

    while True:
        while grid[row][col] != "#" and row > 0: # Move upwards in the grid until either about to leave or hits obstacle
            grid[row][col] = "X"
            row -= 1
        if grid[row][col] != "#" and row == 0: # Guard is leaving the area
            grid[row][col] = "X" # Mark the final position before breaking out
            break
        row += 1 # If the guard hits the obstacle, he takes one step backs before turning 90 degrees to the right

        while grid[row][col] != "#" and col < num_cols - 1: # Move to the right
            grid[row][col] = "X"
            col += 1
        if grid[row][col] != "#" and col == num_cols - 1:
            grid[row][col] = "X"
            break
        col -= 1

        while grid[row][col] != "#" and row < num_rows - 1: # Moves downwards
            grid[row][col] = "X"
            row += 1
        if grid[row][col] != "#" and row == num_rows - 1:
            grid[row][col] = "X"
            break
        row -= 1
        while grid[row][col] != "#" and col > 0: # Moves to the left
            grid[row][col] = "X"
            col -= 1
        if grid[row][col] != "#" and col == 0:
            grid[row][col] = "X"
            break
        col += 1
        
        iteration+=1
        if iteration == 100: # If 100 iterations of up, right, down, left without exitting map consider it to be an infinite loop. (Was initially a larger number)
            infinity_obstacle += 1
            break
    
    grid[current_tuple[0]][current_tuple[1]] = "X" # Removes the tested obstacle
        
print(f"The guard visits {n_visited} positions before leaving the mapped area!")
print(f"There are {infinity_obstacle} placements for an obstacle to make the guard loop infinitely!")