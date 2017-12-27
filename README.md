# wifi-kit-32
Mac OS X Setup instructions and examples for the WiFi Kit 32 Board

![](http://esp32.net/images/Heltec/WIFI-Kit-32/Heltec_WIFI-Kit-32_PhotoDisplay.jpg)

## Setup

1. Install the esptool

	```
	% pip install esptool 
	% pip install esptool --upgrade
	```
1. Install Adafruit Micropython Tool (ampy)

	```
	% pip install adafruit-ampy
	```
1. Download the Micropython ESP32 firmware from here: [https://micropython.org/download#esp32](https://micropython.org/download#esp32)

1. Connect the board to the computer.  Verify the USB connection is present:

	```
	% ls /dev/tty.SLAB*
	/dev/tty.SLAB_USBtoUART
	```

1. Test the communications:

	```
	% esptool.py --port /dev/tty.SLAB_USBtoUART flash_id
	esptool.py v2.2
	Connecting........_____..
	Detecting chip type... ESP32
	Chip is ESP32D0WDQ6 (revision 1)
	Uploading stub...
	Running stub...
	Stub running...
	Manufacturer: ef
	Device: 4016
	Detected flash size: 4MB
	Hard resetting…
	```
	
	```
	% esptool.py --port /dev/tty.SLAB_USBtoUART chip_id
	esptool.py v2.2
	Connecting........_
	Detecting chip type... ESP32
	Chip is ESP32D0WDQ6 (revision 1)
	Uploading stub...
	Running stub...
	Stub running...
	Chip ID: 0xcb30aea44c4f
	Hard resetting…
	```
1. Erase the flash

	```
	% esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash
	```	

1. Upload the Micropython firmware

	```
	% esptool.py --port /dev/tty.SLAB_USBtoUART write_flash -z 0x1000 ~/Downloads/esp32-20171226-v1.9.3-217-g5de064fb.bin
	```
	
1. Connect to the board and verify Micropython

	```
	screen /dev/tty.SLAB_USBtoUART 115200
	```

1. Download the OLED SSD1306 python library and unzip: [https://github.com/adafruit/micropython-adafruit-ssd1306](https://github.com/adafruit/micropython-adafruit-ssd1306)

1. Upload the ssd1306 library:

	```
	ampy --port /dev/tty.SLAB_USBtoUART put ~/Downloads/micropython-adafruit-ssd1306-master/ssd1306.py
	```

1. Test the OLED display:

	```
	import machine, ssd1306
	from machine import Pin
	
	# pull the OLED_RST pin HIGH
	oled_rst = Pin(16, Pin.OUT)
	oled_rst.value(1)
	
	# Connect to the board
	i2c = machine.I2C(scl=machine.Pin(15), sda=machine.Pin(4))
	oled = ssd1306.SSD1306_I2C(128, 64, i2c)
	
	# Display text
	oled.text('Hello World', 0, 0)
	oled.show()
	```

## Reference

[WIFI Kit 32 Pinout Diagram](http://esp32.net/images/Heltec/WIFI-Kit-32/Heltec_WIFI-Kit-32_DiagramPinout.jpg)

![WIFI Kit 32 Pinout Diagram](http://esp32.net/images/Heltec/WIFI-Kit-32/Heltec_WIFI-Kit-32_DiagramPinout.jpg)

