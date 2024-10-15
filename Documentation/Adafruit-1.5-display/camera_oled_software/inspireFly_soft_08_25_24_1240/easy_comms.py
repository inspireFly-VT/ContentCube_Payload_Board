from machine import UART, Pin
from time import time_ns

class Easy_comms:
 
    uart_id = 0
    baud_rate = 9600
    timeout = 5*10^9#10000
    
    def __init__(self, uart_id: int, baud_rate: int = None):
        self.uart_id = uart_id
        if baud_rate: 
            self.baud_rate = baud_rate
        # Set the baud rate
        self.uart = UART(self.uart_id, self.baud_rate)
        # Initialise the UART serial port
        self.uart.init()            
    
    def send_bytes(self, data: bytes):
#         print("Sending bytes...")
        self.uart.write(data)
        
    def start(self):
        message = "ahoy\n"
        print(message)

    def read_bytes(self) -> bytes:
        start_time = time_ns()
        current_time = start_time
        message = b""
        count = 1; #new
        chunksize = 255
        while current_time <= (start_time + self.timeout):
            while self.uart.any() > 0:
                message += self.uart.read(chunksize)
                current_time = time_ns()
                count = count + 1 #new
                
        if len(message) > 0:
            return message#, count #,count added
        else:
            return None
        
    def overhead_send(self, message: bytes):
        print(f'Sending Message: {message}...')
        message = message + '\n'
        self.uart.write(bytes(message,'utf-8'))
               
    def overhead_read(self)->str:
        start_time = time_ns()
        current_time = start_time
        new_line = False
        message = ""
        while (not new_line) or (current_time <= (start_time + self.timeout)):
            if (self.uart.any() > 0):
                message = message + self.uart.read().decode('utf-8')
                if '\n' in message:
                    new_line = True
                    message = message.strip('\n')
                    # print(f'received message: {message}')
                    return message
                else:
                        return None

            