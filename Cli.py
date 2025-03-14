from building import Building

class CLISimulator:
    def __init__(self, num_floors=5, num_elevators=1, elevator_capacity=5):
        self.building = Building(num_floors, num_elevators, elevator_capacity)

    def run(self):
        while True:
            command = input("Comando (run, status, exit): ").strip().lower()
            if command == "run":
                self.building.run_simulation()
            elif command == "status":
                print(self.building.get_status())
            elif command == "exit":
                break