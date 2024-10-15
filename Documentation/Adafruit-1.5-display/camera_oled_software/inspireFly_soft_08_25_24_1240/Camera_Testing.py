from machine import Pin, SPI
from Camera import *
import os
spi = SPI(0,sck=Pin(18), miso=Pin(16), mosi=Pin(19), baudrate=8000000)
cs = Pin(17, Pin.OUT)
# button = Pin(15, Pin.IN,Pin.PULL_UP)
onboard_LED = Pin(25, Pin.OUT)
cam = Camera(spi, cs)

def TakePicture(imageName, resolution):
    onboard_LED.on()
    finalImageName = imageName
    if not '.jpg' in finalImageName:
        finalImageName = finalImageName + '.jpg'
    cam.resolution = resolution
    #Kept getting an error saying to add 500ms of delay
    sleep_ms(500)
    cam.capture_jpg()
    sleep_ms(500)
    cam.saveJPG(finalImageName)
    onboard_LED.off()

def TakeMultiplePictures(imageName, resolution, interval, count):
    cam.resolution = resolution
    for x in range(count):
        if x!=0:
            endImageName = imageName + str(x + 1) + '.jpg'
            try:
                uos.remove(endImageName)
            except:
                print("File does not exist")
    for x in range(count): 
        endImageName = imageName + str(x + 1) + '.jpg'
        TakePicture(endImageName, resolution)
        sleep_ms(500)
        if x==0:
            uos.remove(endImageName)
        sleep_ms(interval)
      
#Not sure what default values to use
#cam.resolution = '640x480'
#cam.set_brightness_level(brightness)
#cam.set_filter(effect)
#cam.set_saturation_control(saturation_value)
#set_contrast(contrast)
#set_white_balance(environment)

'''
#Choose function to run below
#For TakePicture, include image name and resolution

#For TakeMultiplePictures, include image name, resolution, interval(ms), then number of pictures

#When the LED is on it is taking the picture
'''
##########################################
#TakePicture('Final Test', '640x480')
TakeMultiplePictures('Test_Images', '640x480', 500, 2)
##########################################
'''
Valid 3MP Resolutions
320x240
640x480
1280x720
1600x1200
1920x1080
2048x1536
96X96
128X128
320X320


Valid 5MP Resolutions
320x240
640x480
1280x720
1600x1200
1920x1080
2592x1944
96X96
128X128
320X320


Other camera functions to potentially add to the functions
# cam.set_brightness_level(brightness)

# cam.set_filter(effect)

# cam.set_saturation_control(saturation_value)

# set_contrast(contrast)

# set_white_balance(environment)

Valid values for above functions:

Brightness:
    BRIGHTNESS_MINUS_4 = 8
    BRIGHTNESS_MINUS_3 = 6
    BRIGHTNESS_MINUS_2 = 4
    BRIGHTNESS_MINUS_1 = 2
    BRIGHTNESS_DEFAULT = 0
    BRIGHTNESS_PLUS_1 = 1
    BRIGHTNESS_PLUS_2 = 3
    BRIGHTNESS_PLUS_3 = 5
    BRIGHTNESS_PLUS_4 = 7

Filter:
    SPECIAL_NORMAL = 0x00
    SPECIAL_COOL = 1
    SPECIAL_WARM = 2
    SPECIAL_BW = 0x04
    SPECIAL_YELLOWING = 4
    SPECIAL_REVERSE = 5
    SPECIAL_GREENISH = 6
    SPECIAL_LIGHT_YELLOW = 9 # 3MP Only

Saturation:
    SATURATION_MINUS_3 = 6
    SATURATION_MINUS_2 = 4
    SATURATION_MINUS_1 = 2
    SATURATION_DEFAULT = 0
    SATURATION_PLUS_1 = 1
    SATURATION_PLUS_2 = 3
    SATURATION_PLUS_3 = 5
    
Contrast:
    CONTRAST_MINUS_3 = 6
    CONTRAST_MINUS_2 = 4
    CONTRAST_MINUS_1 = 2
    CONTRAST_DEFAULT = 0
    CONTRAST_PLUS_1 = 1
    CONTRAST_PLUS_2 = 3
    CONTRAST_PLUS_3 = 5

White Balance:
    WB_MODE_AUTO = 0
    WB_MODE_SUNNY = 1
    WB_MODE_OFFICE = 2
    WB_MODE_CLOUDY = 3
    WB_MODE_HOME = 4

Exposure: (Note, there is no set_exposure_value function in the code)
    EXPOSURE_MINUS_3 = 6
    EXPOSURE_MINUS_2 = 4
    EXPOSURE_MINUS_1 = 2
    EXPOSURE_DEFAULT = 0
    EXPOSURE_PLUS_1 = 1
    EXPOSURE_PLUS_2 = 3
    EXPOSURE_PLUS_3 = 5

Sharpness: (Note, there is no set_sharpness_value function in the code)
    SHARPNESS_NORMAL = 0
    SHARPNESS_1 = 1
    SHARPNESS_2 = 2
    SHARPNESS_3 = 3
    SHARPNESS_4 = 4
    SHARPNESS_5 = 5
    SHARPNESS_6 = 6
    SHARPNESS_7 = 7
    SHARPNESS_8 = 8
'''
