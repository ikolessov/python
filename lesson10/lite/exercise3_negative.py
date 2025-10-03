class NegativeNumberError(Exception):
    def __init__(self, value, message="Число не должно быть отрицательным"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.value}"


def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError(num)
    print(f"Число {num} положительное.")
    return True

if __name__ == "__main__":
    # Положительное число
    check_positive_number(10)

    # Отрицательное число
    try:
        check_positive_number(-5)
    except NegativeNumberError as e:
        print(e)
