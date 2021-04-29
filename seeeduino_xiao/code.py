# only for AZERTY 
# UART to HID GATEWAY
# By BeBoX (c)2021
import busio
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
import keybfr
keyboard = Keyboard(usb_hid.devices)
k = keybfr.layout(keyboard)
uart = busio.UART(board.TX, board.RX, baudrate=115200)
# Keyboard COMMANDS over UART
# PRESS:keycode : press   key              ex. PRESS:0x2c
# RLEAS:keycode : release key              ex. RLEAS:0x2c
# TYPEK:keycode : press ans release key    ex. TYPEK:0x2c
# WRITE:String  : type a string            ex. WRITE:Hello World!
while True:
    data=uart.readline()
    if data is not None:
        data_string= ''.join([chr(b) for b in data])
        if data_string[:5]=="PRESS":
            try:
                k.presse(data_string[6:])
                uart.write(b'OK')
            except:
                uart.write(b'NO')
        if data_string[:5]=="RLEAS":
            try:
                k.relache(data_string[6:])
                uart.write(b'OK')
            except:
                uart.write(b'NO')                
        if data_string[:5]=="TYPEK":
            try:
                k.tape(data_string[6:])
                uart.write(b'OK')
            except:
                uart.write(b'NO')            
        if data_string[:5]=="WRITE":
            try:
                k.ecrit(data_string[6:])
                uart.write(b'OK')
            except:
                uart.write(b'NO')            