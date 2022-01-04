import math


class Sleep:

    def __init__(self, hours, name):
        self.hours = hours
        self.name = name

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        if hours <= 0:
            raise TypeError
        if not isinstance(hours, int):
            raise TypeError
        self.__hours = hours

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name = name    

    def __str__(self):
        return f"You must sleep - {self.__hours} hours today. Go to the bed."

    def __float__(self):
        return self.__hours


    @staticmethod
    def hours(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Hours")    

    @staticmethod
    def name(name_of_file):
        with open(name_of_file, "r") as read_file:
            info = json.load(read_file)
        return info.get("Name")        

    def add_user(self):  # add to .json file
        sleep = {
            "Hours": self.hours,
            "Name": self.name
        }
        self.file_tickets.append(sleep)
        with open("sleep.json", "w") as write_file:
            json.dump(self.file_tickets, write_file)
        write_file.close()


  
        

  