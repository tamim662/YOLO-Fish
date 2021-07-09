import glob
import os
import re

def class_changer(files_path):
    for i, file_path in enumerate(files_path):
    
        with open(file_path, "r") as f_o:
            
            lines = f_o.readlines()

            text_converted = []
            for line in lines:
                print(line)
                numbers = re.findall("[0-9.]+", line)
                print(numbers)
                if numbers:

                    # Define coordinates
                    text = "{} {} {} {} {}".format(0, numbers[1], numbers[2], numbers[3], numbers[4])
                    text_converted.append(text)
                    #print(i, file_path)
                    #print(text)
            # Write file
            with open(file_path, 'w') as fp:
                for item in text_converted:
                    fp.writelines("%s\n" %item)
                        

#put the directory name
txt_files_path = glob.glob(r"/media/tamim/Study/Datasets/Ozfish/roboflow/ozfish.v1-batch01_check01.darknet/train/annot/*.txt") # (r"directory_name/*.txt")


class_changer(txt_files_path)
                    