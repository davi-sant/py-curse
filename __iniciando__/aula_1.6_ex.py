
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura: "))

class Person:
    def __init__(self, nome: str, sobrenome: str, idade: int, ano_nascimento: int, maior_idade: bool, altura: float) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.ano_nascimento = ano_nascimento
        self.maior_idade = maior_idade
        self.altura = altura
        
        
def create_person(nome: str, sobrenome: str, idade: int, ano_nascimento: int, altura: float):
        if idade  < 18:
            print("Para criar uma conta você precisa ser maior de idade.")
            maior_idade: bool = False
        elif idade >= 18:
            maior_idade: bool = True
        return Person(nome, sobrenome, idade, ano_nascimento, maior_idade, altura)
    
create_person(nome, sobrenome, idade, ano_nascimento, altura)