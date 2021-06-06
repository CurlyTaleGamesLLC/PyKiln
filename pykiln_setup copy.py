import os
import time
import json
# import threading

# from tkinter import *
# import tkinter.ttk as tkk
# import tkinter.font as tkFont

# migrated imports
import subprocess
import sys
import glob
import time
# import webbrowser

import setup.settings as settings
# from setup.setup_utils import *
# import setup.setup_utils


import setup.setup_layouts as sl
# from setup.setup_layouts import LayoutSplash, LayoutTextImage, LayoutText, LayoutLoading, LayoutWifi, initialize



def main():
    # global page
    print("Hello World!")
    # Updates the dependencies, and then loads the splash screen
    # page = "splash"
    settings.SetCurrentPage("splash")
    sl.LayoutLoading("Updating Dependencies", "If this is your first time it might take a minute...")
    # sl.LayoutLoading()
    sl.initialize()

if __name__ == "__main__":
    main()





