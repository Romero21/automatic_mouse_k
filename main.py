import pyautogui
import win32api 
import time


def check_positions():
    mouse = pyautogui.position()
    return mouse

def is_pressed_L():
    return True if win32api.GetKeyState(0x01)<0 else False

def is_pressed_R():
    return True if win32api.GetKeyState(0x02)<0 else False

def start_record():
    return True if input("Do you wanna record sequence? Y/N: ").lower() == "y" else False 

def play_sequence():
    return True if input("Do you wanna play your sequence? Y/N: ").lower() == "y" else False   


if __name__ == "__main__":
    
    answer = start_record()
    l_button = False
    r_button = True
    sequence = [[False, 0, 0]]

    while answer: 
        sequence.append(["moveTo()", check_positions()[0],check_positions()[1]])
        if is_pressed_L():
            if l_button == False:
                sequence.append(["mouseDown()"])
                l_button = True
                r_button = True
            
        else:
            if r_button == True:
                sequence.append(["mouseUp()"])
                l_button = False
                r_button = False

        if is_pressed_L() and is_pressed_R():
            break

        time.sleep(0.1)

    
    if play_sequence():
        pyautogui.FAILSAFE = False
        for item in sequence:
            if item[0] == "moveTo()":
                pyautogui.moveTo(item[1],item[2])
            if item[0] == "mouseDown()":
                pyautogui.click()
                pyautogui.mouseDown()
            if item[0] == "mouseUp()":
                pyautogui.mouseUp()
    pyautogui.mouseUp()
