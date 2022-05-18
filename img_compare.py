# import module
from PIL import Image, ImageChops
import os
import cv2

# assign images
img1 = Image.open("1img.jpg")
img2 = Image.open("2img.jpg")
#print(img2.size)
#print("\n")
#print(img1.size)

# finding difference
diff = ImageChops.difference(img1, img2)

# showing the difference
#diff.show()
#clrs = diff.getcolors()
#if (len(clrs)==1):
#    print("Equal")
#else:
#    print("Not Equal")
if not diff.getbbox():
    print("Equal")
    diff.save('C:\Users\revanth\Desktop\bhargav\internship\Similar.jpeg')
    
else:
    print("Not equal")
    #diff.save('/jpg/{}.jpg'.format("Unique"))
