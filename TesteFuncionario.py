"""
    Criação de objetos e chamadas dos métodos
"""
from Funcionario import Funcionario

funcionario = Funcionario('Antonio', 'tonhão@email.com')

print(funcionario)

funcionario.cadastro_hora('Janeiro', 280)
funcionario.cadastro_hora('Fevereiro', 220)
funcionario.cadastro_salario_hora('Janeiro', 250)
funcionario.cadastro_salario_hora('Fevereiro', 250)
print(funcionario.calcula_salario('Janeiro'))
print(funcionario)
print(funcionario.calcula_salario('Fevereiro'))
print(funcionario)
