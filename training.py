import math


class Training:

    def __init__(self, calories=1, water=1):
        self.calories = calories
        self.water = water

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

    def __str__(self):
        return f"You must eat - {self.__calories} today.\nYou need to drink {self.__water} liters."

    def __float__(self):
        return self.__calories
        

  