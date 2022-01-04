import math


class Food:

    def __init__(self, calories=1, water=1, name):
        self.calories = calories
        self.water = water
        self.name = name

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        if calories <= 0:
            raise TypeError
        if not isinstance(calories, int):
            raise TypeError
        self.__calories = calories

    @property
    def water(self):
        return self.__water

    @water.setter
    def water(self, water):
        if not water:
            raise ZeroDivisionError
        if not isinstance(water, int):
            raise TypeError
        self.__water = water

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name = name    

    def __str__(self):
        return f"You must eat - {self.__calories} today.\nYou need to drink {self.__water} liters."

    def __float__(self):
        return self.__calories

    @staticmethod
    def water(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Water")  

    @staticmethod
    def calories(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Calories")    

    @staticmethod
    def name(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Name")        

    def add_user(self):  # add to .json file
        food = {
            "Water": self.water,
            "Calories": self.calories,
            "Name": self.name
        }
        self.file_tickets.append(food)
        with open("food.json", "w") as write_file:
            json.dump(self.file_tickets, write_file)
        write_file.close()


  
        

  