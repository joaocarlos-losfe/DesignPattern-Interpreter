import abc
from telnetlib import DO

# classe abstrata
class AbsExpressao(abc.ABC):
    @abc.abstractmethod
    def interpretar(self):
        pass

#expressão terminal
class Digito(AbsExpressao): 
    def __init__(self, numero:int or float):
        self.__numero = numero

    def interpretar(self) -> int or float:
        return self.__numero

#operaração não terminal: composta por outras 2 ou mais expressoes
class Soma(AbsExpressao):
    def __init__(self, expressao_esquerda:Digito, expressao_direita:Digito):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    #interpreta a operaçao do lado esquedo e do lado direito 
    def interpretar(self):
        return self.__expressao_esquerda.interpretar() + self.__expressao_direita.interpretar()

class Subtracao(AbsExpressao):
    def __init__(self, expressao_esquerda:Digito, expressao_direita:Digito):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def interpretar(self):
        return self.__expressao_esquerda.interpretar() - self.__expressao_direita.interpretar()

class Multiplicar(AbsExpressao):
    def __init__(self, expressao_esquerda:Digito, expressao_direita:Digito):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def interpretar(self):
        return self.__expressao_esquerda.interpretar() * self.__expressao_direita.interpretar()


if __name__ == '__main__':

    # ((5 + 5 - 3) * 10) + 10
    # arvore de expressoes
    resultado = Soma(Multiplicar(Subtracao(Soma(Digito(5), Digito(5)), Digito(3)), Digito(10)), Digito(10))
    print(resultado.interpretar())

    resultado2 = Soma(resultado, Digito(80))
    print(resultado2.interpretar())

    s = Soma(Digito(10), Digito(5))

    print(s.interpretar())

    print("-------Resposta do Quiz---------");
    #expressão: ((3 * 6) + (40 - 10) ) + ((5-2) * 10)
    #forma 1
    print("Forma 1: ")
    resultado = Soma(Soma(Multiplicar(Digito(3), Digito(6)), Subtracao(Digito(40), Digito(10))), Multiplicar(Subtracao(Digito(5), Digito(2)), Digito(10)))
    print(resultado.interpretar())
    print("\n");
    #forma 2
    lado1 = Soma(Multiplicar(Digito(3), Digito(6)), Subtracao(Digito(40), Digito(10)))
    lado2 = Multiplicar(Subtracao(Digito(5), Digito(2)), Digito(10))

    print(lado1.interpretar())
    print(lado2.interpretar())
    s = Soma(lado1, lado2)
    print(s.interpretar())

    
    