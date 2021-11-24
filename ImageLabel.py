# Found this class from stack overflow, not even using it but makes the gifs run smoother

import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import time


class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

def update(x):
    x += 1

# initialize window
window = tk.Tk()

# set window properties
x = 300
window.config(highlightbackground='black')
window.attributes('-topmost', True)
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'black')
window.geometry('48x48+{x}+1000'.format(x=str(x)))

impath = 'C:\\Users\\eamon\\OneDrive\\Pictures\\desktop-cat\\gifs\\'
walking_right = [tk.PhotoImage(file=impath+'walking_negative.gif', format='gif -index %i' % (i)) for i in range(4)]
walking_left = [tk.PhotoImage(file=impath+'walking_positive.gif', format='gif -index %i' % (i)) for i in range(4)]
idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(8)] #idle gif
sleep = [tk.PhotoImage(file=impath+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(2)] #sleep gif

frame_index = 0
img = walking_right[frame_index]


# img = walking_right[frame_index]
# label = tk.Label(root, bd=0, bg='black')
# x = 0
# label.configure(image=img)
# label.pack()

currGif = 'walking_negative.gif'
timestamp = time.time()
# # advance frame if 50ms have passed
# if time.time() > timestamp + 0.05:
#     timestamp = time.time()
#     # advance the frame by one, wrap back to 0 at the end
#     frame_index = (frame_index + 1) % 4
#     img = walking_right[frame_index]


lbl = ImageLabel(window)
lbl.pack()
lbl.load(impath+currGif)
print(x)
# window.after(1,x+=1)
window.mainloop()

moving = True
while (moving):
    print(x)
    x += 1