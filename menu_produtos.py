import os

def limpar_tela():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def menu_produtos(produtos):
    while True:
        limpar_tela()
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
        p3 = input('Digite a opção que quer acessar : ')
        
        if p3 == '1':
            limpar_tela()
            print(40*'#')
            print('I     ÁREA DE CADASTRO DE PRODUTOS     I')
            print('----------------------------------------')
            print()
            
            codigo = input('> Digite o código do produto : ')
            nome_produto = input('> Digite o nome do produto : ')
            preco_produto = float(input('> Digite o preco do produto : '))
            quantidade_produto = int(input('> Digite a quantidade do produto : '))
            
        
            produtos[codigo] = {'nome' : nome_produto,'preco' : preco_produto,  'quantidade' : quantidade_produto}
            
            print()
            print('Produto cadastrado com sucesso! [OK]')
            print()
            print(40*'#')
            input('Aperte ENTER para voltar.')
            
        elif p3 == '2':
            limpar_tela()
            print(40*'#')
            print('I           PROCURAR PRODUTO           I')
            print('----------------------------------------')
            print()
            
            codigo = input('> Digite o código do produto que deseja buscar : ')
            print()
            
            
            if codigo in produtos:
                print(f'''Produto Encontrado :
Código = {codigo}
Nome = {produtos[codigo]['nome']}
Preço = R$ {produtos[codigo]['preco']}
Quantidade = {produtos[codigo]['quantidade']}''')
            else: 
                print('Esse código ainda não  foi cadastrado. ')
                
            print()
            print(40*'#')
            input('Aperte ENTER para voltar.')
                
        elif p3 == '3':
            limpar_tela()
            print(40*'#')
            print('I          ATUALIZAR PRODUTOS          I')
            print('----------------------------------------')
            print()
            
            codigo = input('> Digite o código do produto que deseja atualizar : ')
            print()
            
            if codigo in produtos:
                print('Informações atuais do produto:')
                print(f'''
Nome = {produtos[codigo]['nome']}
Preço = R$ {produtos[codigo]['preco']}
Quantidade = {produtos[codigo]['quantidade']}
                ''')
                print('------------------------------------------')
                print('Digite os novos dados do produto: ')
                produtos[codigo]['nome'] = input('Nome : ')
                produtos[codigo]['preco'] = float(input('Preço : '))
                produtos[codigo]['quantidade'] = int(input('Quantidade : '))
                print()
                print('Produto atualizado com sucesso! [OK]')
            else:
                print('Produto não encontrado!')
                
            print(40*'#')
            input('Aperte ENTER para voltar.')
                
        elif p3 == '4':
            limpar_tela()
            print(40*'#')
            print('I           EXCLUIR PRODUTO            I')
            print('----------------------------------------')
            print()
            
            codigo = input('> Digite o código do produto que deseja excluir : ')
            print()
            
            if codigo in produtos:
                excluido = produtos[codigo]['nome']
                excluir = (input(f'Excluir produto "{excluido}"? (1-Sim / 2-Não) : '))
                print()
                if excluir == '1':
                    del produtos[codigo] 
                    print('Produto excluido com sucesso! [X]')
                elif excluir =='2':
                    print('Nenhuma alteração foi feita.')
                else:
                    print('Digite uma opção válida!')
            else:
                print('Produto não encontrado!')
                
            print(40*'#')
            input('Pressione ENTER para voltar.')

        elif p3 == '0':
            break
        else:
            limpar_tela()
            print('Digite uma opção válida!')
            input('Pressione ENTER para voltar.')   
    return produtos