#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import time
import io
import base64
import sys
if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
	import Tkinter
	tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
	import tkinter
from PIL import Image, ImageTk


FRAMESPERSECOND=30

def showPIL(pilImage):
	root = tkinter.Tk()
	screenx, screeny = root.winfo_screenwidth(), root.winfo_screenheight()
	sizex, sizey = screenx*0.9, screeny*0.9
	posx, posy = ((screenx-sizex)/2), ((screeny-sizey)/2)

	root.overrideredirect(1)
	root.geometry("%dx%d+%d+%d" % (sizex, sizey,posx,posy))
	root.focus_set()    
	root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
	canvas = tkinter.Canvas(root,width=screenx,height=screeny)
	canvas.pack()
	canvas.configure(background='black')
	imgWidth, imgHeight = pilImage.size
	if imgWidth > screenx or imgHeight > screeny:
		ratio = min(screenx/imgWidth, screeny/imgHeight)
		imgWidth = int(imgWidth*ratio)
		imgHeight = int(imgHeight*ratio)
		pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
	image = ImageTk.PhotoImage(pilImage)
	imagesprite = canvas.create_image(screenx/2,screeny/2,image=image)
	root.mainloop()



while True:

	file = open("packet.txt", "r")
	data=file.read()
	screenx,screeny,mousex,mousey,img_str=data.split(chr(30))
	img_str=img_str.decode('base64')
	file = open("cirao.png", "wb")	
	file.write(img_str)
	file.close()
	img=Image.open(io.BytesIO(img_str))
	showPIL(img)
	time.sleep(1/FRAMESPERSECOND) # nao sei se é bom
	break;

# pyautogui.moveTo(x, y)