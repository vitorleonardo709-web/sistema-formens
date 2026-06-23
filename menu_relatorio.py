import os 

def limpar_tela():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def menu_relatorio():
    while True:
            limpar_tela()
            print(40*'#')
            print('I          ÁREA DE RELATÓRIOS          I')
            print('----------------------------------------')
            print('''>                                      <
>        1 - Imprimir relatório        <
>        0 - Voltar                    <
>                                      <''')
            print(40*'#')
            p3 = input('Digite a opção que quer acessar : ')
            
            if p3 == '1':
                limpar_tela()
                print(40*'#')
                print('I          IMPRIMIR RELATÓRIO          I')
                print('----------------------------------------')
                print('''
Nome do autor : Vitor Leonardo Santos
Curso : Sistemas de Informação - UFRN (CERES/CAICÓ)
Período : 1° Período
Email : vitor.leonardo.709@ufrn.com.br
Turma : 2026.1
''')
                print(40*'#')
                input('Aperte ENTER para voltar.')
            elif p3 == '0':
                break
            else:
                limpar_tela()
                print('Digite uma opção válida!')
                input('Pressione ENTER para voltar.')