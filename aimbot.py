import numpy as np
from PIL import ImageGrab
import cv2, keyboard
from ctypes import windll

def screen_record(): 
	#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	bot_cascade = cv2.CascadeClassifier('target.xml')
	screen_height = 1080
	screen_width = 960
	sensitivity = 2.5
	
	while(True):
		img = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0, 0, screen_height, screen_width))), cv2.COLOR_RGB2BGR)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		bots = bot_cascade.detectMultiScale(gray, minNeighbors=40)

		for (x,y,w,h) in bots:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

		cv2.imshow('img', img)
		cv2.waitKey(1)
		
		if keyboard.is_pressed('esc'): # quit while loop
			print("breaking")
			break
		elif keyboard.is_pressed('l') and type(bots) == np.ndarray: # check if key is pressed and bots are detected
			bot_center = (bots[0][0] + bots[0][2] / 2, bots[0][1] + bots[0][3] / 2)
			rec_screen_center = (screen_width / 2, screen_height / 2)
			windll.user32.mouse_event(0x0001, int((bot_center[0] - rec_screen_center[0]) * sensitivity), int((bot_center[1] - rec_screen_center[1]) * sensitivity), 0,0) 

	img.release()
	cv2.destroyAllWindows()