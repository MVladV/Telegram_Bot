import math
import json


# Клас для зберігання даних користувача
class User:

    def __init__(self, name, sex=None, weight=None, age=None, growth=None, goals=None):
        # Стать
        self.sex = ""
        # Вага
        self.weight = 1
        # Вік
        self.age = 1
        # Зріст
        self.growth = 1
        # Ім'я
        self.name = name
        # Ціль тренуваннь
        self.goals = ""
        # Індекс маси тіла
        self.index = 0
        # Кількість води на добу
        self.water = 0
        # Кількість калорій на добу
        self.calories = 0

        if sex == "None":
            with open("parameters.json", "r") as read_file:
                info = json.load(read_file)
            for person in info:
                if person.get("Name") == name:
                    self.sex1()
                    self.weight1()
                    self.age1()
                    self.growth1()
                    self.goals1()
                    self.index1()
                    self.water1()
                    self.calories1()
        else:
            self.sex = sex
            self.weight = weight
            self.age = age
            self.growth = growth
            self.goals = goals
            self.get_index()
            self.get_water()
            self.get_calories()

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if not isinstance(sex, str):
            raise TypeError
        self.__sex = sex

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight <= 0:
            raise ZeroDivisionError
        if not isinstance(weight, int):
            raise TypeError
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ZeroDivisionError
        if not isinstance(age, int):
            raise TypeError
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

    @property
    def goals(self):
        return self.__goals

    @goals.setter
    def goals(self, goals):
        if not isinstance(goals, str):
            raise TypeError
        self.__goals = goals

    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self, growth):
        if growth <= 0:
            raise ZeroDivisionError
        if not isinstance(growth, int):
            raise TypeError
        self.__growth = growth

    def __str__(self):
        return f"Name - {self.__name}\nSex - {self.sex}\nAge(your group) - {self.__age}\nWeight(your group) - {self.weight}\nGrowth(your group) - {self.growth}\nCalories - {self.calories}\nWater - {self.water}\nIndex - {self.index}"

    def __float__(self):
        return self.index

    # Функція для обчислення індексу
    def get_index(self):
        self.index = self.weight / (self.growth * self.growth)

    # Функція для обчислення кількості води
    def get_water(self):
        if self.weight <= 50:
            self.water = 1.5
        elif self.weight == 55:
            self.water = 1.75
        elif self.weight == 65:
            self.water = 2.0
        elif self.weight == 80:
            self.water = 2.5

    # Функція для обчислення кількості калорій
    def get_calories(self):
        if self.sex == "Жінка":
            if self.weight <= 50:
                self.calories = 1200
            elif self.weight == 55:
                self.calories = 1300
            elif self.weight == 65:
                self.calories = 1400
            elif self.weight == 80:
                self.calories = 1600
        else:
            if self.weight <= 50:
                self.calories = 1600
            elif self.weight == 55:
                self.calories = 1800
            elif self.weight == 65:
                self.calories = 2200
            elif self.weight == 80:
                self.calories = 2600

    # Отримання даних з файлу
    def sex1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for person in info:
            if person.get("Name") == self.name:
                self.sex = person.get("Sex")

    def age1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for person in info:
            if person.get("Name") == self.name:
                self.age = person.get("Age")

    def weight1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for person in info:
            if person.get("Name") == self.name:
                self.weight = person.get("Weight")

    def growth1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for person in info:
            if person.get("Name") == self.name:
                self.growth = person.get("Growth")

    def goals1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for person in info:
            if person.get("Name") == self.name:
                self.goals = person.get("Goals")

    def calories1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for person in info:
            if person.get("Name") == self.name:
                self.calories = person.get("Calories")

    def water1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for person in info:
            if person.get("Name") == self.name:
                self.water = person.get("Water")

    def index1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for person in info:
            if person.get("Name") == self.name:
                self.index = person.get("Index")

    # Запис нового користувача до файлу
    def add_user(self):  # add to .json file
        user = {
            "Name": self.name,
            "Sex": self.sex,
            "Age": self.age,
            "Weight": self.weight,
            "Growth": self.growth,
            "Goals": self.goals,
            "Index": self.index,
            "Water": self.water,
            "Calories": self.calories
        }
        with open("parameters.json", "r") as read_file:
            try:
                data = json.load(read_file)
            except Exception as e:
                data = []
        read_file.close()
        data.append(user)
        with open("parameters.json", "w") as write_file:
            json.dump(data, write_file)
        write_file.close()
