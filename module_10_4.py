from threading import Thread
from queue import Queue
from time import sleep

import random


class Table:
    def __init__(self):
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        eating_time = random.randint(3, 10)
        print(f'{self.name} сел(-а) за стол и кушает')
        sleep(eating_time)
        print(f'{self.name} покушал(-а) и ушел(ушла)')


class Cafe:
    def __init__(self, table_count):
        self.tables = [Table() for _ in range(table_count)]
        self.queue = Queue()

    def guest_arrival(self, guests):
        for guest_name in guests:
            guest = Guest(guest_name)
            self.queue.put(guest)
            print(f'{guest_name} в очереди')

    def serve_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for index, table in enumerate(self.tables):
                if table.guest is not None and not table.guest.is_alive():
                    print(f'Стол номер {index + 1} свободен')
                    table.guest = None
                if table.guest is None and not self.queue.empty():
                    new_guest = self.queue.get()
                    table.guest = new_guest
                    print(f'{new_guest.name} вышел(-а) из очереди и сел(-а) за стол номер {index + 1}')
                    new_guest.start()


cafe = Cafe(table_count=6)
cafe.guest_arrival(['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Viktoria', 'Nikita', 'Galina', 'Pavel'])
cafe.serve_guests()
