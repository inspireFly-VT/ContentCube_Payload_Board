
# Python programs to find 
# unique HSV code for color 
  
# Importing the libraries openCV & numpy 
import cv2 
import numpy as np 
  
# Get green color 
blue = np.uint8([[[255, 0, 0]]]) 
  
# Convert Green color to Green HSV 
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV) 
  
# Print HSV Value for Green color 
print(hsv_blue) 
  
# Make python sleep for unlimited time 
cv2.waitKey(0) 