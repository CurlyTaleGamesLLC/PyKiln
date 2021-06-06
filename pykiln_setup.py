import os
import time
import json
import threading

from tkinter import *
import tkinter.ttk as tkk
import tkinter.font as tkFont

# migrated imports
import subprocess
import sys
import glob
import time
# import webbrowser

import setup.settings as settings

base_folder = os.path.dirname(__file__)
assets_folder = os.path.join(base_folder, 'setup')



screen = Tk()
screen.title("PyKiln Setup")
# set resolution and disable resizing
screen.geometry("640x440")
screen.resizable(False, False)
# set icon
screen.iconbitmap(os.path.join(assets_folder, 'logo.ico'))

bullet = "\u2022" #specifies bullet character

progressbar = ""

wifiName = StringVar()
wifiPassword = StringVar()
host = StringVar()

# adds background image to splash page
background_image = PhotoImage(file=os.path.join(assets_folder, 'setup-background.gif'))
container = Label(screen, image=background_image)
container.config(image=background_image)
container.img = background_image  # avoid garbage collection

headerFont = tkFont.Font(family='Helvetica', size=18, weight=tkFont.BOLD)
bodyFont = tkFont.Font(family='Helvetica', size=12)
labelFont = tkFont.Font(family='Helvetica', size=9)
buttonFont = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)





def buttonClick(newPage):
    global container
    global screen
    
    global wifiName
    global wifiPassword
    global host
    
    page = newPage


    container.pack_forget()

    for widget2 in container.grid_slaves():
        widget2.grid_forget()
        # if int(widget2.grid_info()["row"]) > 6:
            

    for widget in container.winfo_children():
        widget.destroy()

    print(page)

    if page == "splash":
        print("You're on the splash page!")
        LayoutSplash()
        return

    if page == "home":
        print("You're on the home page!")
        LayoutTextImage("Setup PyKiln", "Please make sure your ESP32 is unplugged from your computer, then click Next.", "setup-unplug.gif", "Next", "plugin")
        return

    if page == "plugin":
        print("You're on the plugin page!")
        # serialPortsBefore = list_serial_options(True)
        # serialDevicesBefore = list_serial_options(False)
        settings.SerialReset()
        LayoutTextImage("Detecting ESP32:", "Plug in your ESP32 to your computer, and wait a few seconds to be recognized, then click Next.", "setup-plug.gif", "Next", "install")
        return

    if page == "install":
        print("You're on the install page!")

        settings.SerialSet()

        installMessage = ""
        if settings.GetActiveSerialPort() == "":
            installMessage = "No serial device detected. Please unplug your ESP32 from your computer and try again."
            LayoutText("No Devices Detected", installMessage, "Exit", "home")
        else:
            installMessage = "Device detected on serial port: " + settings.GetActiveSerialPort() + ". Keep the boot button held down and click the next button."
            LayoutTextImage("Detected Device:", installMessage, "setup-boot.gif", "Next", "flashing")
        return

    if page == "flashing":
        print("You're on the flashing page!")
        page = "wifi"
        settings.SetCurrentPage(page)
        LayoutLoading("Flashing Firmware", "Be patient, this will take several minutes. It is erasing the chip, and writing the Micropython Firmware onto the ESP32")
        return

    if page == "wifi":
        print("You're on the wifi page!")
        LayoutWifi("Connect to WiFi", "Connect", "pykiln")
        return

    if page == "pykiln":
        print("You're on the pykiln page!")
        settings.WifiLogin(wifiName.get(), wifiPassword.get(), host.get())
        page = "connected"
        settings.SetCurrentPage(page)
        LayoutLoading("Connecting PyKiln", "Almost there, this will take a few minutes. It is copying the PyKiln files onto the ESP32, connecting to your wireless network, and getting an IP address.")
        return

    if page == "connected":
        print("You're on the connected page!")
        page = "complete"
        settings.SetCurrentPage(page)
        LayoutLoading("Getting IP Address", "Your PyKiln is getting an IP address. Once it connects the ESP32 will reboot")
        return
    if page == "complete":
        print("You're on the complete page!")
        LayoutText("Setup Complete!", "A shortcut has been placed on your desktop, and your default web browser is connecting to your new PyKiln. Be sure to bookmark the web page to access it in the future.", "Exit", "splash")
        
        return


# Resets the layout for different pages
def ResetRows():
    global container
    print("Clear Frame")
    for i in range(5):
        container.grid_rowconfigure(i, weight=0)
    container.grid_columnconfigure(0, weight=1)
    

