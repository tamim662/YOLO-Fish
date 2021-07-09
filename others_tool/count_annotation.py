import os
import glob
def count_lines(filename):
    with open(filename, "r") as file:

        txt_file = file.read()
        colist = txt_file.split("\n")
        count=0
        for i in colist:
            if i:
                count+=1

    return count


# os.chdir('batch1_darknet')
txt_file_paths = glob.glob(r"9908/Annot_9908/*.txt")
total=0
for f in txt_file_paths:
    total+=count_lines(f)

print("Total lines in this directory is: ", total)    