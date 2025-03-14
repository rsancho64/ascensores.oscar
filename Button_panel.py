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