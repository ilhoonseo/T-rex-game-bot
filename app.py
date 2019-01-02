import cv2 as cv
import pyautogui
from PIL import ImageGrab
import ctypes
import wx

SP = 0x39

SendInput = ctypes.windll.user32.SendInput
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
# python을 이용한 C 포인터 타입 선언
PUL = ctypes.POINTER(ctypes.c_ulong)
# python을 이용한 키보드 입력 C 구조체 정의
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]
# python을 이용한 하드웨어 입력 C 구조체 정의
class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]
# python을 이용한 마우스 입력 C 구조체 정의
class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]
# python을 이용한 입력 C 유니온 정의
class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]
# python을 이용한 입력 C 구조체 정의
class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# 키 누르기
def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

app = wx.App()
screen = wx.ScreenDC()
bmp = wx.Bitmap(25,25)

while(1):
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, 25, 25, screen, 300, 420)
    del mem
    bmp.SaveFile('wx.bmp', wx.BITMAP_TYPE_BMP)
    img = cv.imread('wx.bmp')
    print(list(img[10,10]))
    if(list(img[10,10])==[83,83,83]):
        print("검출검출검출")
        PressKey(SP)
        
        


