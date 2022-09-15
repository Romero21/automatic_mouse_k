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


sequence = []
timer = []
m_pos = []


if __name__ == "__main__":
    sequence.append(["mouse", check_positions()[0],check_positions()[1]])
    answer = start_record()
    start_time = time.time()
    write_sequence = False
    while answer:
        if is_pressed_L():
            timer.append(time.time())
            m_pos.append(check_positions())
            write_sequence = True
        else:
            #try:
                #if m_pos[0] != "0":
            if write_sequence:
                sequence.append(["sec_run", float("{:.1f}".format(timer[0] - start_time)), "click", m_pos[0][0], m_pos[0][1], m_pos[-1][0], m_pos[-1][1], float("{:.2f}".format(time.time() - timer[0]))])
                write_sequence = False
                #m_pos[0] = "0"
            m_pos = []
            timer = []   
            #except:
                #pass
            

        if is_pressed_L() and is_pressed_R():
            break

        print(sequence)

    
    if play_sequence():
        start_time = time.time()
        for item in sequence:
            if item[0] == "mouse":
                pyautogui.moveTo(item[1],item[2])
            if item[0] == "sec_run":
                while not float("{:.1f}".format(time.time() - start_time)) == item[1]:
                    #print(float("{:.1f}".format(time.time() - start_time)), item[1])
                    pass
            #if item[2] == "click":
                pyautogui.moveTo(item[3], item[4])
                #pyautogui.click()
            #try:
                #if item[7] > 0.50:
                
                #print("click")
                if item[7] > 0.50:
                    pyautogui.mouseDown()
                    time.sleep(item[7])
                    pyautogui.moveTo(item[5], item[6])
                    pyautogui.mouseUp()
                else:
                    pyautogui.click()
            #except:
             #   pass
                    
            #time.sleep(0.01)
    