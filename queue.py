#! /usr/bin/python3

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

if __name__ == "__main__":
    queue = PersonQueue()
    queue.add_person("Alice")
    queue.add_person("Bob")
    queue.add_person("Charlie")
    print(queue.size())  # 3
    print(queue.remove_person())  # Alice
    print(queue.size())  # 2
    print(queue.remove_person())  # Bob
    print(queue.remove_person())  # Charlie
    print(queue.remove_person())  # None
    print(queue.size())  # 0
