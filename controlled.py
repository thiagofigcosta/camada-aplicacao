#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import time
import io
import base64

FRAMESPERSECOND=30


while True:
	screenx,screeny= pyautogui.size()
	mousex,mousey= pyautogui.position()
	img=pyautogui.screenshot()

	with io.BytesIO() as output:
		img.save(output, format="PNG")
		img_str = base64.b64encode(output.getvalue())
	data=str(screenx)+chr(30)+str(screeny)+chr(30)+str(mousex)+chr(30)+str(mousey)+chr(30)+img_str
	file = open("packet.txt", "wb")
	file.write(data)
	file.close()


		# file.write(str.decode('base64')) //decode str
		


	time.sleep(1/FRAMESPERSECOND)




	