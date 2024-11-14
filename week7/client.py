class Client:
    def __init__(self, name, project, budget, vip):
        self.name = name
        self.project = project
        self.budget = budget
        self.vip = vip
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self.__name = value

    @property
    def project(self):
        return self.__project
    
    @project.setter
    def project(self, value):
        if value == '':
            raise ValueError('Project cannot be empty')
        self.__project = value

    @property
    def budget(self):
        return self.__budget
    
    @budget.setter
    def budget(self, value):
        if value <= 0:
            raise ValueError('Budget must be positive')
        self.__budget = value

    @property
    def vip(self):
        return self.__vip
    
    @vip.setter
    def vip(self, value):
        if not isinstance(value, bool):
            raise ValueError('VIP must be a boolean')
        self.__vip = value