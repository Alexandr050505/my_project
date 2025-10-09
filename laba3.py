# === ЗАДАНИЕ 1 ===
print("\n--- Задание 1: Квадраты чисел ---")
squares = [x ** 2 for x in range(1, 11)]
print("Квадраты чисел от 1 до 10:", squares)

# === ЗАДАНИЕ 2 ===
print("\n--- Задание 2: Четные числа ---")
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print("Четные числа от 1 до 19:", even_numbers)

# === ЗАДАНИЕ 3 ===
print("\n--- Задание 3: Работа со строками ---")
words = ["python", "Java", "c++", "Rust", "go"]
filtered_words = [word.upper() for word in words if len(word) > 3]
print("Слова в верхнем регистре длиннее 3 символов:", filtered_words)

# === ЗАДАНИЕ 4 ===
print("\n--- Задание 4: Итератор Countdown ---")


class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

n = int(input("Введите число для обратного отсчета: "))

print(f"Обратный отсчет от {n}:")
for x in Countdown(n):
    print(x, end=" ")
print()

# === ЗАДАНИЕ 5 ===
print("\n--- Задание 5: Числа Фибоначчи ---")


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


print("Первые 5 чисел Фибоначчи:")
for num in fibonacci(5):
    print(num, end=" ")
print()

# === ЗАДАНИЕ 6 ===
print("\n--- Задание 6: Финансовый калькулятор ---")
from decimal import Decimal, getcontext

getcontext().prec = 10


def calculate_deposit():
    print("Введите данные для расчета вклада:")

    # Ввод данных с клавиатуры
    initial_amount = Decimal(input("Введите начальную сумму вклада (рубли.копейки): "))
    interest_rate = Decimal(input("Введите годовую процентную ставку (например, 7.5): "))
    years = Decimal(input("Введите срок вклада (в годах): "))

    monthly_rate = interest_rate / (12 * 100)
    months = years * 12
    final_amount = initial_amount * (1 + monthly_rate) ** months
    final_amount = final_amount.quantize(Decimal('0.01'))
    profit = final_amount - initial_amount

    print(f"Начальная сумма: {initial_amount} руб.")
    print(f"Итоговая сумма: {final_amount} руб.")
    print(f"Общая прибыль: {profit} руб.")


calculate_deposit()
# === ЗАДАНИЕ 7 ===
print("\n--- Задание 7: Дроби ---")
from fractions import Fraction

frac1 = Fraction(3, 4)
frac2 = Fraction(5, 6)

print(f"Дробь 1: {frac1}")
print(f"Дробь 2: {frac2}")

addition = frac1 + frac2
subtraction = frac1 - frac2
multiplication = frac1 * frac2
division = frac1 / frac2

print(f"Сложение: {frac1} + {frac2} = {addition}")
print(f"Вычитание: {frac1} - {frac2} = {subtraction}")
print(f"Умножение: {frac1} × {frac2} = {multiplication}")
print(f"Деление: {frac1} ÷ {frac2} = {division}")

# === ЗАДАНИЕ 8 ===
print("\n--- Задание 8: Дата и время ---")
from datetime import datetime

now = datetime.now()
print("Текущая дата и время:", now)
print("Только текущая дата:", now.date())
print("Только текущее время:", now.time())

# === ЗАДАНИЕ 9 ===
print("\n--- Задание 9: Разница дат ---")
from datetime import date

birthday = date(2005, 5, 5)  # год, месяц, день
today = date.today()

days_passed = (today - birthday).days

next_birthday = date(today.year, birthday.month, birthday.day)
if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_to_birthday = (next_birthday - today).days

print(f"День рождения: {birthday}")
print(f"Сегодня: {today}")
print(f"Дней прошло с рождения: {days_passed}")
print(f"Дней до следующего дня рождения: {days_to_birthday}")

# === ЗАДАНИЕ 10 ===
print("\n--- Задание 10: Форматирование даты ---")


def format_datetime(dt):
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }

    day = dt.day
    month = months[dt.month]
    year = dt.year
    time = dt.strftime("%H:%M")

    return f"Сегодня {day} {month} {year} года, время: {time}"


current_time = datetime.now()
formatted_string = format_datetime(current_time)
print(formatted_string)