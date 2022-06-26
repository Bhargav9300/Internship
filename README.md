# Internship
**Problem Statement**: Three folders with images will be provided , all stored with unique names of which some images are similar and some are not. For this reason , two new folders are to be created , one containing all the unique images in it and the other folder containing the duplicate images.

I have developed the code in which, the images are accessed from a folder and all the unique images are copied into "Unique" folder and all the duplicates are copied into "Duplicate" folder.

**Inputs:**

Images folder path
Path of Unique images folder (To store all the unique images)
Path of Duplicate images folder( To store all the duplicate images)

**Output:**

All the Unique images are stored in the unique images folder you have created and the duplicates are transferred to Duplicate images folder.


**Working:**

If you have not created any folder for unique and duplicate images, press enter when aked for unique and duplicate folders path and then it will ask you to name the folder and create one for you at the images path (i.e., the images path you have entered as the first input)

The code can even compare an image with its cropped version or zoomed version and identify it as duplicate.

Even with different resolutions of same image, the image with lower resolution wil be transferred to duplicate folder and the one with higher resolution is saved in unique images folder. 

We can always change the "percentage similarity" of two images which is used as the base to decide if an image is duplicate or not, as per our requirement. It ranges from 0 to 1 and 0 implies 0% similarity and 1 means 100% similar. 


