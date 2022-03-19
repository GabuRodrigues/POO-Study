from cProfile import run


class People:
    def __init__(self, name, idade, eating=False, talking=False, friend_name=None, walking=False, running=False):
        self.name = name
        self.idade = idade
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
