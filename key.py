import keyboard


key_list = []
write_to = True
counter = 0

while True:
    counter += 1
    if keyboard.is_pressed(keyboard.read_key()):
        key = keyboard.read_key()
        if key == "esc":
            break
        elif keyboard.is_pressed(key):
            if write_to == True:
                key_list.append([f"{key}(Down)", counter])
                write_to = False
            continue
        else:
            key_list.append([f"{key}(Up)", counter])
            write_to = True
    else:
        continue
    
    

print(key_list)