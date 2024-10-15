# Pico_comms_a
# Sends commands and listens to responses from pico_comms_b

from easy_comms import Easy_comms
from time import sleep
import binascii

com1 = Easy_comms(uart_id=0, baud_rate=9600)
#com1.start()

# Open the image file in binary mode
with open('inspireFly_Capture_#4.jpg', 'rb') as img_file:
    img_data = img_file.read()

# Convert the image data to hexadecimal
hex_img_data = binascii.hexlify(img_data)

while True:
    # Send the image data
    com1.send(hex_img_data)
    
    com1.sent()
    # Listen for responses
    message = com1.read()
    
    if message is not None:
        print(f"message received: {message.strip('\n')}")
    sleep(1)
