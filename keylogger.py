from pynput import keyboard


def keyPressed(key):
    print(f'PRESSED ==> {key}')

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
