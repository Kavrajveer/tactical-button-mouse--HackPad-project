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
# --- PIN SETUP: MOUSE ACTIONS ---
btn_lclick = digitalio.DigitalInOut(board.D4)
btn_lclick.direction = digitalio.Direction.INPUT
btn_lclick.pull = digitalio.Pull.UP

btn_dlclick = digitalio.DigitalInOut(board.D5)
btn_dlclick.direction = digitalio.Direction.INPUT
btn_dlclick.pull = digitalio.Pull.UP

btn_rclick = digitalio.DigitalInOut(board.D6)
btn_rclick.direction = digitalio.Direction.INPUT
btn_rclick.pull = digitalio.Pull.UP

btn_select = digitalio.DigitalInOut(board.D7)
btn_select.direction = digitalio.Direction.INPUT
btn_select.pull = digitalio.Pull.UP

# --- PIN SETUP: ENCODERS ---
# Encoder 1: Vertical Scroll (using pins D8, D9)
encoder_scroll = rotaryio.IncrementalEncoder(board.D8, board.D9)
last_scroll_position = encoder_scroll.position

# Encoder 2: Speed Control (using pins D10, D11)
encoder_speed = rotaryio.IncrementalEncoder(board.D10, board.D11)
last_speed_position = encoder_speed.position
# --- MAIN EXECUTION LOOP ---
select_held = False # Tracks if the text-select toggle is active

while True:
    # 1. Handle Speed Adjustment
        current_speed_position = encoder_speed.position
            if current_speed_position != last_speed_position:
                    # Increase or decrease speed based on rotation
                            if current_speed_position > last_speed_position:
                                        cursor_speed += 1
                                                else:
                                                            cursor_speed -= 1
                                                                    # Hard limit: Prevent speed from dropping below 1 pixel
                                                                            cursor_speed = max(1, cursor_speed) 
                                                                                    last_speed_position = current_speed_position
                                                                                            # (OLED dashboard update logic will go here next)

                                                                                                # 2. Handle Vertical Scrolling
                                                                                                    current_scroll_position = encoder_scroll.position
                                                                                                        if current_scroll_position != last_scroll_position:
                                                                                                                scroll_delta = current_scroll_position - last_scroll_position
                                                                                                                        mouse.move(wheel=scroll_delta)
                                                                                                                                last_scroll_position = current_scroll_position

                                                                                                                                    # 3. Handle Directional Movement
                                                                                                                                        x_move = 0
                                                                                                                                            y_move = 0
                                                                                                                                                if not btn_up.value:
                                                                                                                                                        y_move = -cursor_speed
                                                                                                                                                            if not btn_down.value:
                                                                                                                                                                    y_move = cursor_speed
                                                                                                                                                                        if not btn_left.value:
                                                                                                                                                                                x_move = -cursor_speed
                                                                                                                                                                                    if not btn_right.value:
                                                                                                                                                                                            x_move = cursor_speed
                                                                                                                                                                                                    
                                                                                                                                                                                                        if x_move != 0 or y_move != 0:
                                                                                                                                                                                                                mouse.move(x=x_move, y=y_move)

                                                                                                                                                                                                                    # 4. Handle Standard Clicks
                                                                                                                                                                                                                        if not btn_lclick.value:
                                                                                                                                                                                                                                mouse.click(Mouse.LEFT_BUTTON)
                                                                                                                                                                                                                                        time.sleep(0.2) # Debounce delay to prevent accidental multi-clicks

                                                                                                                                                                                                                                            if not btn_rclick.value:
                                                                                                                                                                                                                                                    mouse.click(Mouse.RIGHT_BUTTON)
                                                                                                                                                                                                                                                            time.sleep(0.2)
                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                        if not btn_dlclick.value:
                                                                                                                                                                                                                                                                                mouse.click(Mouse.LEFT_BUTTON)
                                                                                                                                                                                                                                                                                        time.sleep(0.05)
                                                                                                                                                                                                                                                                                                mouse.click(Mouse.LEFT_BUTTON)
                                                                                                                                                                                                                                                                                                        time.sleep(0.2)

                                                                                                                                                                                                                                                                                                            # 5. Handle Text Select Toggle
                                                                                                                                                                                                                                                                                                                if not btn_select.value:
                                                                                                                                                                                                                                                                                                                        select_held = not select_held
                                                                                                                                                                                                                                                                                                                                if select_held:
                                                                                                                                                                                                                                                                                                                                            mouse.press(Mouse.LEFT_BUTTON) # Holds the click down
                                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                                mouse.release(Mouse.LEFT_BUTTON) # Releases the click
                                                                                                                                                                                                                                                                                                                                                                        time.sleep(0.3) 

                                                                                                                                                                                                                                                                                                                                                                            time.sleep(0.01) # Stabilizes the loop loop
                                                                                                                                                                                                                                                                                                                                                                            