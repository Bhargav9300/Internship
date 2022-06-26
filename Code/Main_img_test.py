
"""Problem Statement : Three folders with images will be provided , all stored with unique names of which some images are 
                       similar and some are not. For this reason , two new folders are to be created , one containing all 
                       the unique images in it and the other folder containing the duplicate images.
"""

import os
import hashlib
import shutil

global path

path =input("Please enter the path of images folder: ")
unique_folder_path = input("Enter folder path for storing unique images or press enter to create new folder : ")
duplicate_folder_path = input("Enter path of folder for storing duplicate images or press enter to create new folder : ")
accepted_files = ["jpg","png","jpeg","gif"]    # Types of accepted image files.

img_dict = {}   # To store image_name with its respective hash ID 
images_hex=[]   # To store images in list
Unique_images = []   # Storing all unique images
Duplicate_images=[]  # Storing duplicate images


# Function to create a new folder for storing unique images if required.
def unique_folder():
    
    if(unique_folder_path):
        return unique_folder_path

    else:
        folder_name = input("Enter folder name for storing unique images: ")
        folder = path + "/" + folder_name
        try:
            os.mkdir(folder)
            return(folder)
        except:
            existing_folder = input("{} Folder name already exists. Want to create a new one? press yes/no: ".format(folder_name))
            if(existing_folder.lower()=="yes" ):
                name = input("Enter name for the unique folder: ")
                folder = path + "\ " + name
                os.mkdir(folder)
                return(folder)
            else:
                return(folder)



# Function to create a new duplicate folder for storing duplicate images.
def duplicate_folder():

    if(duplicate_folder_path):
        return duplicate_folder_path

    else:
        folder_name = input("Enter folder name for storing duplicate images: ")
        folder = path + "/" + folder_name
        try:
            os.mkdir(folder)
            return(folder)
        except:
            existing_folder = input("{}  Folder already exists. Want to create a new one? press yes/no: ".format(folder_name))
            if(existing_folder.lower()=="yes" ):
                name = input("Enter name for the duplicate folder: ")
                folder = path + "\ " + name
                os.mkdir(folder)
                return(folder)
            else:
                return(folder)


# Creating unique hash ID for unique images using md5 algorithm 
def hashing_images(filename):
    BLOCK_SIZE = 65536   
    file_hash = hashlib.md5() 
    with open(filename, 'rb') as file: 
        fb = file.read(BLOCK_SIZE) 
        while len(fb) > 0: 
            file_hash.update(fb) 
            fb = file.read(BLOCK_SIZE)
    return file_hash.hexdigest()

# Check for resolution
#Report of limitations, brief about what the code does, tabular contents, future enhancement --- 3 pgs
# Used cases, scenarios , 

unique1 = unique_folder()
duplicate1 = duplicate_folder()


# The images are accessed and mapping of images with its hash ID is done.
for file in os.listdir(path):
    if (file.split(".")[-1]) in accepted_files:
        #print(file)
        img_dict[file] = hashing_images(file)
        if img_dict[file] not in images_hex:

            img_path = path + "\ " + file
            original = r'{}\{}'.format(path,file) 
            target = r'{}'.format(unique1)
            shutil.copy(original,target)     # The unique images are copied into unique_folder created above.
            Unique_images.append(img_path)
            images_hex.append(img_dict[file])

        else:

            Duplicate_images.append(path + "\ " +file)
            original = r'{}\{}'.format(path,file) 
            target = r'{}'.format(duplicate1)
            shutil.copy(original,target)   # The duplicate images are copied into duplicate_folder.
            
# We can use "shutil.move" to directly move the images without making a copy of it.



# Here we can observe the path for unique_images, Duplicate images and the dictionary containing images with its hashing ID.
print("\n {} \n".format(Unique_images))
print(Duplicate_images)
print("\n {}\n".format(img_dict))
print("\n\n Program Execution Successful! ")