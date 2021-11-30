# import pyautogui
import random
import tkinter as tk
# import ctypes
from ctypes import windll, wintypes, byref
import sys
# import pypiwin32
# from win32api import GetMonitorInfo, MonitorFromPoint
# from PyQt5.QtWidgets import QApplication
# from pywin32 import GetMonitorInfo, MonitorFromPoint

# take a look at this when you get back home ==> https://stackoverflow.com/questions/4357258/how-to-get-the-height-of-windows-taskbar-using-python-pyqt-win32

# get screen resolution
def get_screen_resolution():
  user32 = windll.user32
  screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
  return screensize
# print(screensize[1])

# get taskbar height:
SPI_GETWORKAREA = 48
SM_CYSCREEN = 1
def get_taskbar_size():
    SystemParametersInfo = windll.user32.SystemParametersInfoA
    work_area = wintypes.RECT()
    if (SystemParametersInfo(SPI_GETWORKAREA, 0, byref(work_area), 0)):
        GetSystemMetrics = windll.user32.GetSystemMetrics
        return GetSystemMetrics(SM_CYSCREEN) - work_area.bottom

print('taskbar size : ')
print(get_taskbar_size())

x = (int)(get_screen_resolution()[0]/4)
print(get_screen_resolution()[1])
y = (int)(get_screen_resolution()[1] - (get_taskbar_size()*2))
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
impath = 'gifs\\' # need to make this dynamic 

#transfer random no. to event
def event(cycle,check,event_number,x):
  if event_number in idle_num:
    check = 0
    window.after(400,update,cycle,check,event_number,x) # no. 1,2,3,4 = idle
  elif event_number == 5:
    check = 1
    window.after(100,update,cycle,check,event_number,x) # no. 5 = idle to sleep
  elif event_number in walk_left:
    check = 4
    window.after(100,update,cycle,check,event_number,x) # no. 6,7 = walk towards left
  elif event_number in walk_right:
    check = 5
    window.after(100,update,cycle,check,event_number,x) # no 8,9 = walk towards right
  elif event_number in sleep_num:
    check  = 2
    window.after(1000,update,cycle,check,event_number,x) # o. 10,11,12,13,15 = sleep
  elif event_number == 14:
    check = 3
    window.after(100,update,cycle,check,event_number,x) # no. 15 = sleep to idle
    
#making gif work 
def gif_work(cycle,frames,event_number,first_num,last_num):
  if cycle < len(frames) -1:
    cycle+=1
  else:
    cycle = 0
    event_number = random.randrange(first_num,last_num+1,1)
  return cycle,event_number
 
def update(cycle,check,event_number,x):
  #idle
  if check ==0:
    frame = idle[cycle]
    cycle ,event_number = gif_work(cycle,idle,event_number,1,9)
  
  #idle to sleep
  elif check ==1:
    frame = idle_to_sleep[cycle]
    cycle ,event_number = gif_work(cycle,idle_to_sleep,event_number,10,10) # sleep
  elif check == 2:
    frame = sleep[cycle]
    cycle ,event_number = gif_work(cycle,sleep,event_number,10,15) # sleep to idle
  elif check ==3:
    frame = sleep_to_idle[cycle]
    cycle ,event_number = gif_work(cycle,sleep_to_idle,event_number,1,1) # walk toward left
  elif check == 4:
    frame = walk_positive[cycle]
    cycle , event_number = gif_work(cycle,walk_positive,event_number,1,9)
    x += 3 # walk towards right
  elif check == 5:
    frame = walk_negative[cycle]
    cycle , event_number = gif_work(cycle,walk_negative,event_number,1,9)
    x += -3
  window.geometry('48x48-'+str(x)+'+'+str(y)) # was 1000 for my pc but need to change this to be more dynamic
  label.configure(image=frame)
  window.after(1,event,cycle,check,event_number,x)
 
window = tk.Tk() # call buddy's action gif

idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(8)] # idle gif
idle_to_sleep = [tk.PhotoImage(file=impath+'idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(2)] # idle to sleep gif
sleep = [tk.PhotoImage(file=impath+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(2)] # sleep gif
sleep_to_idle = [tk.PhotoImage(file=impath+'sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(2)] # sleep to idle gif
walk_positive = [tk.PhotoImage(file=impath+'walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(2)] # walk to left gif
walk_negative = [tk.PhotoImage(file=impath+'walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(2)] # walk to right gif

#window configuration
window.config(highlightbackground='black')
label = tk.Label(window,bd=0,bg='black')

# make window frameless
window.overrideredirect(True)
        
# turn black into transparency
window.wm_attributes('-transparentcolor','black')

# make window draw over all others
window.attributes('-topmost', True)

# give window to geometry manager (so it will appear)
label.pack()

#loop the program | run self.update() after 0ms when mainloop starts
window.after(1,update,cycle,check,event_number,x)
window.mainloop()