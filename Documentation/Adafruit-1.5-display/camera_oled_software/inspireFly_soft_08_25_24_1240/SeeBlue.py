#Program reads set of images and runs through them to determine the percentage of the image that is blue
#the program then compares the percentages and determines which image of the selection has the highest percentage of blue
#the respective image is labeled with a 1 and the directory is output in the command shell
#Ideally, this algorithm will automatically determine images taken (internal counter) and then automatically send the best
#image to be transmit to ground
#Should also not decide best picture, but optimal percentage of blue for an ideal image

import cv2

def SeeBlue(jpgfile, tol):
    
    print("Running")

    M = cv2.imread(jpgfile) 

    numrow, numcol, numcolor = M.shape

    red = M[:,:,2]
    green = M[:,:,1]
    blue = M[:,:,0]
    
    #print(blue)

    bluePercent = 0 

    for i in range(numrow): 

        for j in range(numcol): 

            if blue[i,j] > (int(red[i,j]) + int(green[i,j])): 

                bluePercent += 1 

    bluePercent /= (numrow * numcol) /100

    if tol > bluePercent: 

        savemaybe = 0 

    else: 

        savemaybe = 1 

    print(savemaybe)
    print(bluePercent)
    return savemaybe, bluePercent

#SeeBlue(r"C:\Users\micha\Documents\Virginia Tech\InspireFly\CameraCaptures\earthGlare.jpg" ,0.4)

def SeeBlueAlgorithm(images): 

    tol = 0 

    length = len(images) 

    savemaybeAr = [] 

    for i in range(length): 

        imagei = images[i] 

        savemaybe, bluePercent = SeeBlue(imagei, tol) 

        savemaybeAr.append(savemaybe) 

        if bluePercent > tol: 

            tol = bluePercent 

    IndOne = [index for index, value in enumerate(savemaybeAr) if value == 1] 

    bestPictureInd = IndOne[-1] 

    bestPicture = images[bestPictureInd] 

    print(bestPicture)
    return bestPicture 
#C:/Users/davee/OneDrive/Documents/Python Color Detection Example/earth_low_orbit.jpg
img = [r"C:/Users/davee/OneDrive/Documents/Python Color Detection Example/earth.jpg", r"C:/Users/davee/OneDrive/Documents/Python Color Detection Example/earth_low_orbit.jpg"]
SeeBlueAlgorithm(img)
# 1 is yes, 0 is no 