from datetime import datetime


class People:
    today = datetime.today()
    current_year = today.year

    def __init__(self, name, age, eating=False, talking=False, friend_name=None, walking=False, running=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking
        self.walking = walking
        self.friend_name = friend_name
        self.running = running

    def eat(self, food):
        if self.eating:
            print(f"{self.name} is already eating")
            return
        print(f"{self.name} is eating {food}")
        self.eating = True

    def talk(self, friend_name):
        if self.talking:
            print(f"Now, {self.name} is talking to {friend_name}")
            return
        print(f"{self.name} is talking to {friend_name}")
        self.talking = True
        self.friend_name = friend_name

    def walk(self, region):
        if self.walking:
            self.run()
            return
        print(f"{self.name} is walking in {region}")
        self.walking = True

    def run(self):
        if self.running:
            print(f"{self.name} is already running")
            return
        print(f"{self.name} is running")
        self.running = True
    
    @classmethod
    def get_year_of_birth (cls, name, age):
        year_of_birth = cls.current_year - age
        print(f"name: {name}, year_of_birth: {year_of_birth}")
        return cls(name, age)
