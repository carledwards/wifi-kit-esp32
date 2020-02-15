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

#
# Seven Segment Mapping
#
#      a
#    -----
# f |     | b
#   |  g  |
#    -----
# e |     | c
#   |     |
#    -----
#      d
#
segment_map = {
#         a  b  c  d  e  f  g
	'0': [1, 1, 1, 1, 1, 1, 0],
	'1': [0, 1, 1, 0, 0, 0, 0],
	'2': [1, 1, 0, 1, 1, 0, 1],
	'3': [1, 1, 1, 1, 0, 0, 1],
	'4': [0, 1, 1, 0, 0, 1, 1],
	'5': [1, 0, 1, 1, 0, 1, 1],
	'6': [1, 0, 1, 1, 1, 1, 1],
	'7': [1, 1, 1, 0, 0, 0, 0],
	'8': [1, 1, 1, 1, 1, 1, 1],
	'9': [1, 1, 1, 1, 0, 1, 1],
}

def display_segment(x, y, character, size=1, show=True):
	segment_bitmap = segment_map[character]
	segment_length = 5*size
	spacing = size - 1
	for offset_x in range(1,segment_length):
		# segment 'a'
		oled.pixel(x + offset_x, y, segment_bitmap[0])
		# segment 'g'
		oled.pixel(x + offset_x, y + segment_length + (spacing * 2), segment_bitmap[6])
		# segment 'd'
		oled.pixel(x + offset_x, y + (segment_length*2) + (spacing * 4), segment_bitmap[3])
	for offset_y in range(1, segment_length):
		# segment 'f'
		oled.pixel(x, y + offset_y + (spacing * 1), segment_bitmap[5])
		# segment 'b'
		oled.pixel(x + segment_length, y + offset_y + (spacing * 1), segment_bitmap[1])
		# segment 'e'
		oled.pixel(x, y + segment_length + offset_y + (spacing * 3), segment_bitmap[4])
		# segment 'c'
		oled.pixel(x + segment_length, y + segment_length + offset_y + (spacing * 3), segment_bitmap[2])
	if show:
		oled.show()

# clear the screen
oled.fill(0)

# display 0123456789
width = 9
for digit in range(0, 10):
	display_segment(digit * width, 1, str(digit))

# display 0-9 in 3 different sizes
while True:
	for digit in range(0, 10):
		display_segment(0, 20, str(digit), size=1, show=False)
		display_segment(15, 20, str(digit), size=2, show=False)
		display_segment(35, 20, str(digit), size=3)
		utime.sleep(.2)

