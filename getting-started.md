# Getting Started


This is an open source hardware and software project, and before you can get your hands dirty you will need some parts to test things out. [Here is a list of everything you will need.](https://pykiln.com/get-started.html "Here is a list of everything you will need.")

## Install Micropython + PyKiln on an ESP32

[Install Python 3.7 or higher](https://www.python.org/downloads/ "Install Python 3.7 or higher")
(make sure to include the paths and command lines tools during installation)

Download and upzip the PyKiln repository to your computer.

Included in the repository is a python script that will automatically download the required libraries, erase your ESP32, write the Micropython firmware, and then copy the PyKiln files in the src folder to the ESP32. It will also prompt you for your WiFi network name and password. By default PyKiln will connect to GitHub Pages to load a web page to control your kiln. More info below if you want to host the page on your local network.

The script is called **setup_esp32.py**

#### Windows

To run the python script you can double click the **setup_esp32-windows.bat** file

#### Mac OS and Linux
Open terminal and CD to the PyKiln directory and run:

`python3 setup-esp32.py`

#### Installation Complete!

After you have installed Micropython and PyKiln on your ESP32 you are all set to start using it. The instructions below are for developers who want to work on the project.

## How to Locally Host PyKiln

Hosting the PyKiln webpage on your local network is useful if you don't have an internet connection, or are worried about losing internet connection and not being able to control your kilns. Most people should be fine with using GitHub Pages to load the PyKiln webpage.

If you're still interested in hosting the page locally here is how you can do it. 

In the docs>pykiln folder in this repository you will find a file called **MultithreadedSimpleHTTPServer.py**. If you run it it will start a simple web server on your computer. You can then open a web browser on any device on your nextwork and go to the IP address of your computer to see the PyKiln webpage.

------------



## Install Development Tools

If you're interested in customizing or helping with the development of PyKiln here are the tools you'll need to get started.

### Software
- [Install Python 3.7 or higher](https://www.python.org/downloads/ "Install Python 3.7 or higher") (make sure to include the paths and command lines tools during installation)
- [Install NodeJS 6.95 or higher](https://nodejs.org/en/ "Install NodeJS 6.95 or higher")
- [Install Visual Studio Code](https://code.visualstudio.com/ "Install Visual Studio Code")

### Visual Studio Code Extensions
Open Visual Studio Code, then click on the Extensions button and search and install the following extensions:
- python
- pymakr

### Python Libraries
Open command prompt in project directory

`pip3 install esptool`

`pip3 install --upgrade micropy-cli`

### Micropython firmware for the ESP32:
Included in this project is the following build:

**GENERIC : esp32-idf3-20200902-v1.13.bin**

[For the latest firmware please check the micropython website.](https://micropython.org/download/esp32/ "For the latest firmware please check the micropython website.")

### Flashing the firmware:

Here is how to manually flash Micropython onto an ESP32, or you can also  use the included **setup-esp32.py** file which will do the same thing.

#### Find Your Serial Port

**Windows**

Open Device Manager to find the COM port used by your ESP32, it should be labeled Silicon Labs. In my case it's COM4

**Linux**

To find it on Linux, run this command:

`ls /dev/tty*`

**Mac OS**

On Mac run this command:

`ls /dev/cu.*`

More info here if you're having trouble getting connected over Serial:
https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/establish-serial-connection.html


#### Erase everything on the ESP32:
Hold down the BOOT button on the ESP32 and run this command:

`esptool.py --chip esp32 --port COM4 erase_flash`

Once a connection has been established you can let go of the BOOT button

#### Install Micropython:
`esptool.py --chip esp32 --port COM4 --baud 460800 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin`

### Install ESP32 Micropython Libraries for Visual Studio Code

The latest version of micropy cli doesn't support version micropython 1.13. So, I've included the stubs and visual studio settings in this repo, but below are the steps for installing v1.12.0.

Open a command window in the PyKiln project.

Run this to list out all the available Micropython stubs for esp32:

`micropy stubs search esp32`

PyKiln uses micropython 1.13, but the 1.13 stubs are not currently available to download so use 1.12 for now:

`micropy stubs add esp32-micropython-1.12.0`

`micropy init`

Press enter to accept PyKiln as the project name.

Use spacebar to select VSCode Settings for Autocomplete/Intellisense
Press the down arrow key and then press spacebar to select Pymakr, and Pylint, then press enter

Press spacebar to select esp32-micropython-1.12.0, and then press enter

### Uploading Code to ESP32 in Visual Studio Code

- Plug your ESP32 Dev Kit into a USB port on your computer
- Open the PyKiln project in Visual Studio Code
- Press CTRL+SHIFT+P to bring up the search
- Search for Python: Select Interpreter and then select Python 3.7 or newer
- Search for Python: Select Linter and then select pylint
- Search for Pymakr > Global Settings
- - set **address** to be your serial port
- - set **auto_connect** to false
- Press CTRL+SHIFT+P and search for pymaker > connect, this connects to your ESP32 over serial

If you need to manage the files on the ESP32 run this command to get a remote shell connection:

`rshell -p COM4`

To view the files on the ESP32 you can change directory and list the files with these commands:

`cd /pyboard/`

`ls`

You can copy, remove, rename, and create new files like you would in a Linux terminal.

In the **setup-esp32.py** file at the end it does an rsync to copy over the files in the src folder to the ESP32.

`rsync src/ /pyboard/`

------------

## API Documentation

This is still a work in progress, but I've started to put together a Swagger UI for testing and documentation
[Swagger API Documentation](/docs/swagger/ "Swagger API Documentation")

------------

## Component Diagram

This is a high level overview of all the components that go into setting up a PyKiln
![PyKiln Component Diagram](/wiring/pykiln-component-diagram.png)
