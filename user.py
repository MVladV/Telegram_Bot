import math
import json

class User:

    file_users = []

    def __init__(self, name, sex=None, weight=None, age=None, growth=None, goals=None):
        self.sex = ""
        self.weight = 1
        self.age = 1
        self.growth = 1
        self.name = ""
        self.goals = ""

        if sex == "None":
            with open("parameters.json", "r") as read_file:
                info = json.load(read_file)
            for ticket in info:
                if ticket.get("Name") == name:
                    self.sex = str(self.sex1())
                    self.weight = int(self.weight1())
                    self.age = int(self.age1())
                    self.growth = int(self.growth1())
                    self.name = name
                    self.goals = str(self.goals1())
                    self.index = float(self.index1())
                    self.water = float(self.water1())
                    self.calories = int(self.calories1())
        else:    
            self.sex = sex
            self.weight = weight
            self.age = age
            self.growth = growth
            self.name = name
            self.goals = goals
            self.index = self.get_index()
            self.water = self.get_water()
            self.calories = self.get_calories()

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
        return f"Name - {self.__name}\nSex - {self.sex}\nAge - {self.__age}\nWeight - {self.weight}\nGrowth - {self.growth}\nCalories - {self.calories}\nWater - {self.water}\nIndex - {self.index}"

    def __float__(self):
        return self.index

    def get_index(self):
        return self.weight / (self.growth * self.growth)

    def get_water(self):
        if self.weight <= 50:
            return 1.5
        elif self.weight == 55:
            return 1.75
        elif self.weight == 65:
            return 2.0
        elif self.weight == 80:
            return 2.5

    def get_calories(self):
        if self.sex == "Жінка":
            if self.weight <= 50:
                return 1200
            elif self.weight == 55:
                return 1300
            elif self.weight == 65:
                return 1400
            elif self.weight == 80:
                return 1600
        else:
            if self.weight <= 50:
                return 1600
            elif self.weight == 55:
                return 1800
            elif self.weight == 65:
                return 2200
            elif self.weight == 80:
                return 2600
            

    def sex1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Name") == self.name:
                return ticket.get("Sex")
        
    def age1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Name") == self.name:
                return info.get("Age")     
    
    def weight1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Name") == self.name:
                return info.get("Weight")     
        
    def growth1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Name") == self.name:
                return info.get("Growth")     

    def goals1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Name") == self.name:
                return info.get("Goals")     

    def calories1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Name") == self.name:
                return info.get("Calories")  

    def water1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Name") == self.name:
                return info.get("Water")   

    def index1(self):
        with open("parameters.json", "r") as read_file:
            info = json.load(read_file)
        for ticket in info:
            if ticket.get("Name") == self.name:
                return info.get("Index")       

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
        self.file_users.append(user)
        with open("parameters.json", "w") as write_file:
            json.dump(self.file_users, write_file)
        write_file.close()
