#typecoercion

# Dado um input de dados faça uma soma qualquer se atentando para os tipo ultilizados. 
nome = input("Digite seu nome: ")
nota_01 = input("Digite sua nota: ")
nota_02 = input("Digite a sua nota 02: ")


class Student:
    def __init__(self, nome: str, nota_01: float, nota_02: float):
        self.nome = nome
        self.nota_01 = nota_01
        self.nota_02 = nota_02
        
def create_student(nome: str, nota_01: float, nota_02: float) :
    return Student(nome, nota_01, nota_02)

student =  create_student(nome, float(nota_01), float(nota_02))

def avarege() -> None :
    sum_avarege = (student.nota_01 + student.nota_02) / 2
    return print(f"Ola {student.nome} sua media é de {sum_avarege.real}")
       
avarege()