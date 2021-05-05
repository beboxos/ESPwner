# only for AZERTY 
# UART to HID GATEWAY
# By BeBoX (c)2021
import busio
import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
import keybfr
keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)
k = keybfr.layout(keyboard)
uart = busio.UART(board.TX, board.RX, baudrate=115200)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True # OFF
# Keyboard COMMANDS over UART
# PRESS:keycode : press   key              ex. PRESS:0x2c
# RLEAS:keycode : release key              ex. RLEAS:0x2c
# TYPEK:keycode : press ans release key    ex. TYPEK:0x2c
# WRITE:String  : type a string            ex. WRITE:Hello World!
# ECRIT:String  : type a string            ex. WRITE:Hello World! method ALTGR + ascii code (seem to work only in windows)
# Mouse Commands
# MMOVE:x,y,wheel                          ex. MMOVE:x=-10,y=2
# MCLIC:button (1,2 or 4)                  ex. MCLIC:1
# MPRES:button (1,2 or 4)                  ex. MPRES:2
# MRLEA:button (1,2 or 4)                  ex. MRLEA:2

while True:
    led.value = True
    data=uart.readline()
    if data is not None:
        led.value = False
        data_string= ''.join([chr(b) for b in data])
        if data_string[:4]=="PING":
            try:
                print("PONG")
                uart.write(b'PONG')
            except:
                print("PONG ERROR")
                uart.write(b'NO')        
        if data_string[:5]=="PRESS":
            try:
                k.presse(int(data_string[6:]))
                uart.write(b'OK')
            except:
                print("PRESS ERROR")
                uart.write(b'NO')
        if data_string[:5]=="RLEAS":
            try:
                k.relache(int(data_string[6:]))
                uart.write(b'OK')
            except:
                print("RLEAS ERROR")
                uart.write(b'NO')                
        if data_string[:5]=="TYPEK":
            try:
                k.tape(int(data_string[6:]))
                uart.write(b'OK')
            except:
                print("TYPEK ERROR")
                uart.write(b'NO')            
        if data_string[:5]=="ECRIT":
            try:
                k.ecrit(data_string[6:])
                uart.write(b'OK')
            except:
                print("ECRIT ERROR")
                uart.write(b'NO')
        if data_string[:5]=="WRITE":
            try:
                k.write(data_string[6:])
                uart.write(b'OK')
            except:
                print("WRITE ERROR")
                uart.write(b'NO')
        # Mouse part
        # MCLIC:button (1,2 or 4)                  ex. MCLIC:1
        if data_string[:5]=="MCLIC":
            try:
                mouse.click(int(data_string[6:]))
                uart.write(b'OK')
            except:
                print("MCLIC ERROR")
                uart.write(b'NO')
        # MMOVE:x,y,wheel                          ex. MMOVE:x=-10,y=2
        if data_string[:5]=="MMOVE":
            try:
                mouse.move(data_string[6:])
                uart.write(b'OK')
            except:
                print("MMOVE ERROR")
                uart.write(b'NO')
        # MPRES:button (1,2 or 4)                  ex. MPRES:2
        if data_string[:5]=="MPRES":
            try:
                mouse.press(int(data_string[6:]))
                uart.write(b'OK')
            except:
                print("MPRES ERROR")
                uart.write(b'NO')
        # MRLEA:button (1,2 or 4)                  ex. MRLEA:2
        if data_string[:5]=="MRLEA":
            try:
                mouse.release(int(data_string[6:]))
                uart.write(b'OK')
            except:
                print("MRLEA ERROR")
                uart.write(b'NO')