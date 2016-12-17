import os

top = "."

for root, dirs, files in os.walk(top, topdown=False):
   for name in files:
       print(":::"+name)
   for name in dirs:
       print("_"+name)
       #os.rmdir(os.path.join(root, name))