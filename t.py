teste1 = {'a': 't1'}
teste2 = {'b': 't2'}

class Teste():

    def __init__(self):
        self.teste = teste1 | teste2

    def get_teste(self):
        print(self.teste)
    

t = Teste()
t.get_teste()