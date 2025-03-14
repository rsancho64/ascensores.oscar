class PersonQueue:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def remove_person(self):
        if self.people:
            return self.people.pop(0)
        return None

    def size(self):
        return len(self.people)