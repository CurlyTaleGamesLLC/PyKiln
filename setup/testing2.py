import threading
import time
from tkinter.ttk import Progressbar, Frame
from tkinter import IntVar, Tk

import subprocess
import sys

root = Tk()


class Progress:

    val = IntVar()
    ft = Frame()
    ft.pack(expand=True)
    kill_threads = False  # variable to see if threads should be killed

    def __init__(self):
        self.pb = Progressbar(self.ft, orient="horizontal", mode="indeterminate", variable=self.val)
        self.pb.pack(expand=True)
        self.pb.start(50)

        threading.Thread(target=self.check_progress).start()


    def check_progress(self):
        if self.kill_threads:  # if window is closed
            return
        val = self.val.get()
        install("esptool")
        val = self.val.get()
        install("micropy-cli")
        val = self.val.get()
        install("rshell")
        val = self.val.get()
        self.finish()
        return

    def finish(self):
        self.ft.pack_forget()
        print("Finish!")


progressbar = Progress()

def install(package):
    print("Installing " + package)
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print()

def on_closing():       # function run when closing
    progressbar.kill_threads = True  # set the kill_thread attribute to tru
    time.sleep(0.1)  # wait to make sure that the loop reached the if statement
    root.destroy()   # then destroy the window

root.protocol("WM_DELETE_WINDOW", on_closing) # bind a function to close button

root.mainloop()