#! /usr/bin/python3
 
class Person:
    
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def get_status(self):
        return {"origin": self.origin, "destination": self.destination}

if __name__ == "__main__":

    p = Person("A", "B")
    print(p.get_status())

    p2 = Person("A", "B")
    print(p2.get_status())
