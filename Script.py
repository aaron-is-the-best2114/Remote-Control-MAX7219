#To Get the correct codes for your specific remote please run the IR_Sensor_Reader.py script.
import evdev
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

# Set up IR device
def get_ir_device():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if "gpio_ir_recv" in device.name:
            return device

ir_device = get_ir_device()
if ir_device is None:
    print("IR device not found")
else:
    print("IR device found:", ir_device.name)

# Set up MAX7219 8x8 Matrix Display
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1)

# Initialize dot position
x = 3
y = 3

# Draw dot on display
def draw_dot():
    with canvas(device) as draw:
        draw.point((x, y), fill="white")

#draw_dot()

# Move dot based on arrow key press
for event in ir_device.read_loop():
    if event.type == evdev.ecodes.EV_MSC and event.code == evdev.ecodes.MSC_SCAN:
        #You may have to change the values based on the type of remote you have.
        #Run IR_Sensor_Reader.py to see the correct values for your remote
        if event.value == 1088: #Up Arrow
            y = max(0, y - 1)
        elif event.value == 1089: #Down Arrow
            y = min(7, y + 1)
        elif event.value == 1031: #Left Arrow
            x = max(0, x - 1)
        elif event.value == 1030: #Right Arrow
            x = min(7, x + 1)
        draw_dot()
        
        #If you have numbers on your remote. You may have to adjust the values accrodingly
        #Run IR_Sensor_Reader.py to see the correct values for your remote
        #To add numbers to the Display get rid of the quotation marks around the code below
        '''
        if event.value == 1041:
            with canvas(device) as draw:
                text(draw, (1, 0), "1", fill="white", font=proportional(CP437_FONT))
        if event.value == 1042:
            with canvas(device) as draw:
                text(draw, (1, 0), "2", fill="white", font=proportional(CP437_FONT))
        if event.value == 1043:
            with canvas(device) as draw:
                text(draw, (1, 0), "3", fill="white", font=proportional(CP437_FONT))
        if event.value == 1044:
            with canvas(device) as draw:
                text(draw, (1, 0), "4", fill="white", font=proportional(CP437_FONT))
        if event.value == 1045:
            with canvas(device) as draw:
                text(draw, (1, 0), "5", fill="white", font=proportional(CP437_FONT))
        if event.value == 1046:
            with canvas(device) as draw:
                text(draw, (1, 0), "6", fill="white", font=proportional(CP437_FONT))
        if event.value == 1047:
            with canvas(device) as draw:
                text(draw, (1, 0), "7", fill="white", font=proportional(CP437_FONT))
        if event.value == 1048:
            with canvas(device) as draw:
                text(draw, (1, 0), "8", fill="white", font=proportional(CP437_FONT))
        if event.value == 1049:
            with canvas(device) as draw:
                text(draw, (1, 0), "9", fill="white", font=proportional(CP437_FONT))
        if event.value == 1040:
            with canvas(device) as draw:
                text(draw, (0, 0), "0", fill="white", font=proportional(CP437_FONT))
        if event.value == 1032:
            with canvas(device) as draw:
                text(draw, (0, 0), "-", fill="black", font=proportional(CP437_FONT))
                continue
                
        '''
        print(event.value)
        