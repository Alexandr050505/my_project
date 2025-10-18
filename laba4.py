class Transport:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Transport is moving at {self.speed} km/h")

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"


class Car(Transport):

    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def honk(self):
        print("Beep beep!")

    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")

    def __str__(self):
        return f"Car: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"

    def __len__(self):
        return self.seats

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False

    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        elif isinstance(other, (int, float)):
            return self.speed + other
        else:
            return NotImplemented


class Bike(Transport):

    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.type = bike_type

    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")

    def __str__(self):
        return f"Bike: {self.brand}, Speed: {self.speed}, Type: {self.type}"


# 4. Практика использования
if __name__ == "__main__":
    print("=== Создание объектов ===")

    # Создание объектов разных классов
    transport1 = Transport("Generic", 60)
    car1 = Car("Toyota", 120, 5)
    car2 = Car("BMW", 140, 4)
    bike1 = Bike("Trek", 25, "mountain")

    print("\n=== Вывод информации о объектах (__str__) ===")
    print(transport1)
    print(car1)
    print(car2)
    print(bike1)

    print("\n=== Проверка работы методов move() и honk() ===")
    transport1.move()
    car1.move()
    bike1.move()
    car1.honk()

    print("\n=== Использование len(car) ===")
    print(f"Количество мест в {car1.brand}: {len(car1)}")

    print("\n=== Сравнение двух машин (car1 == car2) ===")
    print(f"{car1.brand} == {car2.brand}: {car1 == car2}")

    print("\n=== Сложение скоростей двух машин (car1 + car2) ===")
    total_speed = car1 + car2
    print(f"Суммарная скорость {car1.brand} и {car2.brand}: {total_speed} km/h")

    print("\n=== Попытка сложить машину и велосипед ===")
    try:
        result = car1 + bike1
        print(f"Результат: {result}")
    except TypeError as e:
        print(f"Ошибка: {e}")
        print(
            "Объяснение: Метод __add__ в классе Car не поддерживает сложение с объектами класса Bike, поэтому возвращается NotImplemented")

    # 5. Дополнительное задание
    print("\n=== Дополнительное задание ===")
    vehicles = [
        Transport("Generic", 50),
        Car("Honda", 110, 5),
        Car("Mercedes", 130, 4),
        Bike("Giant", 20, "road"),
        Bike("Specialized", 30, "mountain")
    ]

    print("Вызов метода move() для всех транспортных средств:")
    for vehicle in vehicles:
        vehicle.move()

    print("\nПринцип ООП, который демонстрируется: ПОЛИМОРФИЗМ")
    print(
        "Разные объекты (Transport, Car, Bike) могут отвечать на один и тот же метод (move()) по-разному, в зависимости от их конкретного класса.")