class Computer(object):

    """docstring Computer class   
    Attributes:
        name (TYPE): Description
    """

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return 'the {} computer'.format(self.name)

    def execute(self) -> str:
        return 'executes a program'

class Synthesizer(object):

    """docstring Synthesizer class

    Attributes:
        name (TYPE): Description
    """

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return 'the {} synthesizer'.format(self.name)

    def play(self) -> str:
        return 'is playing an electronic song'

class Human(object):

    """docstring Human class

    Attributes:
        name (TYPE): Description
    """

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return '{} the human'.format(self.name)

    def speak(self) -> str:
        return 'says hello'

class Adapter(object):

    """Adapter pattern"""

    def __init__(self, obj, adapted_methods) -> None:
        self.obj = obj
        self.__dict__.update(adapted_methods)
        self.__dict__.update(self.obj.__dict__)

    def __str__(self) -> str:
        return str(self.obj)


if __name__ == '__main__':
    # Compatible objects
    objects = [Computer('Asus')]

    # Incompatible objects
    synth = Synthesizer('moog')
    human = Human('Bob')

    # Adapter pattern
    objects.append(Adapter(synth, dict(execute=synth.play)))
    objects.append(Adapter(human, dict(execute=human.speak)))

    # Visualize result
    for i in objects:
        # print('{} {}'.format(str(i), i.execute()))
        print(i.name)
