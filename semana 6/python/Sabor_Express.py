print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ █▀ █▀█ █▀█ █▀▀ █▀ █▀ █▀█
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ ▄█ █▀▀ █▀▄ ██▄ ▄█ ▄█ █▄█ \n""")
# no python pode usar tanto aspas simples quanto duplas

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')
# armazena em uma variavel 
# input para interação
# f{} serve para interpolação

opcao_escolhida = input('Escolha uma opção: ')
print(f'Você escolheu a opção {opcao_escolhida}')
