import keyboard


def monitor_keypress():
    while True:
        try:
            if keyboard.is_pressed('a'):
                print("Key pressed: a")
            elif keyboard.is_pressed('b'):
                print("Key pressed: b")
            elif keyboard.is_pressed('c'):
                print("Key pressed: c")
            elif keyboard.is_pressed('esc'):
                print('Exiting process.')
                break

        except KeyboardInterrupt:
            print('\nDone reading input. Keyboard interrupt.')
            break

        except Exception as e:
            print(e)
            break


if __name__ == "__main__":
    monitor_keypress()