def LayoutText(title, content, buttonText, pageName):
    global headerFont
    global bodyFont
    global buttonFont
    global container
    ResetRows()

    # title
    title_text = Label(container, text=title, font=headerFont)
    title_text.grid(row=0, column=0, columnspan=2, sticky="ew", pady=8, padx=16)

    # text content
    content_text = Label(container, text=content, font=bodyFont, wraplength=300, justify="left", anchor="n")
    content_text.grid(row=1, column=0, sticky="new", pady=4, padx=16)
    container.grid_rowconfigure(1, weight=1)

    # button
    if buttonText != "":
        btn = Button(container, text=buttonText, font=buttonFont, command = lambda: buttonClick(pageName))
        btn.grid(row=2, column=0, sticky='esw', columnspan=2, ipady=8)
    container.config(image='')
    container.pack(fill=BOTH, expand=True)

def LayoutTextImage(title, content, imagePath, buttonText, pageName):
    # global page
    global assets_folder
    global headerFont
    global bodyFont
    global buttonFont
    global container
    ResetRows()

    # title
    title_text = Label(container, text=title, font=headerFont)
    title_text.grid(row=0, column=0, columnspan=2, sticky="ew", pady=8, padx=16)

    # text content
    content_text = Label(container, text=content, font=bodyFont, wraplength=260, justify="left")
    content_text.grid(row=1, column=0, sticky="nw", pady=4, padx=(16,0))

    # image content - must be GIF or PBM filetype
    image_path = os.path.join(assets_folder, imagePath)
    img = PhotoImage(file=image_path)
    label = Label(container, image = img)
    label.image = img
    label.grid(row=1, column=1, sticky="nw", padx=16)

    container.grid_rowconfigure(1, weight=1)
    # button
    if buttonText != "":
        btn = Button(container, text=buttonText, font=buttonFont, command = lambda: buttonClick(pageName))
        btn.grid(row=2, column=0, sticky='esw', columnspan=2, ipady=8)
    container.config(image='')
    container.pack(fill=BOTH, expand=True)
    # page = pageName

def LayoutWifi(title, buttonText, pageName):
    # global page
    global assets_folder
    global headerFont
    global labelFont
    global buttonFont
    global container

    global wifiName
    global wifiPassword
    global host

    ResetRows()

    # title
    title_text = Label(container, text=title, font=headerFont)
    title_text.grid(row=0, column=0, columnspan=2, sticky="ew", pady=8, padx=16)

    # wifi input fields
    Label(container, text="WiFi SSID: ").grid(row=1, sticky="e", padx=(10, 0), pady=10)
    Label(container, text="Password: ").grid(row=2, sticky="e", padx=(10, 0), pady=10)
    Label(container, text="Host URL (Optional): ").grid(row=3, sticky="e", padx=(10, 0), pady=(10,0))

    e1 = Entry(container, textvariable=wifiName, width=50)
    e2 = Entry(container, textvariable=wifiPassword, width=50)
    e2.config(show=bullet)
    e3 = Entry(container, textvariable=host, width=50)


    e1.grid(row=1, column=1, sticky="w", padx=(0,80), pady=10)
    e2.grid(row=2, column=1, sticky="w", padx=(0,80), pady=10)
    e3.grid(row=3, column=1, sticky="w", padx=(0,80), pady=(10,0))

    host_text = Label(container, text="Enter the URL for your self hosted web server, if you don't know that this is, leave it blank.", font=labelFont, wraplength=300, justify="left")
    host_text.grid(row=4, column=1, sticky="nw", pady=0, padx=(0,10))
    container.grid_rowconfigure(4, weight=1)

    btn = Button(container, text=buttonText, font=buttonFont, command = lambda: buttonClick(pageName))
    btn.grid(row=5, column=0, sticky='esw', columnspan=2, ipady=8)
    container.config(image='')
    container.pack(fill=BOTH, expand=True)
    # page = pageName

def LayoutSplash():
    global assets_folder
    global headerFont
    global labelFont
    global buttonFont
    global container
    global background_image

    ResetRows()
    # load background image
    print("Load BG")
    background_image = PhotoImage(file=os.path.join(assets_folder, 'setup-background.gif'))
    container.config(image=background_image)
    container.img = background_image  # avoid garbage collection


    xPad = 180
    yPad = 4

    btn0 = Button(container, text="Setup PyKiln", font=buttonFont, command = lambda: buttonClick("home"), bg='#9c27b0', fg='white')
    btn0.grid(row=0, column=0, sticky='esw', ipady=8, pady=(160, yPad), padx=xPad)

    btn1 = Button(container, text="Reconnect to WiFi", font=buttonFont, command = lambda: buttonClick("reconnect"))
    btn1.grid(row=1, column=0, sticky='esw', ipady=8, pady=yPad, padx=xPad)

    btn1 = Button(container, text="Scan Network for PyKiln", font=buttonFont, command = lambda: buttonClick("scan"))
    btn1.grid(row=2, column=0, sticky='esw', ipady=8, pady=yPad, padx=xPad)

    Label(container, text="V0.1", bg='black', fg='white').grid(row=3, sticky="s", pady=10)

    print("Place UI")

    container.pack(fill=BOTH, expand=True)

