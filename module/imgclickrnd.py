#coding:utf-8
import cv2
import numpy as np
from PIL import ImageGrab
from time import sleep
import msvcrt
import sys
import random
#import ctypes
from ctypes import *
#from getch import getch, pause



def imgclickrnd(image="mark.bmp",px=0,py=0,imgminx=0,imgminy=0,imgmaxx=0,imgmaxy=0,threshold=0.9):
	def click(posx,posy):
			windll.user32.SetCursorPos(random.randint(posx+px,posx+px+5),random.randint(posy+py,posy+py+5))
			sleep(random.uniform(0.0,0.1))
			windll.user32.mouse_event(0x2,0,0,0,0)
			sleep(random.uniform(0.,0.1))
			windll.user32.mouse_event(0x4,0,0,0,0)


	while True:

		if imgmaxx != 0:
			imgtemp=ImageGrab.grab((imgminx,imgminy,imgmaxx,imgmaxy))
		if imgmaxx == 0:
			imgtemp=ImageGrab.grab()
		cap = np.asarray(imgtemp)
		#img.save("img2.bmp")

		#画像をグレースケールで読み込む
		img = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
		temp = cv2.imread("img\\"+image, 0)
		#マッチングテンプレートを実行
		result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
		#類似度の設定(0~1)
		#threshold = 0.9
		#検出結果から検出領域の位置を取得
	#    loc = np.where(result >= threshold)

		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
		#max_valが類似最大値の左上座標

		if max_val < threshold:
			print(image+"一致せず")

		if max_val >= threshold:
			print(max_loc)
			click (max_loc[0],max_loc[1])
			return



	#ここから先は終了措置ESCキーで終了 F1でPause Cでコンティニュー
		if msvcrt.kbhit(): # キーが押されているか
			kb = msvcrt.getch() # 押されていれば、キーを取得する
			print(kb)
	#        if kb.decode()=='q':
	#       Escキーは\x1b
			if kb.decode()=='\x1b':
				sys.exit()
			if kb.decode()=='\x00':
				sleep(1)
				f=0
				while f==0:
					kb = msvcrt.getch()
					if kb.decode()=='c':
						f=1
					sleep(0.1)

		#繰り返し途中のスリープ
		sleep(0.1)



