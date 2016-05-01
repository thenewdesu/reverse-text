import win32clipboard, os
import time
def derp():
    global value
    try:
        win32clipboard.OpenClipboard()
        value = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:#clears clipboard that is stuck
        os.popen('@echo off | clip',"r")
        print("Exception! Clipboard cleared!1")
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText("{0}".format(value[::-1]))
        win32clipboard.CloseClipboard()
    except:
        print('wtf r u doing')
    print(value[::-1])
derp()
recent_value = ""
while True:
    time.sleep(.3)
    win32clipboard.OpenClipboard()
    tmp_value = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    if tmp_value[::-1] != recent_value:
        recent_value = tmp_value
        derp()



