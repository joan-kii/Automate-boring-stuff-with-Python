import zombiedice, random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0

        while diceRollResults is not None:
            brains += diceRollResults['brains']
            
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class Aleatorio:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            
            # Lanza de nuevo de forma aleatoria
            newRoll = random.randint(0, 1)
            if newRoll == 1:
                diceRollResults = zombiedice.roll() # Lanza de nuevo
            else:
                break

class Dos_Cerebros:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains = 0

        # Lanza de nuevo si 'brains' es menor que 2.
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # Lanza de nuevo
            else:
                break

class Dos_Escopetas:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        shotguns = 0

        # Lanza de nuevo si 'shotguns' es menor que 2.
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll() # Lanza de nuevo
            else:
                break

class Aleat_Dos_Escopetas:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        shotguns = 0
        rolls = 1

        # Elige cuantas veces lanzará entre 1 y 4, siempre que 
        # 'shotguns' sea menor que 2. 
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            numRolls = random.randint(0, 4)
            if shotguns < 2 and rolls < numRolls:
                diceRollResults = zombiedice.roll() # Lanza de nuevo
            else: 
                break

class Cerebros_vs_Escopetas:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains = 0
        shotguns = 0

        # Lanza de nuevo hasta que 'shotguns' sea mayor que 'brains'.
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']

            if shotguns < brains:
                diceRollResults = zombiedice.roll() # Lanza de nuevo
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Añade aquí los bots creados.
    Aleatorio(name='Bot Aletorio'),
    Dos_Cerebros(name='Bot Dos Cerebros'),
    Dos_Escopetas(name='Bot Dos Escopetas'),
    Aleat_Dos_Escopetas(name='Bot Aleatorio Dos Escopetas'),
    Cerebros_vs_Escopetas(name='Bot Cerebros vs Escopetas')
    )

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
