#! python3
# Rename.py
# Rename the filenames in order 
# Folder 名の名前をつけれていない。。。


import os, re, glob
   
# Folder Name
CWD = os.path.abspath(".")  #CWD
FolderName = re.findall('[a-z|0-9]+$', CWD) #Folder Name

print(FolderName)
path = "./*.pdf"
i=1

flist = glob.glob(path)
print("Current File Name")
print(flist)

for file in flist:
    os.renames(file,'FolderName'+str(i)+".pdf" )
    i+=1

list = glob.glob(path)
print("Rename Files")
print(list)