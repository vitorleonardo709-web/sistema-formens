import os

produto = False
while True:
    os.system('cls')
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
    
    p1 = int(input('Pressione 1 para entrar no sistema! : '))
    
    if p1 == 1:
        while True:
            os.system('cls')
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
            p2 = int(input('Digite a opção que deseja entrar : '))

            if p2 == 1:
                while True:
                    os.system('cls')
                    print(40*'#')
                    print('I           ÁREA DE PRODUTOS           I')
                    print('----------------------------------------')
                    print('''>                                      <
>        1 - Cadastrar produto         <
>        2 - Procurar produto          <
>        3 - Atualizar produto         <
>        4 - Remover produto           <
>        0 - Voltar                    <
>                                      <''')
                    print(40*'#')
                    p3 = int(input('Digite a opção que quer acessar : '))
                    
                    if p3 == 1:
                        os.system('cls')
                        print(40*'#')
                        print('I     ÁREA DE CADASTRO DE PRODUTOS     I')
                        print('----------------------------------------')
                        print()
                        nome_produto = input('> Digite o nome do produto que deseja cadastrar no sistema : ')
                        preco_produto = float(input('> Digite o preco do produto : '))
                        quantidade_produto = int(input('> Digite a quantidade do produto : '))
                        produto = True
                        print()
                        print('Produto cadastrado com sucesso! [OK]')
                        print()
                        print(40*'#')
                        input('Aperte ENTER para voltar.')
                        
                    elif p3 == 2:
                        os.system('cls')
                        print(40*'#')
                        print('I           PROCURAR PRODUTO           I')
                        print('----------------------------------------')
                        print()
                        if produto == False:
                            print('Nenhum produto foi cadastrado ainda.')
                            print()
                            print(40*'#')
                            input('Aperte ENTER para voltar.')
                        else: 
                            print(f'''Produto 1 :
Nome = {nome_produto}
Preço = R$ {preco_produto}
Quantidade = {quantidade_produto}''')
                            print()
                            print(40*'#')
                            input('Aperte ENTER para voltar.')
                            
                    elif p3 == 3:
                        os.system('cls')
                        print(40*'#')
                        print('I          ATUALIZAR PRODUTOS          I')
                        print('----------------------------------------')
                        print()
                        if produto == False:
                            print('Nenhum produto cadastrado ainda!')
                            print()
                            print(40*'#')
                            input('Aperte ENTER para voltar.')
                        else:
                            print('Informações atuais do produto:')
                            print(f'''
Produto 1 :
Nome = {nome_produto}
Preço = R$ {preco_produto}
Quantidade = {quantidade_produto}
                            ''')
                            print('------------------------------------------')
                            print('Digite os novos dados do produto: ')
                            nome_produto = input('Nome : ')
                            preco_produto = float(input('Preço : '))
                            quantidade_produto = int(input('Quantidade : '))
                            print()
                            print('Produto atualizado com sucesso! [OK]')
                            print(40*'#')
                            input('Aperte ENTER para voltar.')
                            
                    elif p3 == 4:
                        os.system('cls')
                        print(40*'#')
                        print('I           EXCLUIR PRODUTO            I')
                        print('----------------------------------------')
                        print()
                        if produto == False:
                            print('Não há nenhum produto cadastrado ainda.')
                            print()
                            print(40*'#')
                            input('Pressione ENTER para voltar.')
                        else:
                            excluir = int(input(f'Excluir produto "{nome_produto}"? (1-Sim / 2-Não) : '))
                            print()
                            if excluir == 1:
                                produto = False
                                print('Produto excluido com sucesso! [X]')
                            else:
                                print('Nenhuma alteração foi feita.')
                            print(40*'#')
                            input('Pressione ENTER para voltar.')

                    elif p3 == 0:
                        break
                    else:
                        os.system('cls')
                        print('Digite uma opção válida!')
                        input('Pressione ENTER para voltar.')

            elif p2 == 2:
                while True:
                    os.system('cls')
                    print(40*'#')
                    print('I         CADASTRO DE CLIENTES          I')
                    print('----------------------------------------')
                    print('''>                                      <
>     1 - Cadastrar novos clientes     <
>     2 - Remover clientes             <
>     0 - Voltar                       <
>                                      <''')
                    print(40*'#')
                    p3 = int(input('Digite a opção que quer acessar : '))
                    
                    if p3 == 1:
                        os.system('cls')
                        print(40*'#')
                        print('I       CADASTRAR NOVOS CLIENTES       I')
                        print('----------------------------------------')
                        print()
                        print('Página interditada - Homens trabalhando...')
                        print()
                        print(40*'#')
                        input('Aperte ENTER para voltar.')
                    elif p3 == 2:
                        os.system('cls')
                        print(40*'#')
                        print('I           REMOVER CLIENTES           I')
                        print('----------------------------------------')
                        print()
                        print('Página interditada - Homens trabalhando...')
                        print()
                        print(40*'#')
                        input('Aperte ENTER para voltar.')
                    elif p3 == 0:
                        break
                    else:
                        os.system('cls')
                        print('Digite uma opção válida!')
                        input('Pressione ENTER para voltar.')

            elif p2 == 3:
                while True:
                    os.system('cls')
                    print(40*'#')
                    print('I            ÁREA DE VENDAS            I')
                    print('----------------------------------------')
                    print('''>                                      <
>       1 - Registrar nova venda       <
>       2 - Alterar venda              <
>       0 - Voltar                     <
>                                      <''')
                    print(40*'#')
                    p3 = int(input('Digite a opção que quer acessar : '))
                    
                    if p3 == 1:
                        os.system('cls')
                        print(40*'#')
                        print('I         REGISTRAR NOVA VENDA         I')
                        print('----------------------------------------')
                        print()
                        print('Página interditada - Homens trabalhando...')
                        print()
                        print(40*'#')
                        input('Aperte ENTER para voltar.')
                    elif p3 == 2:
                        os.system('cls')
                        print(40*'#')
                        print('I            ALTERAR VENDA             I')
                        print('----------------------------------------')
                        print()
                        print('Página interditada - Homens trabalhando...')
                        print()
                        print(40*'#')
                        input('Aperte ENTER para voltar.')
                    elif p3 == 0:
                        break
                    else:
                        os.system('cls')
                        print('Digite uma opção válida!')
                        input('Pressione ENTER para voltar.')

            elif p2 == 4:
                while True:
                    os.system('cls')
                    print(40*'#')
                    print('I          ÁREA DE RELATÓRIOS          I')
                    print('----------------------------------------')
                    print('''>                                      <
>        1 - Imprimir relatório        <
>        0 - Voltar                    <
>                                      <''')
                    print(40*'#')
                    p3 = int(input('Digite a opção que quer acessar : '))
                    
                    if p3 == 1:
                        os.system('cls')
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
                    elif p3 == 0:
                        break
                    else:
                        os.system('cls')
                        print('Digite uma opção válida!')
                        input('Pressione ENTER para voltar.')

            elif p2 == 0:
                break
            else:
                os.system('cls')
                print('Digite uma opção válida!')
                input('Pressione ENTER para continuar.')

    else:
        print('Fim do sistema!')
        break
