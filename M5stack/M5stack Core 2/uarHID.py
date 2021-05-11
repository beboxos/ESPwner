# UART HID library by BeBoX (c) 2021
# ----------------------------------
# 
# Keyboard COMMANDS over UART
# PRESS:keycode : press   key              ex. PRESS:0x2c
# RLEAS:keycode : release key              ex. RLEAS:0x2c
# TYPEK:keycode : press ans release key    ex. TYPEK:0x2c
# WRITE:String  : type a string            ex. WRITE:Hello World!
# ECRIT:String  : type a string            ex. WRITE:Hello World! method ALTGR + ascii code (seem to work only in windows)
# Mouse Commands
# MMOVE:x,y,wheel                          ex. MMOVE:x=-10,y=2
# MCLIC:button (1,2 or 4)                  ex. MCLIC:1   1= LEFT button
# MPRES:button (1,2 or 4)                  ex. MPRES:2   2= RIGHT button
# MRLEA:button (1,2 or 4)                  ex. MRLEA:2   4= Wheel button
# ---------------------------------
import time

def uart_command(command):
    response = ""
    uart1.write(command)
    time.sleep(0.5) # wait 500 ms
    response = uart1.readline()
    if response=="":
        response="Time out"
    return response

def uart_type(keycode):
    # Press and release a key
    uart1.write('TYPEK:' + keycode)
def uart_press(keycode):
    # Press a key
    uart1.write('PRESS:' + keycode)
def uart_release(keycode):
    # Release a key
    uart1.write('RLEAS:' + keycode)
def uart_write(text):
    # Write a String
    uart1.write('WRITE:' + text)
def uart_ecrit(text):
    # Write a String with ALTGR + ascii code from numeric pad ex ALTGR + 0065
    uart1.write('ECRIT:' + text)


