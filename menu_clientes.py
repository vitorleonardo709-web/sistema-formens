import os 

def limpar_tela():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def menu_clientes(clientes):
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
            clientes[id_cliente] = {'nome' : nome_cliente, 'email' : email_cliente,'telefone' :  telefone_cliente}
            
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
        Nome = {clientes[id_cliente]['nome']}
        Email = {clientes[id_cliente]['email']}
        Telefone = {clientes[id_cliente]['telefone']}
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
        Nome = {clientes[id_cliente]['nome']}
        Email = {clientes[id_cliente]['email']}
        Telefone = {clientes[id_cliente]['telefone']}
                ''')
                print('------------------------------------------')
                print('Digite os novos dados do cliente: ')
                print()
                clientes[id_cliente]['nome'] = input('Nome : ')
                clientes[id_cliente]['email'] = input('Email : ')
                clientes[id_cliente]['telefone'] = input('Telefone : ')

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
                
                excluido = clientes[id_cliente]['nome']
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
    return clientes