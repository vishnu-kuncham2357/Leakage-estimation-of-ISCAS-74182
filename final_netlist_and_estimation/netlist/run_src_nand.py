import os
import subprocess
import time


def compute_nand(m):
    sum = m[0]*2 +  m[1]
    return sum
    
command = "ngspice dst.ckt"
completed_process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if completed_process.returncode == 0:
    output = completed_process.stdout
else:
    output = ("Command execution failed.")

# print(output)

m1 = []
currents = []
lines = output.splitlines()

# Process each line
for line in lines:
    # Split the line into words
    words = line.split()
    # Check if the line contains at least one word
    if len(words) > 0:
        # Check if the line contains a voltage value
        if 'v(' in words[0]:
            voltage = float(words[2])
            m1.append(voltage)
        if 'i(' in words[0]:
            current = float(words[2])
            currents.append(current)

# Print the arrays of voltage values
# print("m1:", m1)
# print(len(m1))
# print(currents)

count = 0
for i in range(len(m1)):
    if m1[i]<0.5:
        m1[i] = 0
        count = count+1
    else:
        m1[i] = 1

# print(count)
# print(m1)
# Given array of 76 elements
original_array = m1

# Create the 1*4 array
array_1_4 = original_array[:4]

# Create the 25*2 matrix from the next 50 elements
array_25_2 = [original_array[i:i+2] for i in range(4, 54, 2)]

# Create the 12*2 matrix from the rest of the elements
array_12_2 = [original_array[i:i+2] for i in range(54, len(original_array), 2)]

# Print the arrays
# print("Not:", array_1_4)
# print("And:", array_25_2)
# print("or:", array_12_2)


with open('inverter_leakages.txt', 'r') as pmos_file:
    lines = pmos_file.readlines()
with open('And_leakages.txt', 'r') as pmos_file:
    lines1 = pmos_file.readlines()
with open('Or_leakages.txt', 'r') as pmos_file:
    lines2 = pmos_file.readlines()
# print(lines)

nand_indices = []
nand_currents = []
nor_indices = []
sum = 0
for i in range(len(array_25_2)):
    index = compute_nand(array_25_2[i])
    nand_indices.append(index)
    line = lines1[index]
    values = line.split()
    sum = sum+float(values[0])



for i in range(len(array_12_2)):
    index = compute_nand(array_12_2[i])
    nor_indices.append(index)
    line = lines2[index]
    values = line.split()
    sum = sum+float(values[0])

for i in range(len(array_1_4)):
    line = lines[array_1_4[i]]
    values = line.split()
    sum = sum+float(values[0])

# print(array_1_4)
# print(nand_indices)
# print(nand_currents)
# print(sum)

original_sum = 0
for i in range(len(currents)):
    if(currents[i] < 0):
        original_sum = original_sum + abs(currents[i])
# print(original_sum)
error = (abs(original_sum - sum)/original_sum) * 100
print(error)
