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