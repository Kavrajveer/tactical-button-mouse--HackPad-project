import time
import board
import digitalio
import rotaryio
import usb_hid
from adafruit_hid.mouse import Mouse

# Initialize the Mouse HID object
mouse = Mouse(usb_hid.devices)

# --- CONFIGURATION VARIABLES ---
# Default pixels moved per directional click
cursor_speed = 10 
# --- PIN SETUP: DIRECTIONAL BUTTONS ---
# (Assuming standard digital pins D0-D3 for movement)
btn_up = digitalio.DigitalInOut(board.D0)
btn_up.direction = digitalio.Direction.INPUT
btn_up.pull = digitalio.Pull.UP

btn_down = digitalio.DigitalInOut(board.D1)
btn_down.direction = digitalio.Direction.INPUT
btn_down.pull = digitalio.Pull.UP

btn_left = digitalio.DigitalInOut(board.D2)
btn_left.direction = digitalio.Direction.INPUT
btn_left.pull = digitalio.Pull.UP

btn_right = digitalio.DigitalInOut(board.D3)
btn_right.direction = digitalio.Direction.INPUT
btn_right.pull = digitalio.Pull.UP
