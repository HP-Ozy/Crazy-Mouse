import pyautogui
import random
import time
import keyboard

pyautogui.FAILSAFE = False

print("Mouse impazzito attivato... buona fortuna 😈")
print("(psst: CTRL+SHIFT+Q per fermarlo)")

running = True

def stop():
    global running
    running = False

keyboard.add_hotkey('ctrl+shift+q', stop)

while running:
    
    dx = random.randint(-80, 80)
    dy = random.randint(-80, 80)
    
    
    durata = random.uniform(0.05, 0.3)
    
    pyautogui.moveRel(dx, dy, duration=durata)
    
    
    time.sleep(random.uniform(0.1, 2.0))

print("Mouse liberato! 🐭")
