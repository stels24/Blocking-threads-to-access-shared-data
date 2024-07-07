import threading

lock = threading.Lock()


class BankAccount:
    def __init__(self, surplus=1000):
        self.surplus = surplus

    def deposit(self, summa):
        with lock:
            self.surplus += summa
        print(f'Deposited {summa}, new balance {self.surplus}')

    def withdraw(self, summa):
        with lock:
            self.surplus -= summa
        print(f'Withdrew {summa}, new balance {self.surplus}')


def deposit_task(account, summa):
    for _ in range(5):
        account.deposit(summa)


def withdraw_task(account, summa):
    for _ in range(5):
        account.withdraw(summa)


account = BankAccount(1000)

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

