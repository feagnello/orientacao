class Pessoa:
    "Isto é uma nova classe chamada Pessoa"
    
    idade = 15
    
    def saudacao(sef):   #def é uma função/comportamento da classe 'Pessoa'
        print("Olá Pessoas!")
        
print(Pessoa.idade) #atributo estático 
print(Pessoa.saudacao)

objetoPessoa = Pessoa()

objetoPessoa.saudacao()
print(objetoPessoa.idade)
print(objetoPessoa.saudacao)