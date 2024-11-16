# Open the output file
with open('output.txt', 'r') as file:
    lines = file.readlines()

# Initialize arrays for each variable
v_drain_values = []
v_gate_values = []
v_source_values = []
i_vd_values = []
i_vg_values = []
i_vs_values = []
i_vb_values = []

# Process each line in the file
for line in lines:
    # Split the line into words
    words = line.split()

    # Check if the line contains the relevant information
    if 'v(drain)' in words:
        v_drain = float(words[2])
        v_drain_values.append(v_drain)

    elif 'v(gate)' in words:
        v_gate = float(words[2])
        v_gate_values.append(v_gate)

    elif 'v(source)' in words:
        v_source = float(words[2])
        v_source_values.append(v_source)

    elif 'i(vd)' in words:
        i_vd = float(words[2])
        i_vd_values.append(i_vd)

    elif 'i(vg)' in words:
        i_vg = float(words[2])
        i_vg_values.append(i_vg)

    elif 'i(vs)' in words:
        i_vs = float(words[2])
        i_vs_values.append(i_vs)

    elif 'i(vb)' in words:
        i_vb = float(words[2])
        i_vb_values.append(i_vb)

# Combine the values into rows
data_rows = list(zip(v_drain_values, v_gate_values, v_source_values, i_vd_values, i_vg_values, i_vs_values, i_vb_values))

# Print the header
print('v(drain) v(gate) v(source) i(vd) i(vg) i(vs) i(vb)')

# Print the data rows
for row in data_rows:
    print(*row)
