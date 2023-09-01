import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class Momento:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'moment : {self.value}'


class BankAccount:
    def __init__(self, balance: int = 0) -> None:
        logger.info(f'init account with balance: {balance}')
        self.balance = balance

    def deposit(self, amount):
        logger.info(f'deposit {amount}')
        self.balance += amount
        return Momento(self.balance)

    def restore(self, momento: Momento):
        logger.info(f'restore to << {momento}')
        self.balance = momento.value

    def __str__(self) -> str:
        return f'balance: {self.balance}'


if __name__ == '__main__':
    bk = BankAccount(100)

    m1 = bk.deposit(20)
    m2 = bk.deposit(20)
    logger.info(bk)

    bk.restore(m1)
    logger.info(bk)
