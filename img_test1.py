import os
import hashlib
import shutil
import uuid

path =input("Please enter your path")
unique_folder_path = input("Enter unique folder path: ")
duplicate_folder_path = input("Enter path of duplicate folder: ")
accepted_files = ["jpg","png","jpeg"]
img_dict = {}
Unique_images = []
images_hex=[]
Duplicate_images=[]

def unique_id(filename):
    return(uuid.uuid1())


for file in os.listdir(path):
    if (file.split(".")[-1]) in accepted_files:
        img_dict[file] = unique_id(file)
        if img_dict[file] not in images_hex:
            original = r'{}\{}'.format(path,file) 
            target = r'{}'.format(unique_folder_path)
            shutil.move(original,target) 
            Unique_images.append(path + "/" + file)
            images_hex.append(img_dict[file])
        else:
            Duplicate_images.append(path + "/" +file)
            original = r'{}\{}'.format(path,file) 
            target = r'{}'.format(duplicate_folder_path)
            shutil.move(original,target) 

print(Unique_images)
print(images_hex)
print("\n")
print(Duplicate_images)


# C:\Users\revanth\Desktop\bhargav\internship




