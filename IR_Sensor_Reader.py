#Please run to get the codes for the left, right, up, and down buttons. Number buttons are optional. Any Remote Should work. 
import evdev

def get_ir_device():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if "gpio_ir_recv" in device.name:
            return device

ir_device = get_ir_device()
if ir_device is None:
    print("IR device not found") #If this shows, please check your wiring and read the instructions to ensure you have everything installed correctly. Any questions please ask. 
else:
    print("IR device found:", ir_device.name)
    for event in ir_device.read_loop():
        if event.type == evdev.ecodes.EV_MSC and event.code == evdev.ecodes.MSC_SCAN:
            print(event.value) #This will print the value codes for any button that is pressed on the IR Remote. 
