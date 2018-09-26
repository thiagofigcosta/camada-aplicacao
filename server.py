#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import time


FRAMESPERSECOND=30


while True:
	print pyautogui.size()
	print pyautogui.position()
	print pyautogui.screenshot()
	time.sleep(1/FRAMESPERSECOND)