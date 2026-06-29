import os 

def limpar_tela():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def menu_relatorio(vendas, clientes, produtos):
    while True:
        limpar_tela()
        print(40*'#')
        print('I          ÁREA DE RELATÓRIOS          I')
        print('----------------------------------------')
        print('''>                                      <
>        1 - Listagem Geral            <
>        2 - Listagem com Filtro       <
>        3 - Filtro e Processamento    <
>        4 - Combinação de Dados       <
>        0 - Voltar                    <
>                                      <''')
        print(40*'#')

        escolha = input('Digite a opção que deseja acessar : ')
        if escolha == '1':
            print()
            limpar_tela()
            print(40*'#')
            print('I           LISTAGEM GERAL             I')
            print('----------------------------------------')
            print('> Listar todos os Produtos(1),Clientes(2) ou Vendas(3)?')
            print()
            print(40*'#')
            print()
            listar = input('O que você deseja listar? (1/2/3): ')
            print()
            
            if listar == '1':
                if len(produtos) == 0:
                    print('Não há produtos cadastrados!')
                else:
                    print('=== CÓDIGO === | === NOME === | === PREÇO === | === ESTOQUE ===')
                    for codigo in produtos:
                        nome = produtos[codigo]['nome']
                        preco = produtos[codigo]['preco']
                        quantidade = produtos[codigo]['quantidade']
                        
                        print(f"      {codigo}        | {nome} | R$ {preco:.2f} |   {quantidade} unidades ")
            
            elif listar == '2':
                if len(clientes) == 0:
                    print('Nenhum cliente cadastrado!')
                else:
                    print('=== ID DO CLIENTE === | === NOME === | === EMAIL === | === TELEFONE === | === STATUS ===')
                    
                    for id_cliente in clientes:
                        nome = clientes[id_cliente]['nome']
                        email = clientes[id_cliente]['email']
                        telefone = clientes[id_cliente]['telefone']
                        
                        if clientes[id_cliente]['ativo'] == True:
                            status = "Ativo"
                        else:
                            status = "Inativo"

                        print(f"        {id_cliente}             | {nome}   | {email} | {telefone} | {status} ")
                    
            elif listar == '3':
                if len(vendas) == 0:
                    print('Nenhuma venda registrada!')
                else:
                    print('=== ID DA VENDA === | === NOME DO CLIENTE === | === NOME DO PRODUTO === | === QUANTIDADE === | === VALOR TOTAL ===')
                    
                    for id_venda in vendas:
                        id_cliente = vendas[id_venda]['id_cliente']
                        codigo = vendas[id_venda]['codigo']
                        quantidade = vendas[id_venda]['quantidade']
                        valor = vendas[id_venda]['valor']
                        nome_cliente = clientes[id_cliente]['nome']
                        nome_produto = produtos[codigo]['nome']
                        
                        print(f" {id_venda}    |  {nome_cliente}      | {nome_produto}      | {quantidade}      | R$ {valor:.2f} ")
            
            else:
                print('Opção inválida!')
            print()
            print(40*'#')
            input('Pressione ENTER para voltar.')
        elif escolha == '2':
            limpar_tela()
            print(40*'#')
            print('I         LISTAGEM COM FILTRO          I')
            print('----------------------------------------')
            print('1 - Clientes Inativos.')
            print('2 - Produtos abaixo de R$ 40,00.')
            print()
            print(40*'#')
            
            escolha_filtro = input('Qual filtro deseja aplicar? (1/2): ')
            print()
            
            if escolha_filtro == '1':
                limpar_tela()
                print('=== ID === | === NOME === | === EMAIL === | === TELEFONE ===')
                
                encontrou = False
                
                for id_cliente in clientes:
                    if clientes[id_cliente]['ativo'] == False: 
                        encontrou = True
                        nome = clientes[id_cliente]['nome']
                        email = clientes[id_cliente]['email']
                        telefone = clientes[id_cliente]['telefone']
                        
                        print(f'    {id_cliente}      | {nome} | {email} | {telefone}')
                        
                if encontrou == False:
                    print("Não há nenhum cliente inativo no momento.")
                    
            elif escolha_filtro == '2':
                limpar_tela()
                print('=== CÓDIGO ===  | === NOME ===  | === PREÇO ===  |  === ESTOQUE ===')
                encontrou = False
                for codigo in produtos:
                    if produtos[codigo]['preco'] < 40:
                        encontrou = True
                        nome = produtos[codigo]['nome']
                        preco = produtos[codigo]['preco']
                        quantidade = produtos[codigo]['quantidade']
                        
                        print(f"      {codigo}         | {nome} | R$ {preco:.2f}     | {quantidade} unidades ")
                        
                if encontrou == False:
                    print("Nenhum produto custando menos de R$ 40,00 no estoque.")
            
            else:
                print("Opção inválida.")
                
            print()
            print(40*'#')
            input('Pressione ENTER para voltar.')
        
        elif escolha == '3':
            limpar_tela()
            print(40*'#')
            print('I    FILTRO E PROCESSAMENTO DE DADOS   I')
            print('----------------------------------------')
            print()
            desconto = float(input('Digite a porcentagem de desconto (ex: 10, 20) : '))
            valor_maximo = float(input('Mostrar produtos que fiquem abaixo de R$ : '))
            print()
            
            print('=== CÓDIGO === | === NOME === | === PREÇO NOVO ===')
            
            for codigo in produtos:
                preco_original = produtos[codigo]['preco']
                valor_desconto = preco_original * (desconto / 100)
                preco_novo = preco_original - valor_desconto
                if preco_novo < valor_maximo:
                    nome = produtos[codigo]['nome']
                    print(f"      {codigo}        | {nome} | R$ {preco_novo:.2f} ")
                    
            print()
            print(40*'#')
            input('Pressione ENTER para voltar.')
        
        elif escolha == '4':
            limpar_tela()
            print(40*'#')
            print('I         COMBINAÇÃO DE DADOS          I')
            print('----------------------------------------')
            print('Escolha quais dados dos CLIENTES(ativos) deseja ver:')
            print()
            print('Apenas nome e telefone (1) ou apenas nome e email (2)')
            print()
            print(40*'#')
            print()
            filtro = input('Digite a sua opção (1/2): ')
            print()
            
            if filtro == '1':
                limpar_tela()
                print('=== NOME === | === TELEFONE ===')
                encontrou = False
                for id_cliente in clientes:
                    if clientes[id_cliente]['ativo'] == True:
                        encontrou = True
                        nome = clientes[id_cliente]['nome']
                        telefone = clientes[id_cliente]['telefone']
                        print(f" {nome} | {telefone} ")
                if encontrou == False:
                    print('Nenhum cliente ativo cadastrado!')
            
            elif filtro == '2':
                limpar_tela()
                print('=== NOME === | === E-MAIL ===')
                encontrou = False
                for id_cliente in clientes:
                    if clientes[id_cliente]['ativo'] == True:
                        encontrou = True
                        nome = clientes[id_cliente]['nome']
                        email = clientes[id_cliente]['email']
                        print(f" {nome} | {email} ")
                if encontrou == False:
                    print('Nenhum cliente ativo cadastrado!')
                    
            else:
                print('Opção inválida.')
                
            print()
            print(40*'#')
            input('Pressione ENTER para voltar.')
        elif escolha =='0':
            break
        else:
            print('Digite uma resposta válida! ')
            input('Pressione ENTER para voltar.')

