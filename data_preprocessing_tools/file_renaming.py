import os
  
os.chdir('/media/tamim/Study/Datasets/Ozfish/verison1/batch03') # put the dir
print(os.getcwd())

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_ext=".png"
    
    
  
    new_name = '{}{}'.format(f_name, f_ext)
    os.rename(f, new_name)