import os
import pickle
from arquivos import*
from menu_produtos import menu_produtos
from menu_clientes import menu_clientes
from menu_vendas import menu_vendas
from menu_relatorio import menu_relatorio
#######################################################################
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#######################################################################
produtos = recupera_produtos()

clientes = recupera_clientes()

vendas = recupera_vendas()
#######################################################################

while True:
    limpar_tela()
    print(50*'#')
    
    print('''
#####  #####  #####  #   #  #####  #   #  #####
#      #   #  #   #  ## ##  #      ##  #  #    
#####  #   #  #####  # # #  #####  # # #  #####
#      #   #  #  #   #   #  #      #  ##      #
#      #####  #   #  #   #  #####  #   #  #####
          ''')
    print(50*'#')
    print()
    
    p1 = input('Pressione 1 para entrar no sistema ou 0 para sair ! : ')
    
    if p1 == '1':
        while True:
            limpar_tela()
            print(40*'#')
            print('I          OPÇÕES DO SISTEMA           I')
            print('----------------------------------------')
            print('''>                                      <
>            1 - Produtos              <
>            2 - Clientes              <
>            3 - Vendas                <
>            4 - Relatório             <
>            0 - Sair                  <
>                                      <''')
            print(40*'#')
            p2 = input('Digite a opção que deseja entrar : ')

            if p2 == '1':
                produtos = menu_produtos(produtos)

            elif p2 == '2':
                clientes = menu_clientes(clientes)
            
            elif p2 == '3':
                vendas = menu_vendas(vendas)
            
            elif p2 == '4':
                menu_relatorio()

            elif p2 == '0':
                break
            else:
                limpar_tela()
                print('Digite uma opção válida!')
                input('Pressione ENTER para continuar.')
    elif p1 =='0' :
        print('Você saiu do sistema! Até mais.') 
        break
    else:
        limpar_tela()
        print('Digite uma opção válida')
        input('Pressione Enter para voltar')

print('Fim dos trabalhos , salvando...')

salva_produtos(produtos)
salva_clientes(clientes)
salva_vendas(vendas)
