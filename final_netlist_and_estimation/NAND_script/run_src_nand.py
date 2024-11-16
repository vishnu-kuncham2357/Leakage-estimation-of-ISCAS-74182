import os
import subprocess
import time
import numpy as np

def compute(m):
    m[0] = ((round(m[0]/0.05)*0.05))/0.05
    m[1] = (round(m[1]/1.1))*529
    m[2] = 23*((round(m[2] / 0.05) * 0.05)/0.05)
    sum = m[0] + m[1] + m[2]
    return sum
    
#destination file name should be written here
command = "ngspice NAND.ckt"
completed_process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if completed_process.returncode == 0:
    # Capture the standard output into a string
    output = completed_process.stdout
else:
    output = ("Command execution failed.")

#print(output)

m1 = []
# Split the data into lines
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

# Print the arrays of voltage values
#print("m1:", m1)
k = 0
i = 0
indices_m1 = []
while i<(len(m1)/3):
    index = compute(m1[k:k+3])
    indices_m1.append(index)
    # print(index)
    k = k+3
    i = i+1
#print(indices_m1)
#rint(f"length of array = {len(indices_m1)}")
with open('PMOS_2W_L.txt', 'r') as pmos_file:
    lines = pmos_file.readlines()
with open('Nmos_2W_L.txt', 'r') as nmos_file:
    lines1 = nmos_file.readlines()

index_array = indices_m1

sum = 0
count = 0 #for number of mosfets
input = 0 #for number of inputs
i = 0
i_matrix = []
input = 0
for i in range(16):
    j = i%4
    if j < 2:  #pmos
        line = lines[int(index_array[i])]
        values = line.split()

        temp = [abs(float(values[3])), abs(float(values[4])), abs(float(values[5])), abs(float(values[6]))]
        i_matrix.append(temp)
        
        count = count + 1
    else:           #nmos
        line = lines1[int(index_array[i])]
        values = line.split()

        temp = [abs(float(values[3])), abs(float(values[4])), abs(float(values[5])), abs(float(values[6]))]
        i_matrix.append(temp)
        count = count + 1
    
    #compute current

    # print(fourth_value)
    if(count == 4):
        # print(f"{input} : {sum}")
        count = 0
        if(input == 0):
            # print(i_matrix)
            sum = abs(2*i_matrix[0][1] + i_matrix[2][0] - 2*i_matrix[0][3])+ 2*i_matrix[0][3]
            sum_original = 2.20081e-10 + 2.20081e-10 
        elif(input == 1):
            # print(i_matrix)
            sum = abs(i_matrix[0][1] + i_matrix[2][0] - i_matrix[0][3] + i_matrix[3][1]) + i_matrix[0][3]
            sum_original = 2.54154e-09 +4.44089e-16+ 1.03873e-15  + 7.71898e-11
        elif(input == 2):
            # print(i_matrix)
            sum = abs(i_matrix[3][0] + i_matrix[2][3] - i_matrix[2][1]) + i_matrix[1][1] - i_matrix[1][3]  + i_matrix[1][3]+ i_matrix[2][1]
            sum_original = 4.23638e-16 + 1.09069e-09 + 2.62013e-14
        elif(input == 3):
            # print(i_matrix)
            sum = 2*i_matrix[0][2] + 2*i_matrix[0][1] + 2*i_matrix[2][1] + 2*i_matrix[0][3]
            sum_original = 2*5.94862e-10 + 2*8.48526e-11 + 2*7.71863e-11 
        percentage = (abs(sum_original-sum)/sum_original)*100
        # print(f"for input={input} : current is {sum} and original is {sum_original} with error {percentage}")
        print(f"{sum}")
        input = input +1
        i_matrix = []
    

#sum = 2.55077e-09 + 2.114952e-10 + 7.71903e-11
#sum1 = 6.62794308765e-09
#print(sum)
# percentage_err = ((sum1 - sum) / sum ) * 100
# print(percentage_err)
# total = 3.60944e-09  
# print(total)
# 528.0, 22.0, 1057.0, 529.0
