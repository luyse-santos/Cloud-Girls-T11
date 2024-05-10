import os
# importando uma biblioteca

restaurantes = ['Pizza', 'Sushi']

# cria uma lista de dados
# tupla = () tambem servem para armazenar dados ,mas sao dados imutaveis e tem um desempenho melhor

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

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()
# função para simplificar

def finalizar_app():
    exibir_subtitulo('finalizar app')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')
    main()
# main() faz voltar ao menu principal
    
def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu_principal()

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)
    # int para tranformar string em número
    
    if opcao_escolhida == 1:
        cadastrar_novo_restaurante() 
    elif opcao_escolhida == 2:
        listar_restaurantes()
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    elif opcao_escolhida == 4: 
        finalizar_app()
    else:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

# função main(principal)

if __name__ == '__main__':
    main()
# condicional main
