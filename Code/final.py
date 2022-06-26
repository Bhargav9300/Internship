import cv2 as cv
import numpy as np
import os
import shutil

global path
global img_lst
global dup

img_lst = []  # To store images in list
dup = []  # To check duplicate images 
path =input("Please enter the path of images folder: ")
unique_folder_path = input("Enter folder path for storing unique images or press enter to create new folder : ")
duplicate_folder_path = input("Enter path of folder for storing duplicate images or press enter to create new folder : ")
accepted_files = ["jpg","png","jpeg","gif"]    # Types of accepted image files.




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


unique1 = unique_folder()
duplicate1 = duplicate_folder()

for file in os.listdir(path):
    if (file.split(".")[-1]) in accepted_files:
        img_lst.append("{}\{}".format(path,file))



for i in range(len(img_lst)-1):   
    for j in range(i+1,len(img_lst)):  # Looping through each image 
        # Comparing each image with all remaining images 
        base = cv.imread(r'{}'.format(img_lst[i]))
        test = cv.imread(r'{}'.format(img_lst[j]))
        
        x1 = base.shape[0]
        y1 = base.shape[1]

        x2 = test.shape[0]
        y2= test.shape[1]

        hsv_base = cv.cvtColor(base, cv.COLOR_BGR2HSV)  # Converting the image from RBG to HSV 
        hsv_test = cv.cvtColor(test, cv.COLOR_BGR2HSV)

        h_bins = 50  
        s_bins = 60
        histSize = [h_bins, s_bins]   # It is the number of lines or commands that are stored in memory in a history
                                      # list while your bash session is ongoing.
        h_ranges = [0, 180]
        s_ranges = [0, 256]
        ranges = h_ranges + s_ranges
        channels = [0, 1]

                    #cv2.calcHist(images(as list), channels(converting to greyscale), mask(None), histSize, ranges)

        hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
        cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
        hist_test = cv.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
        cv.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
        
        #cv2.normalize(source, destination ,alpha(lower bound value) , beta(upper bound value)  norm_type )
        # When the normType is NORM_MINMAX, "cv2.normalize" normalizes source in such a way that the min value of destination is 
        # alpha and max value of dst is beta


        compare_method = cv.HISTCMP_CORREL

        # One of the comparision methods that calculates correlation of 2 histograms.


        base_test = cv.compareHist(hist_base, hist_test, compare_method)


        #print('base_test Similarity = ', base_test)
        if base_test >=0.8 and img_lst[j] not in dup:  
            '''base_test>=0.8 means if the image compared is 80% similar to the base image, then it is considered as a duplicate 
            of the base image, We can change the base_test to our required percentage'''
            if x1>=x2 and y1>=y2:
                dup.append(img_lst[j])
            else:
                dup.append(img_lst[i])

            
print(dup)

for i in img_lst:
    if i not in dup:
        original = r'{}'.format(i) 
        target = r'{}'.format(unique1)
        shutil.copy(original,target)  # We can use "shutil.move" to move the images instead of making a copy.
        

    else:
        original = r'{}'.format(i) 
        target = r'{}'.format(duplicate1)
        shutil.copy(original,target)
    
    