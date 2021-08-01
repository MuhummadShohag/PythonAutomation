'''
    * os.walk(path): it is used to generate directory and file names in a directory tree
                by walking

'''
import os
path='path'
# print(list(os.walk(path)))

# print(os.rmdir(path+"\\"+"good"))

for r,d,f in os.walk(path):
   if len(f) != 0:
    for each_file in f: 
        print(os.path.join(r,each_file))  





    