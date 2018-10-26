#coding:utf-8
import cv2
import numpy as np
from PIL import ImageGrab


def chkimg(image="mark.bmp",imgminx=0,imgminy=0,imgmaxx=0,imgmaxy=0,threshold=0.8):


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
			return (0)
		if max_val >= threshold:
			print(max_loc)
			return (max_loc)
