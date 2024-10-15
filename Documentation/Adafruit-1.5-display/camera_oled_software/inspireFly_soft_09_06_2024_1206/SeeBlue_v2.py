
#Use something other than cv2
import cv2
import numpy as np

def See_Blue(jpg_file):

    img = cv2.imread(jpg_file)

    # Scale your BIG image into a small one:
    scalePercent = 0.5

    # Calculate the new dimensions
    width = int(img.shape[1] * scalePercent)
    height = int(img.shape[0] * scalePercent)
    newSize = (width, height)

    # Resize the image:
    image = cv2.resize(img, newSize, None, None, None, cv2.INTER_AREA)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array([100, 40, 40])			#The lower blue threshold for lighter blues 
    upper = np.array([140, 255, 255])		#The upper threshold for more saturated blues

    mask = cv2.inRange(hsv, lower, upper)

    ratio_blue = cv2.countNonZero(mask)/(image.size/3)
    colorPercent = (ratio_blue * 100)

    #Images tagged 1 will be transmitted to ground control, else they will be handled some other way.
    if colorPercent >= 40:
        tag = "TRANSFER"
        
        
    else:
        tag = "NO TRANSFER"

    return colorPercent, tag

#Below, include the paths for the images taken by the cube sat. Will likely be a standardized path with a counter of sorts.
img_paths = ["blue.jpg", "inspireFly_Capture_1.jpg", "earth_low_blue.jpg", "earth_low_orbit.jpg", "earth.jpg"]

for path in img_paths:
    percent_blue, tag = See_Blue(path)
    print(f"Image '{path}' has {percent_blue:.4f}% blue and tagged as: {tag}")