def LayoutLoading(title, content):
    # global page
    global headerFont
    global bodyFont
    global buttonFont
    global container
    ResetRows()

    global progressbar

    # title
    title_text = Label(container, text=title, font=headerFont)
    title_text.grid(row=0, column=0, columnspan=2, sticky="ew", pady=8, padx=16)

    # text content
    content_text = Label(container, text=content, font=bodyFont, wraplength=300, justify="left", anchor="n")
    content_text.grid(row=1, column=0, sticky="new", pady=4, padx=16)
    container.grid_rowconfigure(1, weight=1)

    progressbar = None
    progressbar = Progress()

    # placeholder used to offset progress bar from the bottom
    Label(container, text=" ").grid(row=4, sticky="s", pady=(250,0))

    container.config(image='')
    container.pack(fill=BOTH, expand=True)


class Progress:

    # global page
    # global serialPortsDetected
    global assets_folder
    global container

    val = IntVar()
    kill_threads = False  # variable to see if threads should be killed

    def __init__(self):
        self.pb = tkk.Progressbar(container, orient="horizontal", mode="indeterminate", variable=self.val)
        self.pb.grid(row=2, column=0, sticky="ew", pady=4, padx=180)
        container.grid_rowconfigure(2, weight=1)
        self.pb.start(50)
        threading.Thread(target=self.check_progress).start()

    def check_progress(self):
        if self.kill_threads:  # if window is closed
            return

        # page = pys.GetCurrentPage()
        page = settings.GetCurrentPage()
        
        if page == "splash":
            val = self.val.get()
            settings.install("esptool")
            val = self.val.get()
            settings.install("micropy-cli")
            val = self.val.get()
            settings.install("rshell")
            val = self.val.get()
            self.finish()
            return
        
        if page == "wifi":
            binFile = ""
            for file in os.listdir(assets_folder):
                if file.endswith(".bin"):
                    print(os.path.join(assets_folder, file))
                    binFile = os.path.join(assets_folder, file)
            val = self.val.get()
            print("Erasing ESP32 chip")
            os.system("esptool.py --chip esp32 --port " + settings.GetActiveSerialPort() + " erase_flash") #serialPortsDetected[0]
            val = self.val.get()
            print("lashing Micropython to ESP32")
            os.system("esptool.py --chip esp32 --port " + settings.GetActiveSerialPort() + " --baud 460800 write_flash -z 0x1000 " + binFile) #serialPortsDetected[0]
            self.finish()
            return

        if page == "connected":
            val = self.val.get()
            os.system("rshell -p " + settings.GetActiveSerialPort() + " rsync src/ /pyboard/ ; exit")
            val = self.val.get()
            os.system("rshell -p " + settings.GetActiveSerialPort() + " repl ~ import reset ~ ; exit")
            self.finish()
            return

        if page == "complete":
            val = self.val.get()
            print("IP PATH")
            dirPath = os.getcwd()
            filePath = os.path.join(dirPath, 'ip.txt')

            print(filePath)

            # convert path to forward slashes and remove the drive letter for REPL
            filePathREPL = filePath.replace('\\', '/')
            if os.name == 'nt':
                filePathREPL = filePathREPL.replace('C:', '')

            
            print(filePathREPL)
            copyCommand = "cp /pyboard/ip.txt " + filePathREPL
            os.system("rshell -p " + settings.GetActiveSerialPort() + " " + copyCommand + " ; exit")
            os.system("rshell -p " + settings.GetActiveSerialPort() + " repl ~ import reset ~ ; exit") #reboots the pykiln
            time.sleep(10.0) #wait for reboot

            self.finish()
            return

    def finish(self):
        self.pb.pack_forget()
        print("Finish!")
        print(settings.GetCurrentPage())
        buttonClick(settings.GetCurrentPage())
        self.pb.destroy

def on_closing():       # function run when closing
    global progressbar
    # global screen
    if progressbar != "":
        progressbar.kill_threads = True  # set the kill_thread attribute to tru
    time.sleep(0.1)  # wait to make sure that the loop reached the if statement
    screen.destroy()   # then destroy the window




def main():
    print("Hello World!")

if __name__ == "__main__":
    main()


settings.SetCurrentPage("splash")
LayoutLoading("Updating Dependencies", "If this is your first time it might take a minute...")


screen.protocol("WM_DELETE_WINDOW", on_closing) # bind a function to close button
screen.mainloop()