import os

restaurantes = [{'nome':'Bar do Armando','categoria':'Bar','ativo' : True},{'nome':'Gustavo"s','categoria':'Pizzaria','ativo' : False},{'nome':'Jeronimos','categoria':'Sushi','ativo' : True}]


def exibir_nome_do_programa():
    '''Essa função exibe o texto com o nome do restaurante
    
    Output:
    - Mensagem customizada com o nome do curso

    '''

    print("""
    ███████████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█─▄▄─█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█─██─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀
        """)

def exibir_opcoes():
    '''Essa função exibe o texto com as opções do menu principal
    
    Output:
    - Lista de opções do menu incial
    
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def escolha_opcoes():
    '''Essa função recebe a escolha do usuário e redireciona para a função correspondente
    
    Input
    - Opção escolhida pelo usuário

    Output
    - Print com a opção escolhida
    - Redirecionamento para a função correspondente a opção escolhida
    
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')
        match opcao_escolhida:
            case 1:
                cadastrar_restaurantes()
            case 2:
                listar_restaurantes()
            case 3:
                ativar_restaurantes()
            case 4:
                finalizar_app()
    except:
        opcao_invalida()

def ativar_restaurantes():
    '''Essa função altera o status de um restaurante
    Input
    - Recebe o nome do restaurante

    Output
    - Altera o status do restaurante 
    - Exibe uma mensagem de confirmação da ação
    '''
    apresenta_subtitulos("Alterar o status de um restaurante")

    nome_do_restaurante = input("Digite o nome do restaurante: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f'O restaurante {nome_do_restaurante} foi ativado') if restaurante['ativo'] else (f'O restaurante {nome_do_restaurante} foi desativado')
            print(mensagem)


    retornar_menu_anterior()

def finalizar_app():
    '''Essa função finaliza a aplicação'''
    apresenta_subtitulos("Encerrando o app.\n")
    
def opcao_invalida():
    '''Essa função exibe o texto em caso de entrada inválida'''
    print("Você digitou uma opção inválida \n")
    retornar_menu_anterior()
    
def cadastrar_restaurantes():
    '''Essa função cadastra um restaurante'''
    apresenta_subtitulos("Módulo de Cadastro de Restaurantes!\n") 
    nome_Restaurante = input("Digite o nome do restaurante que deseja cadastrar: \n")
    categoria_restaurante = input(f"Digite a categoria do restaurante {nome_Restaurante} ")
    dados = {'nome':nome_Restaurante,'categoria':categoria_restaurante,'ativo':False}
    restaurantes.append(dados)
    print(f"O Restaurante {nome_Restaurante} cadastrado com sucesso! \n")
    retornar_menu_anterior()

def listar_restaurantes():
    '''Essa função exibe a lista de todos os restaurantes'''
    apresenta_subtitulos("Módulo de Visualização dos Restaurantes Cadastrados \n")    
    for restaurante in restaurantes:
        nome_Restaurante = restaurante['nome']
        categoria_Restaurante = restaurante['categoria']
        ativo_Restaurante = restaurante['ativo']
        print(f". {nome_Restaurante} | {categoria_Restaurante} | {ativo_Restaurante}")
    retornar_menu_anterior()

def main():
    '''Essa função chama o menu inicial'''
    exibir_nome_do_programa()
    exibir_opcoes()
    escolha_opcoes()
    os.system("cls")

def retornar_menu_anterior():
    '''Essa função retorna o usuário ao menu principal'''
    input("\n Digite uma tecla para retornar ao menu anterior")
    main()    

def apresenta_subtitulos(texto):
    '''Essa função constroi subtitulos das opções do menu'''
    os.system('CLS')
    print(texto)


if __name__ == '__main__':
    main()