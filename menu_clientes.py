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
            
            if id_cliente in clientes:
                print()
                print('Esse cliente já está cadastrado!')
                print()
                print(40*'#')
                input('pressione ENTER para voltar!')
                continue
            
            nome_cliente = input('> Digite o nome do cliente : ').strip()

            while len(nome_cliente) == 0 or not nome_cliente.replace(" ", "").isalpha() : 
                print('Digite um nome válido')
                nome_cliente = input('> Digite o nome do cliente : ').strip()


            email_cliente = input('>Digite o email do cliente :')

            while '@' not in email_cliente or '.' not in email_cliente:
                print("Email inválido!, precisa do '@' e do ponto final incluidos'.'  tente novamente : ")
                email_cliente = input('>Digite o email do cliente :')


            telefone_cliente = input('> Digite o telefone do cliente : ').strip()
            
            while len(telefone_cliente) < 8 or len(telefone_cliente) >= 12 or not(telefone_cliente).isdigit():
                print('Telefone inválido, certifique-se de que o número tenha mais de oito dígitos e contenha apenas números!')
                telefone_cliente = input('> Digite o telefone do cliente : ').strip()
            
            clientes[id_cliente] = {'nome' : nome_cliente, 'email' : email_cliente,'telefone' :  telefone_cliente, 'ativo' : True}
            
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
            print('Busca por ID(1) ou nome(2)?')
            busca = input('Digite uma opção : ')
            
            if busca == '1':
                id_cliente = input('Digite o ID do cliente que deseja buscar : ')
                if id_cliente in clientes and clientes[id_cliente]['ativo'] == True : 
                    print(f'''Id do cliente : {id_cliente} 
            Nome = {clientes[id_cliente]['nome']}
            Email = {clientes[id_cliente]['email']}
            Telefone = {clientes[id_cliente]['telefone']}
                        ''')
                else:
                    print()
                    print('Cliente não cadastrado ou inativo!')

            
            elif busca == '2':
                busca_nome = input('Digite uma letra ou parte do nome do cliente : ').lower()
                print()
                encontrado = False
                for id_cliente in clientes:
                    if clientes[id_cliente]['ativo'] == True: 
                        nome_cliente = clientes[id_cliente]['nome'].lower()
                        if busca_nome in nome_cliente:
                            print(f"ID : {id_cliente} -- Nome : {clientes[id_cliente]['nome']}")
                            encontrado = True
                if not encontrado:
                    print('Cliente não encontrado. ')
            
            else:
                print('Digite uma opção válida!.')
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
                if clientes[id_cliente]['ativo'] == True:
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
                    print('Este cliente está inativo!')
                    input('Pressione ENTER  para voltar ')
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
                    clientes[id_cliente]['ativo'] = False
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