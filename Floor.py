from queue import PersonQueue

class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.queue = PersonQueue()
        self.button_panel = FloorButtonPanel()

    def add_person(self, person):
        self.queue.add_person(person)
        self.button_panel.press_button(person.destination > self.floor_number)

    def get_status(self):
        return {
            "floor": self.floor_number,
            "queue_size": self.queue.size()
        }