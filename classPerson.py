class Person:
    def __init__(self, name, cpf, age, email, password):
        self.__name = name
        self.__cpf = cpf
        self.__age = age
        self.__email = email
        self.__password = password
    def getcpf(self):
        return self.__cpf
        
    def getEmail(self):
        return self.__email
    
    def getPassword(self):
        return self.__password
    
    def getName(self):
        return self.__name

#cria uma classe pessoa com nome, cpf e idade. 

class User(Person):
    def __init__(self, name, cpf, age, email, password):
        super().__init__(name, cpf, age, email, password)

#cria uma classe usuario que herda de pessoa.         

class Employee(Person):
    def __init__(self, name, id, age, registration_id, password):
        super().__init__(name, id, age)
        self.__registration_id = registration_id
        self.__password = password
    
    def getRegistrationid(self):
        return self.__registration_id

#cria uma classe empregado que herda de pessoa.        