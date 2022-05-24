import os
import hashlib
import shutil

global path

path =input("Please enter the path of images folder: ")
unique_folder_path = input("Enter unique folder path  or press enter to create new folder : ")
duplicate_folder_path = input("Enter path of duplicate folder or press enter to create new folder : ")
accepted_files = ["jpg","png","jpeg"]
img_dict = {}
Unique_images = []
images_hex=[]
Duplicate_images=[]



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
                folder = path + "/" + name
                os.mkdir(folder)
                return(folder)
            else:
                return(folder)




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
                folder = path + "/" + name
                os.mkdir(folder)
                return(folder)
            else:
                return(folder)



def hashing_images(filename):
    BLOCK_SIZE = 65536  # 64kb data 
    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(filename, 'rb') as file: # Reading the image as bytes
        fb = file.read(BLOCK_SIZE) # Read from the file. 
        while len(fb) > 0: 
            file_hash.update(fb) # Update the hash
            fb = file.read(BLOCK_SIZE)
    return file_hash.hexdigest()



unique1 = unique_folder()
duplicate1 = duplicate_folder()
for file in os.listdir(path):
    if (file.split(".")[-1]) in accepted_files:
        img_dict[file] = hashing_images(file)
        if img_dict[file] not in images_hex:

            img_path = path + "/" + file
            original = r'{}\{}'.format(path,file) 
            target = r'{}'.format(unique1)
            shutil.move(original,target) 
            Unique_images.append(img_path)
            images_hex.append(img_dict[file])

        else:

            Duplicate_images.append(path + "/" +file)
            original = r'{}\{}'.format(path,file) 
            target = r'{}'.format(duplicate1)
            shutil.move(original,target) 



print("{} \n".format(Unique_images))
print(images_hex)
print("\n")
print(Duplicate_images)

