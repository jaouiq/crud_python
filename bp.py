# importa biblioteca
import os

# inserir pessoas na lista
pessoas = []

while True:
    # usuário informa pessoas 
    nova_pessoa = input('Digite o nome da pessoa que deseja inserir na lista ou aperte Enter para encerrar e exibir a lista: ')

# verifica se o usuário inseriu nova pessoa
    if nova_pessoa != '':
        pessoas.append(nova_pessoa)
        continue
    else:
        break

# limpa console
os.system('cls')

# ordena a lista de pessoas em ordem alfábetica
print(f'{'-'*30}LISTA DE PESSOAS{'-'*30}\n')
pessoas.sort()

for pessoa in pessoas:
        print(pessoa)

# usuário informa a pessoa a ser deletada       
pessoa_deletada = input('Nome do usuário a ser deletado: ')
os.system('cls')

# deleta o usuário informado
try:
    pessoas.remove(pessoa_deletada)
except:
    print('Não foi possível deletar o usuário.')

print(f'{'-'*30}LISTA DE PESSOAS{'-'*30}\n')
pessoas.sort()

for pessoa in pessoas:
        print(pessoa)

# encerra o programa
print('Programa encerrado. Obrigado por usar!')



    

