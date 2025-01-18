import pyautogui
import time

def main():
    try:
        while True:
            # Type the letter "A"
            pyautogui.typewrite("A")
            # Get the current mouse position
            x, y = pyautogui.position()
            # Move the mouse 3 pixels up
            pyautogui.moveTo(x, y - 3, duration=0.2)
            time.sleep(0.2)  # Small delay for smooth movement
            # Move the mouse 3 pixels down
            pyautogui.moveTo(x, y + 3, duration=0.2)
            time.sleep(1.6)  # Remaining time for a total of 2 seconds
    except KeyboardInterrupt:
        print("Script stopped by user.")

if __name__ == "__main__":
    main()
