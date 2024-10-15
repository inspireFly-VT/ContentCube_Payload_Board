def wrapper(command:bytes):
    message = b'\x3C' #'<'
    message = message + command
    message = message + b'\x3E'
    return message

def stripper(command:bytes):
    message = command[1:-1]
    return message