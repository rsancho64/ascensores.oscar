#! /usr/bin/python3
 
class Building:

    def __init__(self, num_floors, num_elevators, elevator_capacity):
        self.floors = [Floor(i) for i in range(num_floors)]
        self.elevators = [Elevator(i, elevator_capacity, num_floors) for i in range(num_elevators)]
        self.time = 0

    def run_simulation(self):
        print(f"Simulación corriendo en tiempo: {self.time}")
        for elevator in self.elevators:
            elevator.move()
        self.time += 1

    def get_status(self):
        status = {"time": self.time}
        status["elevators"] = [e.get_status() for e in self.elevators]
        status["floors"] = [f.get_status() for f in self.floors]
        return statusif __name__ == "__main__":

if __name__ == "__main__":

    building = Building(5, 1, 5)
    print(building.get_status())

    building.run_simulation()
    print(building.get_status())

    building.run_simulation()
    print(building.get_status())

