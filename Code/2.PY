import os
import numpy as np
import skimage
import cv2

accepted_files = ["jpg","jpeg","png"]
global path, imgs_matrix
imgs_matrix = []
px_size = 50
path = input("Enter path")
for file in os.listdir(path):
    if (file.split(".")[-1]) in accepted_files:
        
        print(file)
        #print(os.path.join)
        p = os.path.join(path,file)
        if not os.path.isdir(p):
            try:
                img = cv2.imdecode(np.fromfile(p, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
                if type(img)==np.ndarray:
                    img = img[..., 0:3]
                    img = cv2.resize(img, dsize=(px_size, px_size), interpolation=cv2.INTER_CUBIC)
                    
                    if len(img.shape) == 2:
                        img = skimage.color.gray2rgb(img)
                    imgs_matrix.append(img)
            except:
                pass

# print(imgs_matrix)
# print(len(imgs_matrix))
def mse(imageA,imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


print(int(mse(imgs_matrix[15],imgs_matrix[16])))
for i in range(len(imgs_matrix)):
    for j in range(i+1,len(imgs_matrix)):
        if int(mse(imgs_matrix[i],imgs_matrix[j]))<=200:
            # print(imgs_matrix[i])
             print(i,j)
             print()


