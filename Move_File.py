import os
import shutil

from_dir = "C:/Users/localuser/Downloads"
to_dir = "C:/Users/localuser/Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    name,ext = os.path.splitext(i)
    print(name)
    print(ext)
    if ext=="":
        continue
    if ext in [".gif",".png",".jpeg",".jpg"]:
        path1 = from_dir+'/'+ i
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + i
        if os.path.exists(path2):
            print("moving "+i+"...")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("moving "+i+"...")
            shutil.move(path1,path3)