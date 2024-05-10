import os
# importando uma biblioteca
def exibir_nome_do_programa():
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ █▀ █▀█ █▀█ █▀▀ █▀ █▀ █▀█
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ ▄█ █▀▀ █▀▄ ██▄ ▄█ ▄█ █▄█ \n""")
# no python pode usar tanto aspas simples quanto duplas

def exibir_opcoes():
    
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n') 

def escolher_opcao():

    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)
    # int para tranformar string em número
    
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    else:
        finalizar_app()
# condicional

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
# função main(principal)

if __name__ == '__main__':
    main()
# condicional main
