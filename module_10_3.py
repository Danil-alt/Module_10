from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            amount = randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}')
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
                sleep(0.001)

    def take(self):
        for i in range(100):
            amount = randint(50, 500)
            print(f'Запрос на {amount}')
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонен, недостаточно средств')
                    self.lock.acquire()
                sleep(0.001)


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')