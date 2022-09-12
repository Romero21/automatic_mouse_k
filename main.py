import pyautogui
import win32api
import os 
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


positions = []
start_t = []


if __name__ == "__main__":
    positions.append(["mouse", check_positions()[0],check_positions()[1]])
    answer = start_record()
    while answer:
        if is_pressed_L():
            start_t.append(time.time())
            m_pos = check_positions()
        else:
            try:
                if m_pos != "":
                    positions.append(["mouse", m_pos[0], m_pos[1]]) 
                    positions.append(["click", m_pos[0], m_pos[1]]) 
                    positions.append(["sec", "{:.2f}".format(start_t[0]-time.time())])
                m_pos = ""
                start_t = []
            except:
                pass

        if is_pressed_L() and is_pressed_R():
            break

        print(positions)

    
    if play_sequence():
        for item in positions:
            if item[0] == "mouse":
                pyautogui.moveTo(item[1],item[2])
            if item[0] == "click":
                pyautogui.click()
            if item[0] == "sec":
                pass

