class variable:
    def __init__(self, name, roll):
        self.name = name
        self.value = roll


default_variables = []
default_variables.append(variable('x', '*'))
default_variables.append(variable('sqrt', 'math.sqrt'))
default_variables.append(variable('mod', '%'))