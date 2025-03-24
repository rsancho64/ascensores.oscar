#! /usr/bin/python3q
 
from button import ElevatorButtonPanel
from person import Person 

class Elevator:

    def __init__(self, id, capacity, num_floors):
        self.id = id
        self.capacity = capacity
        self.current_floor = 0
        self.direction = None  # "up", "down", or None
        self.passengers = []
        self.button_panel = ElevatorButtonPanel(num_floors)

    def move(self):
        if self.direction == "up" and self.current_floor < self.button_panel.max_floor - 1:
            self.current_floor += 1
        elif self.direction == "down" and self.current_floor > 0:
            self.current_floor -= 1

    def add_passenger(self, person):
        if len(self.passengers) < self.capacity:
            self.passengers.append(person)
            self.button_panel.press_button(person.destination)
            return True
        return False

    def get_status(self):
        return {
            "id": self.id,
            "floor": self.current_floor,
            "direction": self.direction,
            "passengers": len(self.passengers)
        }

if __name__ == "__main__":

        elevator = Elevator(1, 2, 10)
        print(elevator.get_status())  # {'id': 1, 'floor': 0, 'direction': None, 'passengers': 0}
        
        elevator.direction = "up"
        elevator.move()
        
        print(elevator.get_status())  # {'id': 1, 'floor': 1, 'direction': 'up', 'passengers': 0}
        elevator.add_passenger("Alice")
        print(elevator.get_status())  # {'id': 1, 'floor': 1, 'direction': 'up', 'passengers': 1}
        elevator.move()
        
        print(elevator.get_status())  # {'id': 1, 'floor': 2, 'direction': 'up', 'passengers': 1}
        elevator.add_passenger("Bob")
        print(elevator.get_status())  # {'id': 1, 'floor': 2, 'direction': 'up', 'passengers': 2}
        elevator.move()
        
        print(elevator.get_status())  # {'id': 1, 'floor': 3, 'direction': 'up', 'passengers': 2}
        elevator.add_passenger("Charlie")
        print(elevator.get_status())  # {'id': 1, 'floor': 3, 'direction': 'up', 'passengers': 2}
        elevator.move()
        
        print(elevator.get_status())  # {'id': 1, 'floor': 4, 'direction': 'up', 'passengers': 2}
        elevator.add_passenger("David")
        print(elevator.get_status())  # {'id': 1, 'floor': 4, 'direction': 'up', 'passengers': 2}
        elevator.move()
        
        print(elevator.get_status())  # {'id': 1, 'floor': 5, 'direction': 'up', 'passengers': 2}
        elevator.add_passenger("Eve")
        print(elevator.get_status())  #
        