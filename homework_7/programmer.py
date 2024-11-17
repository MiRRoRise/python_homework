class Programmer:

    def __init__(self, name, position):
        """Конструктор для инициализации человека"""

        # Проверка на валидность для имени
        if not isinstance(name, str):
            raise ValueError("Имя должно быть строкой")

        # Проверка на пустоту
        if not name.strip():
            raise ValueError("Имя не может быть пустым")

        # Проверка на валидность для должности
        if position not in ["Junior", "Middle", "Senior"]:
            raise ValueError("Возможны только следующие должности: Junior, Middle, Senior")

        self.__name = name
        self.__position = position
        self.__salary = 0
        self.__up = 0
        self.__working = 0

        # Начало истории работы
        self.__data_work = []
        self.__data_work.append(f"{self.__name} в должности {self.__position} теперь работает в компании")

    @property
    def get_name(self):
        """Получаем имя работника"""
        return self.__name

    @property
    def get_position(self):
        """Получаем должность работника"""
        return self.__position

    @property
    def get_salary(self):
        """Получаем зарплату работника"""
        return self.__salary

    def work(self, time):
        """Добавляем время работы"""

        # Проверки на валидность
        if not isinstance(time, int):
            raise ValueError("Количество часов должно быть целым числом")
        if time < 0:
            raise ValueError("Количество часов не может быть отрицательным")

        self.__working += time
        if self.__position == "Junior":
            self.__salary += time * 10
        elif self.__position == "Middle":
            self.__salary += time * 15
        elif self.__position == "Senior":
            self.__salary += time * (20 + self.__up) # Учитываем возможное "повышение" Senior
        self.__data_work.append(f"{self.__name} проработал {time} часов")

    def bonus(self, amount):
        """Выдаем бонус работнику"""

        # Проверки на валидность
        if not isinstance(amount, int):
            raise ValueError("Бонус должен быть целым числом")
        if amount < 0:
            raise ValueError("Бонус не может быть отрицательным")

        self.__salary += amount
        self.__data_work.append(f"{self.__name} получил бонус {amount} тугриков")

    def rise(self):
        """Повышение работника"""

        if self.__position == "Junior":
            self.__position = "Middle"
            self.__data_work.append(f"{self.__name} повысился до {self.__position}")
        elif self.__position == "Middle":
             self.__position = "Senior"
             self.__data_work.append(f"{self.__name} повысился до {self.__position}")
        elif self.__position == "Senior":
            self.__up += 1 # Оклад Senior увеличивается при "повышении"
            self.__data_work.append(f"{self.__name} получил надбавку")

    def info(self):
        """Получаем информацию о работнике"""
        return f"{self.__name} {self.__working}ч. {self.__salary} тгр."

    def salary(self):
        """Выдаем зарплату и обнуляем текущую"""

        money = self.__salary
        self.__salary = 0
        self.__data_work.append(f"{self.__name} получил зарплату в размере {money}")
        return money

    def stat(self):
        """Выводим историю работника"""

        print(f"История работника {self.__name}:")
        for data in self.__data_work:
            print(data)

def main():
    programmer = Programmer("Васильев Иван", "Junior")
    programmer.work(750)
    print(programmer.info())
    programmer.rise()
    programmer.work(500)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())
    print()
    programmer.stat()

if __name__ == "__main__":
    main()
