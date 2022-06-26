import cv2 as cv
import numpy as np
import os
import shutil

# global path
# global img_lst
# global dup

# img_lst = []  # To store images in list
# dup = []  # To check duplicate images 
# path =input("Please enter the path of images folder: ")
# unique_folder_path = input("Enter folder path for storing unique images or press enter to create new folder : ")
# duplicate_folder_path = input("Enter path of folder for storing duplicate images or press enter to create new folder : ")
# accepted_files = ["jpg","png","jpeg","gif"]    # Types of accepted image files.




# # Function to create a new folder for storing unique images if required.
# def unique_folder():
    
#     if(unique_folder_path):
#         return unique_folder_path

#     else:
#         folder_name = input("Enter folder name for storing unique images: ")
#         folder = path + "/" + folder_name
#         try:
#             os.mkdir(folder)
#             return(folder)
#         except:
#             existing_folder = input("{} Folder name already exists. Want to create a new one? press yes/no: ".format(folder_name))
#             if(existing_folder.lower()=="yes" ):
#                 name = input("Enter name for the unique folder: ")
#                 folder = path + "\ " + name
#                 os.mkdir(folder)
#                 return(folder)
#             else:
#                 return(folder)



# # Function to create a new duplicate folder for storing duplicate images.
# def duplicate_folder():

#     if(duplicate_folder_path):
#         return duplicate_folder_path

#     else:
#         folder_name = input("Enter folder name for storing duplicate images: ")
#         folder = path + "/" + folder_name
#         try:
#             os.mkdir(folder)
#             return(folder)
#         except:
#             existing_folder = input("{}  Folder already exists. Want to create a new one? press yes/no: ".format(folder_name))
#             if(existing_folder.lower()=="yes" ):
#                 name = input("Enter name for the duplicate folder: ")
#                 folder = path + "\ " + name
#                 os.mkdir(folder)
#                 return(folder)
#             else:
#                 return(folder)


# unique1 = unique_folder()
# duplicate1 = duplicate_folder()

# for file in os.listdir(path):
#     if (file.split(".")[-1]) in accepted_files:
#         img_lst.append("{}\{}".format(path,file))


# print(type(img_lst[0]))
# a = img_lst[0]
# print(type(r'C:\Users\revanth\Desktop\bhargav\internship\Images\img_1(2).jpg'))
# base = cv.imread(r'{}'.format(img_lst[0]))
# cv.imshow('base',base)
# cv.waitKey(0)



base = cv.imread(r'C:\Users\revanth\Desktop\bhargav\internship\Images\res_1.jpg')
test = cv.imread(r'C:\Users\revanth\Desktop\bhargav\internship\Images\res_2.jpg')
#test2 = cv.imread('img_2(2).jpg')

hsv_base = cv.cvtColor(base, cv.COLOR_BGR2HSV)
hsv_test = cv.cvtColor(test, cv.COLOR_BGR2HSV)
#hsv_test2 = cv.cvtColor(test2, cv.COLOR_BGR2HSV)

h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges
channels = [0, 1]

hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
hist_test = cv.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
#hist_test2 = cv.calcHist([hsv_test2], channels, None, histSize, ranges, accumulate=False)
#cv.normalize(hist_test2, hist_test2, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

compare_method = cv.HISTCMP_CORREL

base_base = cv.compareHist(hist_base, hist_base, compare_method)
base_test = cv.compareHist(hist_base, hist_test, compare_method)
#base_test2 = cv.compareHist(hist_base, hist_test2, compare_method)

#print('base_base Similarity = ', base_base)

print('base_test Similarity = ', base_test)
# cv.imshow('base',base)
# cv.imshow('test1',test)
# #cv.imshow('test2',test2)
# cv.waitKey(0)

'''for i in range(len(img_lst)-1):
    #a = (f"r'{i}'")
    for j in range(i+1,len(img_lst)-1):
        #print(img_lst[i],img_lst[j])
        # i = (f"r'{img_lst[i]}'")
        # j = (f"r'{img_lst[j]}'" )
        #print(i,j)

        base = cv.imread(r'{}'.format(img_lst[i]))
        test = cv.imread(r'{}'.format(img_lst[j]))
        #test2 = cv.imread('img_2(2).jpg')

        hsv_base = cv.cvtColor(base, cv.COLOR_BGR2HSV)
        hsv_test = cv.cvtColor(test, cv.COLOR_BGR2HSV)
        #hsv_test2 = cv.cvtColor(test2, cv.COLOR_BGR2HSV)

        h_bins = 50
        s_bins = 60
        histSize = [h_bins, s_bins]
        h_ranges = [0, 180]
        s_ranges = [0, 256]
        ranges = h_ranges + s_ranges
        channels = [0, 1]

        hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
        cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
        hist_test = cv.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
        cv.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
        #hist_test2 = cv.calcHist([hsv_test2], channels, None, histSize, ranges, accumulate=False)
        #cv.normalize(hist_test2, hist_test2, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

        compare_method = cv.HISTCMP_CORREL

        base_base = cv.compareHist(hist_base, hist_base, compare_method)
        base_test = cv.compareHist(hist_base, hist_test, compare_method)
        #base_test2 = cv.compareHist(hist_base, hist_test2, compare_method)

        #print('base_base Similarity = ', base_base)

        print('base_test Similarity = ', base_test)
        if base_test >=0.8 and img_lst[j] not in dup:
            dup.append(img_lst[j])

            #img_lst.remove(img_lst[j])


        #print('base_test2 Similarity = ', base_test2)

        # cv.imshow('base',base)
        # cv.imshow('test1',test)
        # #cv.imshow('test2',test2)
        # cv.waitKey(0)

#print(img_lst)
print(dup)

for i in img_lst:
    if i not in dup:
        original = r'{}'.format(i) 
        target = r'{}'.format(unique1)
        shutil.copy(original,target)

    else:
        original = r'{}'.format(i) 
        target = r'{}'.format(duplicate1)
        shutil.copy(original,target)
    '''
    