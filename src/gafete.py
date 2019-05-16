
from ili934xnew import ILI9341, color565
from machine import Pin, SPI
import tt14
import glcdfont
import tt14
import tt24
import tt32
import xeron36

fonts = [glcdfont,tt14,tt24,tt32,xeron36]

spi = SPI(miso=Pin(12), mosi=Pin(13, Pin.OUT), sck=Pin(14, Pin.OUT))

display = ILI9341(
    spi,
    cs=Pin(15),
    dc=Pin(5),
    rst=Pin(4),
    width=240,
    height=320,
    mirror=False)
display.erase()
display.set_pos(0,0)

display.set_font(fonts[4])
display.print("Steven")
display.print("Silva")
display.set_font(fonts[3])
display.print(" ")
display.print("FunPython Member")
