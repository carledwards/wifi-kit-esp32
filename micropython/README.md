# wifi-kit-esp32
Mac OS X Micropython setup instructions and examples for the WiFi Kit 32 Board

![](http://esp32.net/images/Heltec/WIFI-Kit-32/Heltec_WIFI-Kit-32_PhotoDisplay.jpg)

## Prerequisites
1. Using Mac OS X
2. Python 3 is installed and is the default in the path

```shell
% python --version
Python 3.7.6
```


## Setup

1. Install the esptool

	```shell
	% pip3 install esptool 
	% pip3 install esptool --upgrade
	```
	
2. Install Adafruit Micropython Tool (ampy)

	```shell
	% pip3 install adafruit-ampy
	```
	
3. Download the Micropython ESP32 firmware from here: [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/).  The latest version I have tested is: `v1.20.0 (2023-04-26)`

4. Connect the board to the computer.  Verify the USB connection is present.  _Note: the actual name of the USB port may vary depending on the state/firmware version of your ESP32 device._

	```shell
	% ls /dev/tty.usbserial*
	/dev/tty.usbserial-0001
	```

5. Test the communications:

	```shell
	% esptool.py --port /dev/tty.usbserial-0001 flash_id
	esptool.py v4.5.1
	Serial port /dev/tty.usbserial-0001
	Connecting.......
	Detecting chip type... Unsupported detection protocol, switching and trying again...
	Connecting............
	Detecting chip type... ESP32
	Chip is ESP32-D0WDQ6 (revision v1.0)
	Features: WiFi, BT, Dual Core, Coding Scheme None
	Crystal is 26MHz
	MAC: 30:ae:a4:4c:4f:58
	Uploading stub...
	Running stub...
	Stub running...
	Manufacturer: ef
	Device: 4016
	Detected flash size: 4MB
	Hard resetting via RTS pin...
	```
	
	```shell
	% esptool.py --port /dev/tty.usbserial-0001 chip_id
	esptool.py v4.5.1
	Serial port /dev/tty.usbserial-0001
	Connecting......
	Detecting chip type... Unsupported detection protocol, switching and trying again...
	Connecting.........
	Detecting chip type... ESP32
	Chip is ESP32-D0WDQ6 (revision v1.0)
	Features: WiFi, BT, Dual Core, Coding Scheme None
	Crystal is 26MHz
	MAC: 30:ae:a4:4c:4f:58
	Uploading stub...
	Running stub...
	Stub running...
	Warning: ESP32 has no Chip ID. Reading MAC instead.
	MAC: 30:ae:a4:4c:4f:58
	Hard resetting via RTS pin...
	```
	
6. Erase the flash

	```shell
	% esptool.py --chip esp32 --port /dev/tty.usbserial-0001 erase_flash
	esptool.py v4.5.1
	Serial port /dev/tty.usbserial-0001
	Connecting...........
	Chip is ESP32-D0WDQ6 (revision v1.0)
	Features: WiFi, BT, Dual Core, Coding Scheme None
	Crystal is 26MHz
	MAC: 30:ae:a4:4c:4f:58
	Uploading stub...
	Running stub...
	Stub running...
	Erasing flash (this may take a while)...
	Chip erase completed successfully in 9.6s
	Hard resetting via RTS pin...
	```

7. Upload the Micropython firmware

	```shell
	% esptool.py --port /dev/tty.usbserial-0001 write_flash -z 0x1000 ~/Downloads/esp32-20230426-v1.20.0.bin
	esptool.py v4.5.1
	Serial port /dev/tty.usbserial-0001
	Connecting....
	Detecting chip type... Unsupported detection protocol, switching and trying again...
	Connecting.....
	Detecting chip type... ESP32
	Chip is ESP32-D0WDQ6 (revision v1.0)
	Features: WiFi, BT, Dual Core, Coding Scheme None
	Crystal is 26MHz
	MAC: 30:ae:a4:4c:4f:58
	Uploading stub...
	Running stub...
	Stub running...
	Configuring flash size...
	Flash will be erased from 0x00001000 to 0x0017ffff...
	Compressed 1566528 bytes to 1034676...
	Wrote 1566528 bytes (1034676 compressed) at 0x00001000 in 92.0 seconds (effective 136.2 kbit/s)...
	Hash of data verified.

	Leaving...
	Hard resetting via RTS pin...
	```
	
	*_Note: if you receive the error: `A fatal error occurred: The chip stopped responding.`, try re-running the command again._*
	
8. Connect to the board and verify Micropython

	```shell
	screen /dev/tty.usbserial-0001 115200
	```
	Press Enter and you should see the ">>>" Python REPL

	*To soft reboot Python, press "control+d".  you should see a similar output to this:*

	```MPY: soft reboot
	MicroPython v1.20.0 on 2023-04-26; ESP32 module with ESP32
	Type "help()" for more information.
	>>>
	```

	*To exit the screen utility, press "control+a" then "k" and then "y"*

9. Download the OLED SSD1306 python library and unzip: [https://github.com/adafruit/micropython-adafruit-ssd1306](https://github.com/adafruit/micropython-adafruit-ssd1306)

10. Upload the ssd1306 library:

	```shell
	ampy --port /dev/tty.SLAB_USBtoUART put ~/Downloads/micropython-adafruit-ssd1306-master/ssd1306.py
	```

11. Test the OLED display.  While in the REPL connected with the screen utility, enter the following code:

	```python
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

[WIFI Kit 32 Pinout Diagram](http://esp32.net/images/Heltec/WIFI-Kit-32/Heltec_WIFI-Kit-32_DiagramPinout.jpg) (bottom view)

![WIFI Kit 32 Pinout Diagram](http://esp32.net/images/Heltec/WIFI-Kit-32/Heltec_WIFI-Kit-32_DiagramPinout.jpg)

