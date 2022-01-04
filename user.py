import math


class User:

    def __init__(self, sex, weight = 1, age, growth, name = "User", goals):
        with open(event.name_of_file, "r") as read_file:
            info = json.load(read_file)
        self.sex = sex
        self.weight = weight
        self.age = age
        self.growth = growth
        self.name = name
        self.goals = goals
        self.index = 0
        self.get_index()

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if not isinstance(calories, str):
            raise TypeError
        self.__calories = calories

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
        if age <= 10:
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
    def growth(self, int):
        if growth <= 10:
            raise ZeroDivisionError
        if not isinstance(growth, int):
            raise TypeError
        self.__growth = growth            

    def __str__(self):
        return f"Name - {self.__name}\nSex - {self.sex}\nAge - {self.__age}\nWeight - {self.weight}\nGrowth - {self.growth}\n"

    def __float__(self):
        return self.index

    def get_index():
        self.index = self.weight / (self.growth * self.growth)    
        
    @staticmethod
    def name(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Name")     

    @staticmethod
    def sex(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Sex")     
        
    @staticmethod
    def age(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Age")     
    
    @staticmethod
    def weight(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Weight")     
        
    @staticmethod
    def growth(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Growth")     

    @staticmethod
    def goals(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Goals")           

    def add_user(self):  # add to .json file
        user = {
            "Name": self.event.name,
            "Sex": self.number,
            "Age": self.type_t,
            "Weight": self.days,
            "Growth": self.price,
            "Index": self.index,
            "Goals": self.goals
        }
        self.file_tickets.append(user)
        with open("parameters.json", "w") as write_file:
            json.dump(self.file_tickets, write_file)
        write_file.close()


  