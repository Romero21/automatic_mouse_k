import pyautogui
import win32api 
import win32con
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

def stop_record():
    return True if win32api.GetKeyState(win32con.VK_ESCAPE)<0 else False

def play_sequence():
    return True if input("Do you wanna play your sequence? Y/N: ").lower() == "y" else False   


pyautogui.FAILSAFE = False
mouse_down_L, mouse_up_L, mouse_down_R, mouse_up_R = True, False, True, False
sequence = []
counter_rec = 0
counter_play = 0
iteration = 0
        

if __name__ == "__main__":
    answer = start_record()
    while answer:
        time.sleep(0.01)
        counter_rec += 1 
        if is_pressed_L():
            if mouse_down_L == True:
                sequence.append(["mouseDown(L)", check_positions()[0],check_positions()[1], counter_rec])
                mouse_down_L = False
                mouse_up_L = True   
        else:
            if mouse_up_L == True:
                sequence.append(["mouseUp(L)", check_positions()[0],check_positions()[1], counter_rec])
                mouse_down_L = True
                mouse_up_L = False
        if is_pressed_R():
            if mouse_down_R == True:
                sequence.append(["mouseDown(R)", check_positions()[0],check_positions()[1], counter_rec])
                mouse_down_R = False
                mouse_up_R = True   
        else:
            if mouse_up_R == True:
                sequence.append(["mouseUp(R)", check_positions()[0],check_positions()[1], counter_rec])
                mouse_down_R = True
                mouse_up_R = False
        if stop_record():
            break
    print(sequence)    
    
    if play_sequence():
        while sequence[-1][3] >= counter_play:
            if sequence[iteration][3] == counter_play:
                if sequence[iteration][0] == "mouseDown(L)":
                    pyautogui.moveTo(sequence[iteration][1],sequence[iteration][2])
                    pyautogui.mouseDown()
                if sequence[iteration][0] == "mouseUp(L)":
                    pyautogui.moveTo(sequence[iteration][1],sequence[iteration][2]) 
                    pyautogui.mouseUp()
                if sequence[iteration][0] == "mouseDown(R)":
                    pyautogui.moveTo(sequence[iteration][1],sequence[iteration][2])
                    pyautogui.mouseDown(button='right')
                if sequence[iteration][0] == "mouseUp(R)":
                    pyautogui.moveTo(sequence[iteration][1],sequence[iteration][2]) 
                    pyautogui.mouseUp(button='right')
                iteration += 1
            counter_play += 1
            time.sleep(0.00001)