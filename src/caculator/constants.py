class variable:
    def __init__(self, name, roll):
        self.name = name
        self.value = roll


default_variables = []
default_variables.append(variable('x', '*'))
default_variables.append(variable('abs', 'math.abs'))