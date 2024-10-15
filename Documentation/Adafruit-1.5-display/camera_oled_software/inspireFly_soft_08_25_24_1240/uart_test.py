from easy_comms import Easy_comms
from time import sleep
import uart_packer
from ssd1351 import Display
from machine import Pin, SPI
from camera_commands import TakeMultiplePictures
from Camera import *

# screen setup
spi_screen = SPI(0, baudrate=14500000, sck=Pin(18), mosi=Pin(19))  # Using machine.SPI directly
display = Display(spi_screen, dc=Pin(14), cs=Pin(21), rst=Pin(7))  # Adjust pin assignments

# camera setup
spi_cam = SPI(1,sck=Pin(10), miso=Pin(8), mosi=Pin(11), baudrate=8000000)
cs = Pin(9, Pin.OUT)
# button = Pin(15, Pin.IN,Pin.PULL_UP)
onboard_LED = Pin(25, Pin.OUT)
cam = Camera(spi_cam, cs)

#uart bus setup
com1 = Easy_comms(uart_id=0, baud_rate=9600)

#Received Command Definitions
activate = b'\x11'
shutdown = b'\x22' 
takePicture = b'\x33'
sendPicture = b'\x44'

#Sending Command Definitions
payloadOn = b'\x99'
payloadOff = b'\x88'
pictureTaken = b'\x77'
pictureSent = b'\x66'

while True:
    receivedCommand = uart_packer.stripper(com1.read_bytes())
    print(receivedCommand)
    if receivedCommand == activate:
        print("turning screen on")
        display.display_on()
        display.draw_image('RaspberryPiWB128x128.raw', 0, 0, 128, 128)
        com1.send_bytes(uart_packer.wrapper(payloadOn))
    elif receivedCommand == shutdown:
        print("turning screen off")
        display.display_off()
        com1.send_bytes(uart_packer.wrapper(payloadOff))
    elif receivedCommand == takePicture:
        print("taking picture")
        TakeMultiplePictures('inspireFly_Capture', '640x480', 500, 2, cam)
        com1.send_bytes(uart_packer.wrapper(pictureTaken))
    elif receivedCommand == sendPicture:
        print("sending picture")
        com1.send_bytes(uart_packer.wrapper(pictureSent))
    else:
        print("unknown command")
                        