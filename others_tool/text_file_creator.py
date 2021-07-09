import os
  
os.chdir('/media/tamim/Study/Datasets/DeepFish/me1/7117/empty')
# print(os.getcwd())

path=os.getcwd()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_ext='.txt'

    file = '{}{}'.format(f_name, f_ext)

    with open(os.path.join(path, file), 'w') as fp:
        
        pass