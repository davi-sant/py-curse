#tipodedados #boolean

"""_boolean_
    int (inteiro). Vamos quebrar isso em partes:

    type(age): Esta expressão retorna o tipo da variável age. Por exemplo, se age for um número inteiro, type(age) retornará <class 'int'>.

    type(age) == int: Isso compara se o tipo da variável age é igual ao tipo int. Se age for um número inteiro, essa expressão será avaliada como True.

    not type(age) == int: O operador not inverte o resultado da comparação. 
    Portanto, se o tipo de age não for igual a int, a expressão será avaliada como True. 
    Isso significa que o bloco de código dentro do if será executado se age não for um número inteiro.
"""

def check_age(age: int) -> int:
    
    # se idade for igual a 29 siginifica que é  -> true
    if not type(age) == int:
        print("Por favor informe uma idade valida.")
        return age 
    if  age == 29: 
        print("Essa é minha idade.")
        return age
    print("Ops idade errada.")
    return age
    
check_age(29)