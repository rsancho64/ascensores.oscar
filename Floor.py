#! /usr/bin/python3
 
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
        }if __name__ == "__main__":

if __name__ == "__main__":
    
    f = Floor(0)
    f.add_person("Alice")
    f.add_person("Bob")
    f.add_person("Charlie")
    print(f.get_status())  # {"floor": 0, "queue_size": 3}
    print(f.queue.remove_person())  # Alice
    print(f.get_status())  # {"floor": 0, "queue_size": 2}
    print(f.queue.remove_person())  # Bob
    print(f.queue.remove_person())  # Charlie
    print(f.queue.remove_person())  # None
    print(f.get_status())  # {"floor": 0, "queue_size": 0}

