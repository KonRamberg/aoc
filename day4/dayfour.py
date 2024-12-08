with open('input.txt','r') as file:
    xmas_array = [line.strip() for line in file]


num_rows = len(xmas_array)
num_cols = len(xmas_array[0])
xmas_count = 0

for i in range(num_rows):
    row = xmas_array[i]
    xmas_count += row.count("XMAS")
    xmas_count += row[::-1].count("XMAS")

for j in range(num_cols):
    vertical_string =""
    for i in range(num_rows):
        vertical_string += xmas_array[i][j]
    xmas_count += vertical_string.count("XMAS")
    xmas_count += vertical_string[::-1].count("XMAS")

for i in range(num_rows-3):
    for j in range(num_cols):
        if j <= num_cols-4:
            if xmas_array[i][j] == "X" and xmas_array[i+1][j+1] == "M" and xmas_array[i+2][j+2] == "A" and xmas_array[i+3][j+3] == "S":
                xmas_count+=1
            if xmas_array[i][j] == "S" and xmas_array[i+1][j+1] == "A" and xmas_array[i+2][j+2] == "M" and xmas_array[i+3][j+3] == "X":
                xmas_count+=1
        if j >= 3:     
            if xmas_array[i][j] == "X" and xmas_array[i+1][j-1] == "M" and xmas_array[i+2][j-2] == "A" and xmas_array[i+3][j-3] == "S":
                xmas_count+=1
            if xmas_array[i][j] == "S" and xmas_array[i+1][j-1] == "A" and xmas_array[i+2][j-2] == "M" and xmas_array[i+3][j-3] == "X":
                xmas_count+=1
mas_count = 0
for i in range(1, num_rows-1):
    for j in range(1,num_cols-1):
        if xmas_array[i][j] == "A":
            if xmas_array[i-1][j-1]+xmas_array[i-1][j+1] =="MS" and xmas_array[i+1][j-1]+xmas_array[i+1][j+1] =="MS":
                mas_count+=1 
            if xmas_array[i-1][j-1]+xmas_array[i-1][j+1] =="SS" and xmas_array[i+1][j-1]+xmas_array[i+1][j+1] =="MM":
                mas_count+=1 
            if xmas_array[i-1][j-1]+xmas_array[i-1][j+1] =="SM" and xmas_array[i+1][j-1]+xmas_array[i+1][j+1] =="SM":
                mas_count+=1 
            if xmas_array[i-1][j-1]+xmas_array[i-1][j+1] =="MM" and xmas_array[i+1][j-1]+xmas_array[i+1][j+1] =="SS":
                mas_count+=1 

print(f"There are {xmas_count} instances of xmas!")
print(f"There are {mas_count} instances of x-mas!")