from copy import deepcopy

# frutas = ["laranja", "maca", "uva"]
# frutas_novas = ["banana", "abacaxi", "uva"]

# frutas.extend(frutas_novas)
# frutas.pop()

# print(frutas)  # Saída: ['laranja', 'maca', 'uva', 'banana', 'abacaxi']


# numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
# print(numeros)

# nomes1 = ("Diogo", "Maria", "João", "Diogo")

# carros = ("gol",)

# print(isinstance(carros, tuple))  # Saída: False

# convidados = [{"nome": "pedro", "idade": 19, "is_man": True}, {"nome": "maria",
#                                                                "idade": 20, "is_man": False}, {"nome": "joao", "idade": 21, "is_man": True}]


# nomes_capitalize = [p["nome"].capitalize() for p in convidados]
# print(nomes_capitalize)

pessoa = [{
    "nome": "Diogo",
            "idade": 19,
            "is_man": True,
            "parents": {
                "mae": {
                    "nome": "Maria",
                    "idade": 40,
                },
                "pai": {
                    "nome": "João",
                    "idade": 51,
                }

            },

},
    {
    "nome": "Maria",
            "idade": 20,
            "is_man": False
},
    {
    "nome": "João",
            "idade": 21,
            "is_man": True
}

]

# for chave, valor in pessoa[0].items():
#     print(chave, valor)

# pessoa2 = deepcopy(pessoa)
# pessoa2[0]["idade"] = 90

# print()

# for chave, valor in pessoa2[0].items():
#     print(chave, valor)

# print()

# for chave, valor in pessoa[0].items():
#     print(chave, valor)

# for p in pessoa:
#     for chave, valor in p.items():
#         print(chave, valor, sep=": ")


# def diz_oi(nome, idade, profissao, *args, **kwargs):
#     print(args)
#     print(kwargs)

#     if kwargs.get("cidade"):
#         return f'Oi {nome}, você tem {idade} anos e é um {profissao} da {kwargs["cidade"]}'

#     return f'Oi {nome}, você tem {idade} anos e é um {profissao}'


# print(diz_oi('Diogo', 19, 'medico', cidade='São Paulo'))


# def soma(a, b):
#     return (a + b)


# def soma_55(a, b, func):
#     resultado = func(a, b) + 55
#     return print(resultado)


# soma_55(1, 1, soma)


class Funcionario:
    def __init__(self, nome, profissao):
        self.nome = nome
        self.profissao = profissao
        self._salario = 0
        self._bonificacao = 0

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("O salário não pode ser negativo")
        self._salario = valor

    @property
    def bonificacao(self):
        return self._bonificacao

    @bonificacao.setter
    def bonificacao_ou_desconto(self, valor):
        self._bonificacao = valor

    def _calcular_imposto(self):
        if self._salario <= 1100:
            return self._salario * 0.05
        elif self._salario <= 2500:
            return self._salario * 0.10
        return self._salario * 0.15

    @property
    def salario_liquido(self):
        return self._salario - self._calcular_imposto() + self._bonificacao

    def __str__(self):
        return f"{self.nome} é um {self.profissao} e recebe {self.salario_liquido:.2f} R$ líquidos"


nome = input("Informe o nome do funcionario: ")
profissao = input("Informe a profissão do funcionario: ")
salario = input("Informe o salário do funcionario: ")
bonificacao = input(
    "Informe a bonificação ou desconto com sinal negativo se houver: ")
funcionario = Funcionario(nome.capitalize(), profissao)
funcionario.salario = float(salario)
funcionario.bonificacao_ou_desconto = float(bonificacao)
print(funcionario)
