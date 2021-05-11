from m5stack import *
from m5stack_ui import *
from uiflow import *
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


buffer2 = None


label0 = M5Label('UART feedback', x=11, y=10, color=0x000, font=FONT_MONT_14, parent=None)
touch_button0 = M5Btn(text='ECRIT:Hello', x=200, y=10, w=100, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button1 = M5Btn(text='WRITE:Hello', x=200, y=49, w=100, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
touch_button2 = M5Btn(text='TYPEK:0xE3', x=200, y=88, w=100, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
label1 = M5Label('0xE3 = GUI', x=115, y=96, color=0x000, font=FONT_MONT_14, parent=None)
touch_button3 = M5Btn(text='UART ping', x=200, y=128, w=100, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)



def touch_button0_pressed():
  global buffer2
  uart1.write('ECRIT:Hello')
  pass
touch_button0.pressed(touch_button0_pressed)

def touch_button1_pressed():
  global buffer2
  uart1.write('WRITE:Hello')
  pass
touch_button1.pressed(touch_button1_pressed)

def touch_button2_pressed():
  global buffer2
  uart1.write('TYPEK:0xE3')
  pass
touch_button2.pressed(touch_button2_pressed)

def touch_button3_pressed():
  global buffer2
  uart1.write('PING')
  pass
touch_button3.pressed(touch_button3_pressed)


uart1 = machine.UART(1, tx=33, rx=32)
uart1.init(115200, bits=8, parity=None, stop=1)
buffer2 = ''
while True:
  buffer2 = uart1.readline()
  if buffer2:
    buffer2 = buffer2
    label0.set_text(str(str(buffer2.decode())))
    wait(1)
  wait_ms(2)
