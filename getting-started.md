Installing Dependencies:

Install Python 3.7 or Newer, make sure to include the paths and command lines tools
https://www.python.org/downloads/

Install NodeJS 6.95 or higher:
https://nodejs.org/en/

Install Visual Studio Code:
https://code.visualstudio.com/

Install plugins for VS Code:
install python extension
install pymakr extension
install pylint extension

Open command prompt in project directory
pip3 install esptool
pip3 install --upgrade micropy-cli

Download Micropython for the ESP32:
https://micropython.org/download/esp32/
I'm using this build: GENERIC : esp32-idf3-20191220-v1.12.bin

Erase everything on the ESP32:
esptool.py --chip esp32 --port COM4 erase_flash

Install Micropython:
esptool.py --chip esp32 --port COM4 --baud 460800 write_flash -z 0x1000 esp32-idf3-20191220-v1.12.bin


To list out all the available stubs for esp32:
micropy stubs search esp32

PyKiln currently uses micropython 1.12 for the ESP32, so run this command:

micropy stubs add esp32-micropython-1.12.0
micropy init

Press enter to accept PyKiln as the project name.

Use spacebar to select VSCode Settings for Autocomplete/Intellisense
Press the down arrow key and then press spacebar to select Pymakr, and Pylint, then press enter

Press spacebar to select esp32-micropython-1.12.0, and then press enter

Plug your ESP32 Dev Kit into a USB port on your computer

Open the project in visual studio, press CTRL + SHIFT + P to bring up the search
Search for Python: Select Interpreter and then select Python 3.7 or newer
Search for Python: Select Linter and then select pylint
Search for Pymakr > Global Settings

Open Device Manager to find the COM port used by your ESP32, it should be labeled Silicon Labs. In my case it's COM4

To find it on Linux, run this command:
ls /dev/tty*

On Mac run this command:
ls /dev/cu.*

More info here if you're having trouble getting connected over Serial:
https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/establish-serial-connection.html

In the global settings set "address" to be your serial port, also set "auto_connect" to false

Press CTRL + SHIFT + P and search for pymaker > connect

Running that will now connect you to your esp32 over serial
