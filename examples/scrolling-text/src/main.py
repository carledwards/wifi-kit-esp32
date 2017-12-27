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

character_bitmap = {
	'a': [
		0b00100,
		0b10001,
		0b11111,
		0b10001,
		0b10001
		],	
	'c': [
		0b11110,
		0b10000,
		0b10000,
		0b10000,
		0b11110
		],	
	'd': [
		0b11110,
		0b10001,
		0b10001,
		0b10001,
		0b11110
		],	
	'i': [
		0b01110,
		0b00100,
		0b00100,
		0b00100,
		0b01110
		],	
	'k': [
		0b10010,
		0b10100,
		0b11000,
		0b10100,
		0b10010
		],	
	'l': [
		0b10000,
		0b10000,
		0b10000,
		0b10000,
		0b11110
		],	
	'm': [
		0b10001,
		0b11011,
		0b10101,
		0b10001,
		0b10001
		],	
	'n': [
		0b10001,
		0b11001,
		0b10101,
		0b10011,
		0b10001
		],
	'o': [
		0b01110,
		0b10001,
		0b10001,
		0b10001,
		0b01110
		],	
	' ': [
		0b00000,
		0b00000,
		0b00000,
		0b00000,
		0b00000
		]	
}

current_segment_column = 4

def draw_segment_slice(y):
	for iy in range(y, y+6):
		oled.pixel(126, iy, 1)

def display_next_segment(char):
	global current_segment_column
	# for each 'pixel' of the character, we draw a 4x5 box
	# one slice at a time, scrolling each slice inwards
	for segment_slice in range(0, 4):
		for row in range(0, 5):
			bitmap_row = character_bitmap[char][row]
			if bitmap_row & (1 << current_segment_column):
				draw_segment_slice(row*13)
		oled.scroll(-1, 0)
		oled.show()

	current_segment_column = current_segment_column - 1
	if current_segment_column < 0:
		current_segment_column = 4

	oled.show()

def scroll_display_left(count=4):
	for i in range(0, count):
		oled.scroll(-1, 0)
		oled.show()

def display_char(char):
	for char_columns in range(0, 5):
		display_next_segment(char)
		scroll_display_left()
	scroll_display_left()
	utime.sleep_us(1)

# clear the screen
oled.fill(0)

while True:
	for word in ['alli', 'nick', 'mom', 'dad', ' ']:
		for char in word:
			display_char(char)
		# add a space between each word
		display_char(' ')
