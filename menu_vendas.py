import os
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu_vendas(vendas):
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
            vendas [id_venda] = {'nome' : cliente_venda , 'produto' : produto_venda,'quantidade' : quantidade_venda,'valor' : valor_venda}
            
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
Nome do cliente : {vendas[id_venda]['nome']}
Nome do produto : {vendas[id_venda]['produto']}
Quantidade vendida : {vendas[id_venda]['quantidade']}
Valor da venda : {vendas[id_venda]['valor']}
                        
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
Cliente = {vendas[id_venda]['nome']}
Produto = {vendas[id_venda]['produto']}
Quantidade = {vendas[id_venda]['quantidade']}
Valor total = R$ {vendas[id_venda]['valor']}
                ''')
                print('------------------------------------------')
                print('Digite os novos dados desta venda: ')
                vendas[id_venda]['nome'] = input('Cliente : ')
                vendas[id_venda]['produto'] = input('Produto : ')
                vendas[id_venda]['quantidade'] = int(input('Quantidade : '))
                vendas[id_venda]['valor'] = float(input('Valor total : R$ '))
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
                excluir = input(f'Deseja cancelar a venda de {vendas[id_venda]['produto']} para {vendas[id_venda]['nome']}? (1-Sim / 2-Não) : ')
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
    return vendas 