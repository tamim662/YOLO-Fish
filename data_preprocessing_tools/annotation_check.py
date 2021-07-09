# Check that all annoations have done correctly.
import glob
import os
import re

#put the directory name
txt_file_paths = glob.glob(r"raw_data/9908/Annot_9908/*.txt")

flag=True
for i, file_path in enumerate(txt_file_paths):
    # get image size
    if flag:

        with open(file_path, "r") as f_o:
            lines = f_o.readlines()

            text_converted = []
            for line in lines:
                # print(line)
                # numbers = re.findall("[0-9.]+", line)
                # # print(numbers)
                if line[0]== '0':
                    continue
                    
                else:
                    print("{} file is not okay!".format(file_path))
                    flag=False
                    
    
    if flag is not True:
        break

if i==len(txt_file_paths)-1:
    print("Everything is fine")

