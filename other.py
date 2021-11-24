# Can ignore this file

import tkinter as tk
import time
import random

class pet():
    def __init__(self):
        # create a window
        self.window = tk.Tk()

        impath = 'C:\\Users\\eamon\\OneDrive\\Pictures\\desktop-cat\\gifs\\'
        check = 1

        # placeholder image
        self.walking_right = [tk.PhotoImage(file=impath+'walking_negative.gif', format='gif -index %i' % (i)) for i in range(4)]
        self.walking_left = [tk.PhotoImage(file=impath+'walking_positive.gif', format='gif -index %i' % (i)) for i in range(4)]
        self.idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(8)] #idle gif
        self.sleep = [tk.PhotoImage(file=impath+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(2)] #sleep gif
        self.frame_index = 0
        self.img = self.walking_right[self.frame_index]

        # timestamp to check whether to advance frame
        self.timestamp = time.time()

        # set focushighlight to black when the window does not have focus
        self.window.config(highlightbackground='black')

        # make window frameless
        self.window.overrideredirect(True)

        # make window draw over all others
        self.window.attributes('-topmost', True)

        # turn black into transparency
        self.window.wm_attributes('-transparentcolor', 'black')

        # create a label as a container for our image
        self.label = tk.Label(self.window, bd=0, bg='black')

        # create a window of size 128x128 pixels, at coordinates 0,0
        self.x = 0
        self.window.geometry('50x50+{x}+0'.format(x=str(self.x)))

        # add the image to our label
        self.label.configure(image=self.img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):
        # move right by one pixel
        self.x += 1

        # advance frame if 50ms have passed
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.frame_index = (self.frame_index + 1) % 4
            self.img = self.idle[self.frame_index]

        # create the window | the 1000 is the height of the window
        self.window.geometry('50x50+{x}+1000'.format(x=str(self.x)))
        # add the image to our label
        self.label.configure(image=self.img)
        # give window to geometry manager (so it will appear)
        self.label.pack()

        # call update after 10ms
        self.window.after(10, self.update)

pet()