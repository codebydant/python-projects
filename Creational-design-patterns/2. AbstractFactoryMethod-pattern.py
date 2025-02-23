# PLAYER
class Frog(object):
    """docstring for Frog"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))


# OBSTACLE
class Bug(object):
    """docstring for Bug class"""

    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


# abstract factory
class FrogWorld(object):

    """docstring for FrogWorld - abstract factory"""

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Frog World -------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class GameEnvironment(object):

    """docstring for GameEnviroment (entry point of the game)

    Parameters:
        factory (Abstract Factory): receive as a input the factory abstract method

    Attributes:
        hero (TYPE): Description
        obstacle (TYPE): Description
    """

    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


if __name__ == '__main__':
    # Abstract factory
    factory = FrogWorld(name="Daniel")

    # init game
    game = GameEnvironment(factory)

    # Play game
    game.play()
