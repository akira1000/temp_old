#coding:utf-8
from time import sleep
import random
from ctypes import *


def click(posx,posy):
			windll.user32.SetCursorPos(random.randint(posx,posx+5),random.randint(posy,posy+5))
			sleep(random.uniform(0.05,0.1))
			windll.user32.mouse_event(0x2,0,0,0,0)
			sleep(random.uniform(0.01,0.1))
			windll.user32.mouse_event(0x4,0,0,0,0)

