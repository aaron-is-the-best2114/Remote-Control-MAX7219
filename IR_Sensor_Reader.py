import evdev

def get_ir_device():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        print(device.name)
        if "gpio_ir_recv" in device.name:
            return device

ir_device = get_ir_device()
if ir_device is None:
    print("IR device not found")
else:
    print("IR device found:", ir_device.name)
    for event in ir_device.read_loop():
        if event.type == evdev.ecodes.EV_MSC and event.code == evdev.ecodes.MSC_SCAN:
            print(event.value)