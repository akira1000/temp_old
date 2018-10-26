#coding:utf-8
import cv2
import numpy as np
from PIL import ImageGrab


#OpenCVのcv2.imreadは日本語がつかえないなので画像をimedecodeでメモリに一度読み込む
def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img2 = cv2.imdecode(n, flags)
        return img2
    except Exception as e:
        print(e)
        return None


def chkimg(image="mark.bmp",imgminx=0,imgminy=0,imgmaxx=0,imgmaxy=0,threshold=0.8):
	if imgmaxx != 0:
		imgtemp = ImageGrab.grab((imgminx, imgminy, imgmaxx, imgmaxy))
	if imgmaxx == 0:
		imgtemp = ImageGrab.grab()
	Screencap = np.asarray(imgtemp)

	# 画像をグレースケールで読み込む
	Screenimg = cv2.cvtColor(Screencap, cv2.COLOR_BGR2GRAY)

	# 日本語試行錯誤中
	# この下で動く
	finalname = image

	#		temp = cv2.imread(finalname, 0)
	temp = imread(finalname, 0)

	# マッチングテンプレートを実行
	result = cv2.matchTemplate(Screenimg, temp, cv2.TM_CCOEFF_NORMED)
	# threshold = 0.9
	#    loc = np.where(result >= threshold)

	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	# max_valが類似最大値の左上座標

	if max_val < threshold:
			print(image+" 一致せず")
			return (0)
	if max_val >= threshold:
			print(max_loc)
			return (max_loc)
