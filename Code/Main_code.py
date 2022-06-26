
"""Problem Statement : Three folders with images will be provided , all stored with unique names of which some images are 
                       similar and some are not. For this reason , two new folders are to be created , one containing all 
                       the unique images in it and the other folder containing the duplicate images.
"""

import os
import hashlib
import shutil
import numpy as np
import cv2


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



# Function to create a new duplicate folder for storing duplicate images.
def duplicate_folder():

    if(duplicate_folder_path):
        return duplicate_folder_path

    else:
        folder_name = input("Enter folder name for storing duplicate images: ")
        folder = os.path.join(path,folder_name)
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

def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err
# Creating unique hash ID for unique images using md5 algorithm 
def create_imgs_matrix(path, filename, px_size = 50):
    global image_files
    image_files = []
    counter = 0
    img = cv2.imdecode(np.fromfile(os.path.join(path,filename), dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    if type(img) == np.ndarray:
        img = img[...,0:3]
        # resize the image based on the given compression value
        img = cv2.resize(img, dsize=(px_size, px_size), interpolation=cv2.INTER_CUBIC)
        if counter == 0:
            imgs_matrix = img
            image_files.append(filename)
            counter += 1
        else:
            imgs_matrix = np.concatenate((imgs_matrix, img))
            image_files.append(filename)

def hashing_images(filename):
    # This function will return the `md5` checksum for any input image.
    
    # with open(img_path, mode="rb") as f:
    #     img_hash = hashlib.md5()
    #     while chunk := f.read(8192):
    #        img_hash.update(chunk)
    # return img_hash.hexdigest()



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
# Used cases, scenarios 

unique1 = unique_folder()
duplicate1 = duplicate_folder()


# The images are accessed and mapping of images with its hash ID is done.
for file in os.listdir(path):
    l = []
    if (file.split(".")[-1]) in accepted_files:
        #print(file)
        
        img_dict[file] = hashing_images(os.path.join(path,file.split(".")[0]))
        l.append(create_imgs_matrix(path,file))
        if img_dict[file] not in images_hex:

            img_path = os.path.join(path,file)
            original = os.path.join(path,file) 
            target = r'{}'.format(unique1)
            shutil.copy(original,target)     # The unique images are copied into unique_folder created above.
            Unique_images.append(img_path)
            images_hex.append(img_dict[file])

        else:

            Duplicate_images.append(os.path.join(path,file))
            original = r'{}\{}'.format(path,file) 
            target = r'{}'.format(duplicate1)
            shutil.copy(original,target)   # The duplicate images are copied into duplicate_folder.
            
# We can use "shutil.move" to directly move the images without making a copy of it.



# Here we can observe the path for unique_images, Duplicate images and the dictionary containing images with its hashing ID.
print("\n {} \n".format(Unique_images))
print(Duplicate_images)
print("\n {}\n".format(img_dict))
print(l)
print("\n\n Program Execution Successful! ")
