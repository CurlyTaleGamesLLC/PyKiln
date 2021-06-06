# from tkinter import *
# from tkinter.ttk import Progressbar
# import time
# import threading


# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('400x200')
# ws.config(bg='#345')

# def start_download():
#     print("START")
#     time.sleep(5)
#     pb.start()   
    
# def stop_download():
#     print("STOP")
#     pb.stop()

# pb = Progressbar(
#     ws,
#     orient = HORIZONTAL,
#     length = 200,
#     mode = 'determinate'
#     )
# pb.pack()

# msg = Label(
#     ws,
#     text='',
#     bg='#345',
#     fg='red',
    
# )

# msg.pack()

# start = Button(
#     ws,
#     text='Start Download',
#     command=threading.Thread(target=start_download).start()
#     #command=start_download
#     )

# start.pack()

# stop = Button(
#     ws,
#     text='Stop Download',
#     command=stop_download
# )
# stop.pack()

# ws.mainloop()

# from tkinter import *
# from tkinter.ttk import Progressbar
# import time
# import threading


# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('400x350')
# ws.config(bg='#345')


# def play():
#     time.sleep(10)
#     pb.start()

# pb = Progressbar(
#     ws,
#     orient = HORIZONTAL,
#     length = 100,
#     mode = 'determinate'
#     )
# pb.pack(pady=30)

# play = Button(
#     ws,
#     text="Freeze",
#     #command=threading.Thread(target=play).start())
#     command=play)
# play.pack(pady=30)

# pb1 = Progressbar(
#     ws,
#     orient = HORIZONTAL,
#     length = 100,
#     mode = 'determinate'
#     )

# pb1.start()
# pb1.pack(pady=30)

# ws.mainloop()



import threading
import time
from tkinter.ttk import Progressbar, Frame
from tkinter import IntVar, Tk


root = Tk()


class Progress:

    val = IntVar()
    ft = Frame()
    ft.pack(expand=True)
    kill_threads = False  # variable to see if threads should be killed

    def __init__(self):
        self.pb = Progressbar(self.ft, orient="horizontal", mode="determinate", variable=self.val)
        self.pb.pack(expand=True)
        self.pb.start(50)

        threading.Thread(target=self.check_progress).start()


    def check_progress(self):
        while True:
            if self.kill_threads:  # if window is closed
                return             # return out of thread
            val = self.val.get()
            print(val)
            if val > 97:
                self.finish()
                return
            time.sleep(0.1)

    def finish(self):
        self.ft.pack_forget()
        print("Finish!")


progressbar = Progress()


def on_closing():       # function run when closing
    progressbar.kill_threads = True  # set the kill_thread attribute to tru
    time.sleep(0.1)  # wait to make sure that the loop reached the if statement
    root.destroy()   # then destroy the window

root.protocol("WM_DELETE_WINDOW", on_closing) # bind a function to close button

root.mainloop()