class Player:
    def __init__(self, name):
        self.name = name

    def greetPlayer(self):
        print("Hello, " + self.name)


print("What is your name?")
name = input()
playerOne = Player(name)

playerOne.greetPlayer()