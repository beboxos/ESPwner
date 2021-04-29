# SPDX-FileCopyrightText: 2017 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_hid.keyboard_layout_us.KeyboardLayoutUS`
=======================================================

* Author(s): Dan Halbert
* Modified by BeBoX 29/04/2021 : French AZERTY layout + methods

"""
class code:
    SHIFT = 0xE1
    ALT = 0xE2
    CTRL = 0xE0
    GUI = 0xE3
    RCTRL = 0xE4
    RSHIFT = 0xE5
    RALT = 0xE6
    RGUI = 0xE7
    MENU = 0x65
    RIGHT = 0x4F
    LEFT = 0x50
    DOWN = 0x51
    UP = 0x52
    TAB = 0x2B
    ESC = 0x29
    ENTER = 0x28
    A = 0x14
    B = 0x05
    C = 0x06
    D = 0x07
    E = 0x08
    F = 0x09
    G = 0x0A
    H = 0x0B
    I = 0x0C
    J = 0x0D
    K = 0x0E
    L = 0x0F
    M = 0x33
    N = 0x11
    O = 0x12
    P = 0x13
    Q = 0x04
    R = 0x15
    S = 0x16
    T = 0x17
    U = 0x18
    V = 0x19
    W = 0x1D
    X = 0x1B
    Y = 0x1C
    Z = 0x1A
    UN = 0x1E
    DEUX = 0x1F
    TROIS = 0x20
    QUATRE = 0x21
    CINQ = 0x22
    SIX = 0x23
    SEPT = 0x24
    HUIT = 0x25
    NEUF = 0x26
    ZERO = 0x27    
class layout:

    SHIFT_FLAG = 0x80
    ASCII_TO_KEYCODE = (
        b"\x00"  # 00 NUL
        b"\x00"  # 01 SOH
        b"\x00"  # 02 STX
        b"\x00"  # 03 ETX
        b"\x00"  # 04 EOT
        b"\x00"  # 05 ENQ
        b"\x00"  # 06 ACK
        b"\x00"  # 07 BEL \a
        b"\x2a"  # 08 BS BACKSPACE \b (called DELETE in the usb.org document)
        b"\x2b"  # 09 TAB \t
        b"\x28"  # 10 LF \n (called Return or ENTER in the usb.org document)
        b"\x00"  # 11 VT \v
        b"\x00"  # 12 FF \f
        b"\x00"  # 13 CR \r
        b"\x00"  # 14 SO
        b"\x00"  # 15 SI
        b"\x00"  # 16 DLE
        b"\x00"  # 17 DC1
        b"\x00"  # 18 DC2
        b"\x00"  # 19 DC3
        b"\x00"  # 20 DC4
        b"\x00"  # 21 NAK
        b"\x00"  # 22 SYN
        b"\x00"  # 23 ETB
        b"\x00"  # 24 CAN
        b"\x00"  # 25 EM
        b"\x00"  # 26 SUB
        b"\x29"  # 27 ESC
        b"\x00"  # 28 FS
        b"\x00"  # 29 GS
        b"\x00"  # 30 RS
        b"\x00"  # 31 US
        b"\x2c"  #- 32 SPACE
        b"\x38"  #* 33 ! 
        b"\x20"  #* 34 " 
        b"\xa0"  #! 35 # x20|SHIFT_FLAG (shift 3) xa0 --- ALTGR+ 0x20 00100000 trouver code ------------------------------------------
        b"\x30"  #* 36 $ 
        b"\xb4"  #* 37 % 
        b"\x1e"  #* 38 & 
        b"\x21"  #* 39 '
        b"\x22"  #* 40 ( 
        b"\x2d"  #* 41 ) 
        b"\x31"  #* 42 * 
        b"\xae"  #- 43 + 
        b"\x10"  #* 44 ,
        b"\x23"  #* 45 -
        b"\xb6"  #* 46 . 
        b"\xb7"  #* 47 / 
        b"\xa7"  #* 48 0 
        b"\x9e"  #* 49 1 
        b"\x9f"  #* 50 2
        b"\xa0"  #* 51 3
        b"\xa1"  #* 52 4
        b"\xa2"  #* 53 5
        b"\xa3"  #* 54 6
        b"\xa4"  #* 55 7
        b"\xa5"  #* 56 8
        b"\xa6"  #* 57 9
        b"\x37"  #* 58 : 
        b"\x36"  #* 59 ;
        b"\xb6"  #! 60 <  ?? keycode meme touche que  0x31 \| tricher en ascii  trouver code ------------------------------------------
        b"\x2e"  #- 61 =
        b"\xb7"  #! 62 >  ?? keycode meme touche que  0x31 \| tricher en ascii  trouver code ------------------------------------------
        b"\x90"  #* 63 ? 
        b"\x9f"  #! 64 @ altGR + x2d trouver code ------------------------------------------
        b"\x94"  #* 65 A 
        b"\x85"  #- 66 B 
        b"\x86"  #- 67 C 
        b"\x87"  #- 68 D 
        b"\x88"  #- 69 E 
        b"\x89"  #- 70 F 
        b"\x8a"  #- 71 G 
        b"\x8b"  #- 72 H 
        b"\x8c"  #- 73 I 
        b"\x8d"  #- 74 J 
        b"\x8e"  #- 75 K 
        b"\x8f"  #- 76 L 
        b"\xb3"  #* 77 M 
        b"\x91"  #- 78 N 
        b"\x92"  #- 79 O 
        b"\x93"  #- 80 P 
        b"\x84"  #* 81 Q 
        b"\x95"  #- 82 R 
        b"\x96"  #- 83 S 
        b"\x97"  #- 84 T 
        b"\x98"  #- 85 U 
        b"\x99"  #- 86 V 
        b"\x9d"  #* 87 W 
        b"\x9b"  #- 88 X 
        b"\x9c"  #- 89 Y 
        b"\x9a"  #* 90 Z 
        b"\x2f"  #! 91 [ ALTGR + 0x22 00100010 trouver code ------------------------------------------
        b"\x31"  #! 92 \ backslash ALTGR + 0x25 00100101 trouver code ------------------------------------------
        b"\x30"  #! 93 ] ALTGR + 0x27 00100111 trouver code ------------------------------------------
        b"\x2f"  #* 94 ^ 
        b"\x25"  #* 95 _ 
        b"\x35"  #! 96 `  ALTGR + 0x24 00100100 trouver code ------------------------------------------
        b"\x14"  #* 97 a
        b"\x05"  #- 98 b
        b"\x06"  #- 99 c
        b"\x07"  #- 100 d
        b"\x08"  #- 101 e
        b"\x09"  #- 102 f
        b"\x0a"  #- 103 g
        b"\x0b"  #- 104 h
        b"\x0c"  #- 105 i
        b"\x0d"  #- 106 j
        b"\x0e"  #- 107 k
        b"\x0f"  #- 108 l
        b"\x33"  #* 109 m
        b"\x11"  #- 110 n
        b"\x12"  #- 111 o
        b"\x13"  #- 112 p
        b"\x04"  #* 113 q
        b"\x15"  #- 114 r
        b"\x16"  #- 115 s
        b"\x17"  #- 116 t
        b"\x18"  #- 117 u
        b"\x19"  #- 118 v
        b"\x1d"  #* 119 w
        b"\x1b"  #- 120 x
        b"\x1c"  #- 121 y
        b"\x1a"  #* 122 z
        b"\xaf"  #! 123 { ALTGR + 0x21 00100001
        b"\xb1"  #! 124 | ALTGR + 0x23 00100011
        b"\xb0"  #! 125 } ALTGR + 0x2E 00101110
        b"\xb5"  #! 126 ~ ALTGR + 0x1F 00011111
        b"\x4c"  #- 127 DEL 
    )

    def __init__(self, keyboard):
        self.keyboard = keyboard
        
    def tape(self, touche):
        self.keyboard.press(touche) 
        self.keyboard.release(touche)

    def presse(self, touche):
        self.keyboard.press(touche)
        
    def relache(self, touche):
        self.keyboard.release(touche)

    def ecrit(self, string):
        for l in string:
            asc='{:0>4}'.format(ord(l)) # met sous forme 0065 pour A par exemple
            if int(asc)<32:
                if int(asc)==13:
                    #return key \r 
                    self.keyboard.press(40) #ENTER
                    self.keyboard.release(40) #ENTER
            else:
                self.keyboard.press(0xE2) #alt press
                for k in asc:
                    if int(k)==0:
                        self.keyboard.press(98) # 0 sur pavé numérique num
                        self.keyboard.release(98)
                    else:
                        self.keyboard.press(88+int(k)) # autres sur pavé num
                        self.keyboard.release(88+int(k))
                self.keyboard.release(0xE2) #alt G release       

    def write(self, string):
        for char in string:
            keycode = self._char_to_keycode(char)
            # If this is a shifted char, clear the SHIFT flag and press the SHIFT key.
            if keycode & self.SHIFT_FLAG:
                keycode &= ~self.SHIFT_FLAG
                self.keyboard.press(0xE1)
            self.keyboard.press(keycode)
            self.keyboard.release_all()

    def keycodes(self, char):
        keycode = self._char_to_keycode(char)
        if keycode & self.SHIFT_FLAG:
            return (0xE1, keycode & ~self.SHIFT_FLAG)

        return (keycode,)

    def _char_to_keycode(self, char):
        char_val = ord(char)
        if char_val > 128:
            raise ValueError("Not an ASCII character.")
        keycode = self.ASCII_TO_KEYCODE[char_val]
        if keycode == 0:
            raise ValueError("No keycode available for character.")
        return keycode
