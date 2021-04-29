import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
import keybfr
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = keybfr.layout(keyboard)  # nous on est en France :)

#time.sleep(2) # on se laisse 2 seconde pour cliquer ailleurs
texte = "Hello World!"
keyboard_layout.presse(keybfr.code.GUI)
keyboard_layout.tape(keybfr.code.R)
keyboard_layout.relache(keybfr.code.GUI)
time.sleep(0.5)
keyboard_layout.write("notepad.exe")
keyboard_layout.tape(keybfr.code.ENTER)
time.sleep(1)
keyboard_layout.ecrit(texte)
time.sleep(1)
keyboard_layout.tape(keybfr.code.ENTER)
keyboard_layout.write(texte)
