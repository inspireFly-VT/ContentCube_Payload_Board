from time import sleep_ms
from ssd1351 import Display
from machine import Pin, SPI
from Camera import *
import os

spi = SPI(0, baudrate=14500000, sck=Pin(18), mosi=Pin(19))  # Using machine.SPI directly
display = Display(spi, dc=Pin(14), cs=Pin(21), rst=Pin(7))  # Adjust pin assignments

print("Displaying image...")
display.draw_image('RaspberryPiWB128x128.raw', 0, 0, 128, 128)

spi = SPI(1, sck=Pin(10), miso=Pin(8), mosi=Pin(11), baudrate=8000000)
cs = Pin(9, Pin.OUT)
onboard_LED = Pin(25, Pin.OUT)
cam = Camera(spi, cs)

# Read the last number used from the file
try:
    with open('last_num.txt', 'r') as f:
        last_num = int(f.read())
except OSError:
    # If the file doesn't exist, start from 1
    last_num = 1

def TakePicture(imageName, resolution):
    print("Initializing TakePicture")
    onboard_LED.on()
    finalImageName = imageName
    # Add the number to the image name
    finalImageName += '.jpg'
    print("Setting resolution...")
    cam.resolution = resolution
    print("Resolution set")
    sleep_ms(500)

    cam.capture_jpg()
    print("Image Captured")
    sleep_ms(500)
    cam.saveJPG(finalImageName)
    onboard_LED.off()
    # Increment the number and write it back to the file
    with open('last_num.txt', 'w') as f:
        f.write(str(last_num + 1))

def TakeMultiplePictures(imageName, resolution, interval, count):
    print("Setting resolution...")
    cam.resolution = resolution
    print("Resolution set.")
    for x in range(count):
        endImageName = imageName + str(last_num)  # Generate filename with only number
        TakePicture(endImageName, resolution)
        sleep_ms(500)
        if x == 0:  # If it's the first image
            try:
                os.remove(endImageName + '.jpg')  # Delete the first image
            except OSError:
                print("Error removing file:", endImageName + '.jpg')
        sleep_ms(interval)
        print("Multiple Pictures Taken")
     
count = (last_num + 2) - last_num
print("Initiating TakeMultiplePictures...")
TakeMultiplePictures('inspireFly_Capture_', '320x240', 500, count)


#Display taken image on OLED
#print("Displaying image...")
#display.draw_image('inspireFly_Capture_' + str(last_num) + '.jpg', 0, 0, 128, 128)
