import os
import hashlib
import shutil
import cv2
import numpy as np
import skimage

from Main_code import create_imgs_matrix 

global path

path =input("Please enter the path of images folder: ")
unique_folder_path = input("Enter folder path for storing unique images or press enter to create new folder : ")
duplicate_folder_path = input("Enter path of folder for storing duplicate images or press enter to create new folder : ")
accepted_files = ["jpg","png","jpeg","gif"]

img_dict = {}
images_hex=[]
Unique_images = []
Duplicate_images=[]

# hashing=[]





def unique_folder():
    
    if(unique_folder_path):
        return unique_folder_path

    else:
        folder_name = input("Enter folder name for storing unique images: ")
        folder = os.path.join(path,folder_name)
        try:
            os.mkdir(folder)
            return(folder)
        except:
            existing_folder = input("{} Folder name already exists. Want to create a new one? press yes/no: ".format(folder_name))
            if(existing_folder.lower()=="yes" ):
                name = input("Enter name for the unique folder: ")
                folder = os.path.join(path, name)
                os.mkdir(folder)
                return(folder)
            else:
                return(folder)




def duplicate_folder():

    if(duplicate_folder_path):
        return duplicate_folder_path

    else:
        folder_name = input("Enter folder name for storing duplicate images: ")
        folder = os.path.join(path ,folder_name)
        try:
            os.mkdir(folder)
            return(folder)
        except:
            existing_folder = input("{}  Folder already exists. Want to create a new one? press yes/no: ".format(folder_name))
            if(existing_folder.lower()=="yes" ):
                name = input("Enter name for the duplicate folder: ")
                folder = os.path.join(path, name)
                os.mkdir(folder)
                return(folder)
            else:
                return(folder)



unique1 = unique_folder()
duplicate1 = duplicate_folder()


for file in os.listdir(path):
    if (file.split(".")[-1]) in accepted_files:
        print(file)
#         img_dict[file] = hashing_images(os.path.join(path,file))
#         if img_dict[file] not in images_hex:
#             img_path = path + "\ " + file
#             original = r'{}\{}'.format(path,file) 
#             target = r'{}'.format(unique1)
#             shutil.copy(original,target) 
#             Unique_images.append(img_path)
#             images_hex.append(img_dict[file])

#         else:

#             Duplicate_images.append(path + "\ " +file)
#             original = r'{}\{}'.format(path,file) 
#             target = r'{}'.format(duplicate1)
#             shutil.copy(original,target) 



# print("\n {} \n".format(Unique_images))
# print(Duplicate_images)
# print("\n {}\n".format(img_dict))
# print(unique1)
# print(duplicate1)
# print("\n\n Program Execution Successful! ")





