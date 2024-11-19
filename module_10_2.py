from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.name} сражается {days} дней, осталось {enemies} воинов.')
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


knight1 = Knight('Артур', 10)
knight2 = Knight('Ланселот', 15)

knight1.start()
knight2.start()

knight1.join()
knight2.join()
