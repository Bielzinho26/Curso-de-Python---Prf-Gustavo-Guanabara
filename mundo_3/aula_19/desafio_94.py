"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.

No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todas as pessoas com idade acima da média.
"""

person_dict = dict()
general_info = list()
counter = 0

while True:
    person_dict['name'] = input("Nome: \n")

    # sex = input("Sexo  [M/F]: \n")
    # sex = sex[0:1].upper()
    # person_dict['sex'] = sex

    general_info.append(person_dict.copy())

    leave = input("Continuar? [S/N] \n")
    if leave[0] == "N":
        break
print(f"Dicionários: {general_info}")
for dictionary in general_info:
    counter += len(dictionary)
print(counter)