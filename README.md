# Remote-Control-MAX7219

To Ensure that the code works coreectly, please run the IR_Sensor_Reader.py python file to get the correct codes for your remote

Once you have the codes that are nessesary, you will have to update the Script.py file accrodingly.

Instructions:

Please Fallow the schematic to correctly wire everything together, then you will need to do the fallowing:

1. **Enable Device Tree overlays (dtoverlay)** to enable the kernel to talk to the IR receiver:
    - Edit the Raspberry Pi config file: `sudo nano /boot/config.txt`
    - Uncomment this to enable infrared communication. Change the pin to suit your configuration if required: `dtoverlay=gpio-ir,gpio_pin=17`
    - Reboot when finished: `sudo reboot`

2. **Install ir-keytable** to receive IR scancodes via the sensor:
    - Install the ir-keytable package and temporarily enable all protocols: `sudo apt-get install ir-keytable` and `sudo ir-keytable -p all`
    - Note that the last command will not persist a reboot and is for testing only (we’ll take care of this later!)

3. **Install evdev**, providing a Python interface to read input events generated when IR signals are received:
    - You may need to install pip for Python 3 if not already present: `sudo apt-get install python3-pip`
    - Install the evdev library and evtest package: `sudo pip3 install evdev` and `sudo apt-get install evtest`
    - Run evtest to try it all out: `sudo evtest`

4. **luma.led_matrix library** - This library is used to control the MAX7219 8x8 Matrix Display. You can install it using `pip3 install luma.led_matrix`.

5. **SPI Interface on RPI** - Please ensure that the SPI interface is turned on in the raspberry pi configuration, either through the terminal or GUI. 
