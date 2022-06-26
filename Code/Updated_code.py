
import numpy as np
import cv2
import os
import imghdr


# Function that searches the folder for image files, converts them to a tensor
def create_imgs_matrix(directory, px_size=50):
    global image_files   
    image_files = []
    # create list of all files in directory     
    folder_files = [filename for filename in os.listdir(directory)]  
    
    # create images matrix   
    counter = 0
    for filename in folder_files: 
        # check if the file is accesible and if the file format is an image
        if not os.path.isdir(directory +"\\"+ filename) and imghdr.what(directory +"\\" +  filename):
            # decode the image and create the matrix
            img = cv2.imdecode(np.fromfile(directory + filename, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
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
    return imgs_matrix


# Function that calulates the mean squared error (mse) between two image matrices
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err



#Function for rotating an image matrix by a 90 degree angle
def rotate_img(image):
    image = np.rot90(image, k=1, axes=(0, 1))
    return image



# Function for checking the quality of compared images, appends the lower quality image to the list
def check_img_quality(directory, imageA, imageB, list):
    add_to_list = []
    size_imgA = os.stat(directory + imageA).st_size
    size_imgB = os.stat(directory + imageB).st_size
    if size_imgA > size_imgB:
        add_to_list(imageB, list)
    else:
        add_to_list(imageA, list)

print(create_imgs_matrix(input()))



