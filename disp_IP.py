#Modified script to display IP address of Wifi-connection on jetbot display on startup
#==================================================================================
import netifaces as ni



import time
import os 

# For Jetson Hardware
import subprocess


# For Adafruit Hardware
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Initialize Display-----------------------------------------------------------
# Try to connect to the OLED display module via I2C.

# 128x32 display (default)---------------------------------------------
disp1 = Adafruit_SSD1306.SSD1306_128_32(rst=None, i2c_bus=1, gpio=1) # setting gpio to 1 is hack to avoid platform detection
try:
	# Initiallize Display
	disp1.begin()

	# Clear display.
	disp1.clear()
	disp1.display()
	
	# Create blank image for drawing.
	# Make sure to create image with mode '1' for 1-bit color.
	width = disp1.width
	height = disp1.height
	image = Image.new('1', (width, height))

	# Get drawing object to draw on image.
	draw = ImageDraw.Draw(image)

	# Draw a black filled box to clear the image.
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	# Draw some shapes.
	# First define some constants to allow easy resizing of shapes.
	padding = -2
	top = padding
	bottom = height-padding
	# Move left to right keeping track of the current x position for drawing shapes.
	x = 0

	# Load default font.
	font = ImageFont.load_default()

	# Draw a black filled box to clear the image.
	draw.rectangle((0,0,width,height), outline=0, fill=0)
except OSError as err:
	print("OS error: {0}".format(err))
	time.sleep(5)
	

while True:
	try:
		ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
		break
	
	except KeyError as err:
		time.sleep(1)
		
draw.text((x, top),       ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr'],  font=font, fill=255)
				
# Display image.
disp1.image(image)
disp1.display()



