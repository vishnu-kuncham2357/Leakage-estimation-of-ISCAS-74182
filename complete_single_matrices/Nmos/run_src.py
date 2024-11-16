import os
import subprocess
import time

#destination file name should be written here
command = "ngspice src.net"
file_name = "output.txt"

# fp3 = open(file_name,'w')
# fp3.close()

fp3 = open(file_name,'a') #output file


completed_process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if completed_process.returncode == 0:
    # Capture the standard output into a string
    output = completed_process.stdout
else:
    output = ("Command execution failed.")

fp3.write(output+"\n")
fp3.close()
 
