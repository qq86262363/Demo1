import win32gui
import win32api
import PIL
classname = "Qt5QWindowIcon"
titlename = "逍遥安卓 2.9.6 - MEmu"
#获取句柄
hwnd = win32gui.FindWindow(classname, titlename)

#获取窗口左上角和右下角坐标
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
win32gui.MoveWindow(hwnd, 100, 100, 1280, 720, 0)


print(left)
print(top)
print(right)
print(bottom)
