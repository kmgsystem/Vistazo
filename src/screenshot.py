import win32gui, win32ui, win32con, win32api
import os, sys
import time

def makeScreenshot(obj, width, height, left, top, name= ("desktop" + time.strftime("%a-%b-%d-%H-%M-%S"))):
    srcdc = win32ui.CreateDCFromHandle(obj)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    bmp.SaveBitmapFile(memdc, name + ".bmp")


def desktopScreenShot(name=("window" + time.strftime("%a-%b-%d-%H-%M-%S"))):

    hwin = win32gui.win32gui.GetDesktopWindow()
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    hwindc = win32gui.GetWindowDC(hwin)
    makeScreenshot(hwindc, width, height, left, top, name)

def windowScreenShot(name=("window" + time.strftime("%a-%b-%d-%H-%M-%S"))):

    hwin = win32gui.GetWindow(win32gui.GetForegroundWindow(), 4)
    left, top, width, height  = win32gui.GetClientRect(win32gui.GetForegroundWindow())
    hwindc = win32gui.GetWindowDC(hwin)
    print(width, height, left, top)
    makeScreenshot(hwindc, width, height, left, top, name)

if __name__ == "__main__":
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), 11)
    win32gui.SetActiveWindow(win32gui.GetForegroundWindow())
    os.chdir(os.path.expanduser("~"))
    windowScreenShot()
