import os
  
os.chdir('Data_div/obj')
# print(os.getcwd())

path=os.getcwd()

img_list=[]
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    remove_rb=f_name.split('.')
    remove_jpg=remove_rb[0].replace("_jpg",'')
    
    
    new_name = '{}{}'.format(remove_jpg, f_ext)
    os.rename(f, new_name)
