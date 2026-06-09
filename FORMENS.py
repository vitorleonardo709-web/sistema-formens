import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

produtos = {'1' : ['Perfume kaiak', '20.0', '10'], '2' : ['Calca Jeans', '40.0','8'], '3': ['Camisa regata','45.0','5']}
clientes = {'1' : ['João Pedro', 'joaopedro@gmail.com', '8499956-7234'], '2' : ['Lucas', 'lucasbarboza@gmail.com','8499825-8462'], '3': ['Gabriel','gabrielsantos@gmail.com','8499731-9364']}
vendas = {'1' : ['João Pedro', 'Perfume kaiak', '2', '40'], '2' : ['Lucas', 'Calca Jeans','2','16'], '3': ['Gabriel','Camisa regata','1','45']}


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
                        
                       
                        produtos[codigo] = [nome_produto, preco_produto, quantidade_produto]
                        
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
Nome = {produtos[codigo][0]}
Preço = R$ {produtos[codigo][1]}
Quantidade = {produtos[codigo][2]}''')
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
Nome = {produtos[codigo][0]}
Preço = R$ {produtos[codigo][1]}
Quantidade = {produtos[codigo][2]}
                            ''')
                            print('------------------------------------------')
                            print('Digite os novos dados do produto: ')
                            produtos[codigo][0] = input('Nome : ')
                            produtos[codigo][1] = float(input('Preço : '))
                            produtos[codigo][2] = int(input('Quantidade : '))
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
                            excluido = produtos[codigo][0]
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

            elif p2 == '2':
                while True:
                    limpar_tela()
                    print(40*'#')
                    print('I          ÁREA DE CLIENTES            I')
                    print('----------------------------------------')
                    print('''>                                      <
>        1 - Cadastrar cliente         <
>        2 - Procurar cliente          <
>        3 - Atualizar cliente         <
>        4 - Remover cliente           <
>        0 - Voltar                    <
>                                      <''')
                    print(40*'#')
                    p3 = input('Digite a opção que quer acessar : ')
                    
                    if p3 == '1':
                        limpar_tela()
                        print(40*'#')
                        print('I    ÁREA DE CADASTRO DE CLIENTES      I')
                        print('----------------------------------------')
                        print()
                        id_cliente = input('Digite o ID do cliente : ')
                        nome_cliente = input('> Digite o nome do cliente : ')
                        email_cliente = input('>Digite o email do cliente :')
                        telefone_cliente = input('> Digite o telefone do cliente : ')
                        clientes[id_cliente] = [nome_cliente, email_cliente, telefone_cliente]
                        
                        print()
                        print('Cliente cadastrado com sucesso! [OK]')
                        print()
                        print(40*'#')
                        input('Aperte ENTER para voltar.')
                        
                    elif p3 == '2':
                        limpar_tela()
                        print(40*'#')
                        print('I           PROCURAR CLIENTE           I')
                        print('----------------------------------------')
                        print()
                        id_cliente = input('Digite o ID do cliente que deseja buscar : ')
                        if id_cliente in clientes:
                            print(f'''Id do cliente : {id_cliente} 
Nome = {clientes[id_cliente][0]}
Email = {clientes[id_cliente][1]}
Telefone = {clientes[id_cliente][2]}
                                ''')
                        else:
                            print('Cliente não cadastrado. [X]')
                        print()
                        print(40*'#')
                        input('Aperte ENTER para voltar.')
                            
                    elif p3 == '3':
                        limpar_tela()
                        print(40*'#')
                        print('I          ATUALIZAR CLIENTE           I')
                        print('----------------------------------------')
                        print()
                        id_cliente = input('Digite o ID do cliente que deseja atualizar : ')
                        if id_cliente in clientes:
                            print()
                            print('Informações atuais do cliente:')
                            print()
                            print(f'''
Cliente {id_cliente} :
Nome = {clientes[id_cliente][0]}
Email = {clientes[id_cliente][1]}
Telefone = {clientes[id_cliente][2]}
                            ''')
                            print('------------------------------------------')
                            print('Digite os novos dados do cliente: ')
                            print()
                            clientes[id_cliente][0] = input('Nome : ')
                            clientes[id_cliente][1] = input('Email : ')
                            clientes[id_cliente][2] = input('Telefone : ')

                            print()
                            print('Cliente atualizado com sucesso! [OK]')
                            print(40*'#')
                            input('Aperte ENTER para voltar.')   
                        else:
                            print()
                            print('Cliente não encontrado. [X]')
                            print(40*'#')
                            input('Aperte ENTER para voltar.')
                            
                    elif p3 == '4':
                        limpar_tela()
                        print(40*'#')
                        print('I           EXCLUIR CLIENTE            I')
                        print('----------------------------------------')
                        print()
                        id_cliente = input('Digite o ID do cliente que deseja excluir : ')
                        if id_cliente in clientes:
                            
                            excluido = clientes[id_cliente][0]
                            excluir = input(f'Excluir cliente "{excluido}"? (1-Sim / 2-Não) : ')
                            print()
                            if excluir == '1':
                                del clientes[id_cliente]
                                print('Cliente excluido com sucesso! [X]')
                            elif excluir =='2':
                                print('Nenhuma alteração foi feita.')
                            else:
                                print('Digite uma opção válida!')
                                
                        else:
                            print('Cliente não encontrado.')
                        print(40*'#')
                        input('Pressione ENTER para voltar.')

                    elif p3 == '0':
                        break
                    else:
                        limpar_tela()
                        print('Digite uma opção válida!')
                        input('Pressione ENTER para voltar.')
            
            elif p2 == '3':
                while True:
                    limpar_tela()
                    print(40*'#')
                    print('I             ÁREA DE VENDAS             I')
                    print('----------------------------------------')
                    print('''>                                      <
>        1 - Registrar nova venda      <
>        2 - Consultar venda           <
>        3 - Atualizar venda           <
>        4 - Cancelar venda            <
>        0 - Voltar                    <
>                                      <''')
                    print(40*'#')
                    p3 = input('Digite a opção que quer acessar : ')
                    
                    if p3 == '1':
                        limpar_tela()
                        print(40*'#')
                        print('I         REGISTRAR NOVA VENDA         I')
                        print('----------------------------------------')
                        print()
                        id_venda = input('Digite o ID da venda : ')
                        cliente_venda = input('> Nome do cliente que comprou : ')
                        produto_venda = input('> Nome do produto vendido : ')
                        quantidade_venda = int(input('> Quantidade vendida : '))
                        valor_venda = float(input('> Valor total da venda: R$ '))
                        vendas [id_venda] = [cliente_venda , produto_venda, quantidade_venda, valor_venda]
                        
                        print()
                        print('Venda registrada com sucesso! [OK]')
                        print()
                        print(40*'#')
                        input('Aperte ENTER para voltar.')
                        
                    elif p3 == '2':
                        limpar_tela()
                        print(40*'#')
                        print('I           PROCURAR VENDA            I')
                        print('----------------------------------------')
                        print()
                        id_venda = input('Digite o ID da venda : ')
                        if id_venda in vendas:
                            print(f'''
Dados da venda : {id_venda}
Nome do cliente : {vendas[id_venda][0]}
Nome do produto : {vendas[id_venda][1]}
Quantidade vendida : {vendas[id_venda][2]}
Vaalor da venda : {vendas[id_venda][3]}
                                  
                                  ''')
                            print()
                            print(40*'#')
                            input('Aperte ENTER para voltar.')
                        else: 
                            print()
                            print('Venda não cadastrada ainda.')
                            print(40*'#')
                            input('Aperte ENTER para voltar.')
                            
                    elif p3 == '3':
                        limpar_tela()
                        print(40*'#')
                        print('I           ATUALIZAR VENDA            I')
                        print('----------------------------------------')
                        print()
                        id_venda = input('Digite o ID da venda:')
                        if id_venda in vendas:
                            print()
                            print('Informações atuais da venda:')
                            print(f'''
Cliente = {vendas[id_venda][0]}
Produto = {vendas[id_venda][1]}
Quantidade = {vendas[id_venda][2]}
Valor total = R$ {vendas[id_venda][3]}
                            ''')
                            print('------------------------------------------')
                            print('Digite os novos dados desta venda: ')
                            vendas[id_venda][0] = input('Cliente : ')
                            vendas[id_venda][1] = input('Produto : ')
                            vendas[id_venda][2] = int(input('Quantidade : '))
                            vendas[id_venda][3] = float(input('Valor total : R$ '))
                            print()
                            print('Venda atualizada com sucesso! [OK]')
                            print(40*'#')
                            input('Aperte ENTER para voltar.')
                        else : 
                            print('Nenhuma venda cadastrada ainda.')
                            print(40*'#')
                            input('Aperte ENTER para voltar.')
                            
                    elif p3 == '4':
                        limpar_tela()
                        print(40*'#')
                        print('I            CANCELAR VENDA            I')
                        print('----------------------------------------')
                        print()
                        id_venda = input('Digite o ID da venda que deseja excluir : ')
                        if id_venda in vendas:
                            excluir = input(f'Deseja cancelar a venda de {vendas[id_venda][1]} para {vendas[id_venda][0]}? (1-Sim / 2-Não) : ')
                            print()
                            if excluir == '1':
                                del vendas[id_venda]
                                print('Venda excluída com sucesso! [X]')
                            elif excluir == '2':
                                print('Nenhuma alteração foi feita.')
                            else:
                                print('Digite uma opção válida!')
                            print(40*'#')
                            input('Pressione ENTER para voltar.')
                        
                        else:
                            
                            print('Não há nenhuma venda registrada ainda.')
                            print()
                            print(40*'#')
                            input('Pressione ENTER para voltar.')

                    elif p3 == '0':
                        break
                    else:
                        limpar_tela()
                        print('Digite uma opção válida!')
                        input('Pressione ENTER para voltar.')

            elif p2 == '4':
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
    
    
