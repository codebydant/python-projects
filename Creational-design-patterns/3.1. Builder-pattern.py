class Computer(object):

    """docstring for Computer class

    Attributes:
        gpu (TYPE): Description
        hdd (TYPE): Description
        info (TYPE): Description
        memory (TYPE): Description
        serial (TYPE): Description
    """

    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None  # in gigabytes
        self.hdd = None  # in gigabytes
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)

    __repr__ = __str__


# builder pattern
class ComputerBuilder(object):

    """doctstring for Computer builder class

    Attributes:
        computer (TYPE): Description
    """

    def __init__(self):
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


# Director
class HardwareEngineer(object):

    """docstring for HardwareEngineer class

    Attributes:
        builder (TYPE): Description
    """

    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        (self.builder.configure_memory(memory), self.builder.configure_hdd(hdd), self.builder.configure_gpu(gpu))
        # [step for step in (self.builder.configure_memory(memory), self.builder.configure_hdd(hdd), self.builder.configure_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer


if __name__ == '__main__':
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
    computer = engineer.computer
    print(computer)
