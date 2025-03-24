#! /usr/bin/python3q
 
class ButtonPanel:
    def __init__(self):
        self.buttons = {}

    def press_button(self, button):
        self.buttons[button] = True

    def reset_button(self, button):
        self.buttons[button] = False

class FloorButtonPanel(ButtonPanel):
    def __init__(self):
        super().__init__()
        self.buttons = {"up": False, "down": False}

    def press_button(self, going_up):
        self.buttons["up" if going_up else "down"] = True

class ElevatorButtonPanel(ButtonPanel):
    def __init__(self, num_floors):
        super().__init__()
        self.max_floor = num_floors
        self.buttons = {i: False for i in range(num_floors)}

if __name__ == "__main__":

    fbp = FloorButtonPanel()
    fbp.press_button(True)
    fbp.press_button(False)
    print(fbp.buttons)  # {"up": True, "down": True}
    fbp.reset_button("up")
    print(fbp.buttons)  # {"up": False, "down": True}

    ebp = ElevatorButtonPanel(10)
    ebp.press_button(5)
    ebp.press_button(7)
    print(ebp.buttons)  # {0: False, 1: False, 2: False, 3: False, 4: False, 5: True, 6: False, 7: True, 8: False, 9: False}
    ebp.reset_button(5)
    print(ebp.buttons)  # {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: True, 8: False, 9: False}
    
    