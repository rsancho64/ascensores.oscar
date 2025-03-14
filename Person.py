class Person:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def get_status(self):
        return {"origin": self.origin, "destination": self.destination}