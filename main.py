import abc

# "interface"
class AbsExpressao(abc.ABC):
    @abc.abstractmethod
    def interpretar(self):
        pass

#expressão terminal
class Numero(AbsExpressao): 
    def __init__(self, numero:int or float):
        self.__numero = numero

    def interpretar(self) -> int or float:
        return self.__numero

#operaração não terminal: composta por outras 2 ou mais expressoes
class Soma(AbsExpressao):
    def __init__(self, expressao_esquerda : Numero, expressao_direita : Numero):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    #interpreta a operaçao do lado esquedo e do lado direito 
    def interpretar(self) -> Numero:
        return self.__expressao_esquerda.interpretar() + self.__expressao_direita.interpretar()

class Subtracao(AbsExpressao):
    def __init__(self, expressao_esquerda: Numero, expressao_direita: Numero):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def interpretar(self) -> Numero:
        return self.__expressao_esquerda.interpretar() - self.__expressao_direita.interpretar()

class Multiplicar(AbsExpressao):
    def __init__(self, expressao_esquerda: Numero, expressao_direita: Numero):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def interpretar(self) -> Numero:
        return self.__expressao_esquerda.interpretar() * self.__expressao_direita.interpretar()


if __name__ == '__main__':

    # ((5 + 5 - 3) * 10) + 10
    #arvore ou pilha de expressoes
    resultado = Soma(Multiplicar(Subtracao(Soma(Numero(5), Numero(5)), Numero(3)), Numero(10)), Numero(10))
    print(resultado.interpretar())

    resultado2 = Soma(resultado, Numero(80))
    print(resultado2.interpretar())
    