# 한국방송통신대학 동영상 강의 넘기기

import pyautogui as pgi
import time
import keyboard
import pydirectinput as pyd
import random
print('by 불닭 blog.naver.com/killsonic')
print('"F3" 시작 / "F4" 10초 누르면 종료')

def selectimg(files):    #이미지 찾아서 클릭 함수
    imgfile = pgi.locateCenterOnScreen(files, confidence = 0.8)
    if imgfile == None:
        pass
    else:
        print(imgfile)
        x, y = imgfile
        
        pyd.click(x + 200, y)

def pagedown():
    pgi.press('pgdn')

def imgclick(files):    #이미지 찾아서 클릭 함수
    imgfile = pgi.locateCenterOnScreen(files)
    if imgfile == None:
        pass
    else:
        print(imgfile)
        x, y = imgfile
        pyd.click(x, y)

while True:
    if keyboard.is_pressed('F3'): #작업시작
        print('작업시작')

        while True:
            titleimg1 = pgi.locateCenterOnScreen('title1.png', confidence = 0.8)
            if keyboard.is_pressed('F4'): #F4 중지
                print('중지됨 \n 시작하기 F3')
                break
            elif titleimg1 != None:     #타이틀 이미지가 있는지 없는지 확인
                selectimg('select.png')
                selectimg('select2.png')
                print('학습목록 페이지')
                titleimg1 = None
                time.sleep(3)

                titleimg2 = pgi.locateCenterOnScreen('title2.png', confidence = 0.8)

                if titleimg2 != None:   #타이틀 이미지가 있는지 없는지 확인
                    pagedown()
                    time.sleep(1)
                    imgclick('playbutton.png')
                    time.sleep(1)
                    imgclick('yes.png')
                    time.sleep(1)
                    print('학습하기 페이지')
                    titleimg2 = None
                    while True:
                        checkimg = pgi.locateCenterOnScreen('endvideo.png')    
                        if keyboard.is_pressed('F4'): #F4 중지
                            print('중지됨 \n 시작하기 F3')
                            break
                        elif checkimg == None:
                            print('동영상 시청중 5초대기')
                            time.sleep(5)
                            pgi.moveTo(1, 1)
                            pgi.press('ctrl')
                            pass
                        else:
                            imgclick('close.png')
                            time.sleep(1)
                            imgclick('check.png')
                            time.sleep(1)
                            print('학습종료')
                            time.sleep(3)
                            break
                else:
                    print('학습하기 페이지가 없습니다')
                    pass
            else:
                print('사이트가 없습니다 시작하기 "F3"')    
                break

