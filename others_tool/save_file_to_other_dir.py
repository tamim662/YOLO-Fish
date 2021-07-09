import shutil
import os

os.chdir('/media/tamim/Study/Datasets/frames')
dst_dir = "/media/tamim/Study/Datasets/new1"
for f in os.listdir():
    shutil.copy(f, dst_dir)