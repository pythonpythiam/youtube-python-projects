import keyboard 
keyboard.on_press(lambda e: print(f"Key: {e.name}")) 
keyboard.wait("esc")
