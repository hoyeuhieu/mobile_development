class variable:
    def __init__(self, name, roll):
        self.name = name
        self.value = roll


default_variables = []
default_variables.append(variable('SQRT', 'math.sqrt'))
default_variables.append(variable('MOD', '%'))
default_variables.append(variable('π', 'math.pi'))
default_variables.append(variable('e', 'math.e'))
default_variables.append(variable('^2', '**2'))
default_variables.append(variable('EXP', 'math.exp'))
default_variables.append(variable('ABS', 'math.fabs'))
default_variables.append(variable('^', '**'))
default_variables.append(variable('10^', '10**'))
default_variables.append(variable('log', 'np.log10'))
default_variables.append(variable('ln', 'math.log'))
default_variables.append(variable('N!', 'math.factorial'))
