import os
import subprocess
import time

#destination file name should be written here
command = "ngspice dst.net"

fp3 = open("output.txt",'w')
fp3.close()

for i in range(0,1):

    #open src file and output file
    f1 = open("src.net",'r') #source file
    f2 = open("dst.net",'w') #run file/destination file
    fp3 = open("output.txt",'a') #output file

    fp3.write(f"Matrices for W = {(i+1)*45}n\n")
    #reading data into a string 
    data = f1.read()

    search_text = ".PARAM Wmin=45n"
    replace_text = f".PARAM Wmin = 45n*{i+1}"
    data = data.replace(search_text,replace_text)
    f1.close()

    f2.write(data)
    f2.close()

    completed_process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if completed_process.returncode == 0:
        # Capture the standard output into a string
        output = completed_process.stdout
    else:
        output = ("Command execution failed.", i)

    fp3.write(output+"\n")
    fp3.close()
    # time.sleep(0.5)
 
