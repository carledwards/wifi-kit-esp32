import machine, ssd1306
from machine import Pin
import utime

#
# requires Adafruit OLED SSD1306 Library: https://github.com/adafruit/micropython-adafruit-ssd1306
#

oled_rst = Pin(16, Pin.OUT)
oled_rst.value(1)
i2c = machine.I2C(scl=machine.Pin(15), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)

def draw_square(top_left_x, top_left_y, width, height, col):
	for x in range (top_left_x, top_left_x + width):
		oled.pixel(x, top_left_y, col)
		oled.pixel(x, top_left_y + height, col)
	for y in range (top_left_y, top_left_y + height):
		oled.pixel(top_left_x, y, col)
		oled.pixel(top_left_x + width, y, col)

while True:
	y = 0
	for x in range(0, 31):
		# outer square
		y = int(x * .5)
		draw_square(x, y, 127-(x*2), 63-(y*2), 1)

		# inner square
		x2 = x+31
		y2 = int(x2 * .5)
		draw_square(x2, y2, 127-(x2*2), 63-(y2*2), 1)

		# center squary
		if x == 0:
			draw_square(62, 31, 3, 1, 1)

		# update the display
		oled.show()

		# clear the squares, getting ready for the next ones to be drawn
		draw_square(x, y, 127-(x*2), 63-(y*2), 0)
		draw_square(x2, y2, 127-(x2*2), 63-(y2*2), 0)
		if x == 0:
			draw_square(62, 31, 3, 1, 0)

		# give a little bit of time back to the system
		# makes for uploading code more reliable
		utime.sleep_us(1)
