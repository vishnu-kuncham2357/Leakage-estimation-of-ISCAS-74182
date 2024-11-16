def d2b(number):
    # Convert the number to binary representation
    binary_string = bin(number)[2:]

    # Pad the binary string with zeros to make it 9 bits long
    padded_binary_string = binary_string.zfill(9)

    # Convert the padded binary string to a list of individual bits
    binary_list = [int(bit) for bit in padded_binary_string]

    # Replace any occurrence of 1 with 1.1
    binary_list = [1.1 if bit == 1 else bit for bit in binary_list]

    return binary_list

def copy_and_replace_file_content(src_file_path, dst_file_path, search_string, replace_string):
    # Read the content of the source file
    with open(src_file_path, 'r') as src_file:
        src_content = src_file.read()

    # Replace the search string with the replace string
    modified_content = src_content.replace(search_string, replace_string)

    # Write the modified content to the destination file
    with open(dst_file_path, 'w') as dst_file:
        dst_file.write(modified_content)

cla_file_path = "CLA.ckt"
dst_file_path = "dst.ckt"
search_string = "*search"
output_array = []
# Run the script for 512 times
for i in range(512):
    # Replace these paths with the actual paths of your files
    bin_i = d2b(i)
    replace_string = "V_Cn Cn gnd " + str(bin_i[0]) + "\nV_G0 G0 gnd " + str(bin_i[1]) + "\nV_P0 P0 gnd " + str(bin_i[2]) + "\nV_G1 G1 gnd " + str(bin_i[3]) + "\nV_P1 P1 gnd " + str(bin_i[4]) + "\nV_G2 G2 gnd " + str(bin_i[5]) + "\nV_P2 P2 gnd " + str(bin_i[6]) + "\nV_G3 G3 gnd " + str(bin_i[7]) + "\nV_P3 P3 gnd " + str(bin_i[8])

    # Call the function to copy content and replace search string
    copy_and_replace_file_content(cla_file_path, dst_file_path, search_string, replace_string)

    # Now run your Python code and append the stdout to a results string
    import subprocess

    # Command to run your Python code
    command = ["python3", "run_src_nand.py"]

    # Run the command and capture the stdout
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

    # Append the stdout to a results string
    output_value = float(result.stdout.strip())
    output_array.append(output_value)
print(output_array)

