import os
import hashlib
import shutil

path =input("Please enter your path")
unique_floder_path = input("Enter unique folder path: ")
duplicate_folder_path = input("Enter path of duplicate folder: ")
accepted_files = ["jpg","png","jpeg"]
img_dict = {}
Unique_images = []
images_hex=[]
Duplicate_images=[]

def sha256sum(filename, bufsize=128 * 1024):
    h = hashlib.sha256()
    buffer = bytearray(bufsize)
    # using a memoryview so that we can slice the buffer without copying it
    buffer_view = memoryview(buffer)
    with open(filename, 'rb', buffering=0) as f:
        while True:
            n = f.readinto(buffer_view)
            if not n:
                break
            h.update(buffer_view[:n])
    return h.hexdigest()

for file in os.listdir(path):
    if (file.split(".")[-1]) in accepted_files:
        img_dict[file] = sha256sum(file)
        if img_dict[file] not in images_hex:
            original = r'{}\{}'.format(path,file) 
            target = r'{}'.format(unique_floder_path)
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




