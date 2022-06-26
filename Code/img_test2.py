from re import L
from PIL import Image
import math , operator
import os
import shutil
global l 
l =[]

def img_per(i1,i2):
    (w1,h1) = i1.size
    (w2,h2) = i2.size
    if w1>w2:
        i2 = i2.resize((w1,h1))
    else:
        i1 = i1.resize((w2,h2))
     
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
     
    ncomponents = i1.size[0] * i1.size[1] * 3
    return ((dif / 255.0 * 100) / ncomponents)

path = input("Enter path")
accepted_files = ["jpg","jpeg","png"]
for file in os.listdir(path):
    if (file.split(".")[-1]) in accepted_files:
        curr_path = os.path.join(path,file)
        l.append(curr_path)
        i1 = Image.open(r'{}'.format(curr_path) )
        i2 = Image.open(r'{}'.format(curr_path) )
d = []


# x =r"C:\Users\revanth\Desktop\bhargav\internship\Images\img_2(2).jpg"
# y = r'C:\Users\revanth\Desktop\bhargav\internship\Images\img_2.jpg'
# i1 = Image.open(r'{}'.format(x) )
# i2 = Image.open(r'{}'.format(y) )

# print(img_per(i1,i2))


unique1 = input("uniq floder")
duplicate1 = input("dup folder")

for i in range(len(l)):
    c = 0
    for j in range(i+1,len(l)):
        
        i1 = Image.open(r'{}'.format(l[i]) )
        i2 = Image.open(r'{}'.format(l[j]) )
        p = img_per(i1,i2)

        if p< 17 and l[j] not in u:
            #c+=1

            img_path = l[j]
            original = r'{}'.format(l[j]) 
            target = r'{}'.format(duplicate1)
            shutil.copy(original,target) 
            print(l[i], l[j])
            print()
            d.append(l[j])

for i in l:
    if i not in u:
        #Duplicate_images.append(path + "\ " +file)
        original = r'{}'.format(i) 
        target = r'{}'.format(unique1)
        shutil.copy(original,target)


    





#this will resize any format of image file
# assert i1.mode == i2.mode, "Different kinds of images."
# assert i1.size == i2.size, "Different sizes."

