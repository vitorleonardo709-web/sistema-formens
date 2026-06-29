import os
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu_vendas(vendas, clientes, produtos):
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
            if id_venda in vendas:
                print()
                print('Essa venda já existe!')
                input('Pressione ENTER para voltar')
                continue
            
            id_cliente = input('Digite o ID do cliente que vai comprar : ')
            if id_cliente not in clientes or clientes[id_cliente]['ativo'] == False:
                print('Cliente não encontrado ou inativo!')
                print()
                print(40*'#')
                input('Pressione ENTER para voltar.')
                continue

            codigo = input('Digite o código do produto : ')
            if codigo not in produtos:
                print('Produto não encontrado !')
                print()
                print(40*'#')
                input('Pressione ENTER para voltar.')
                continue

            quantidade_venda = int(input('>Digite a quantidade vendida : '))
            if quantidade_venda > produtos[codigo]['quantidade']:
                print()
                print('Estoque insuficiente para venda! ')
                print(f"O estoque atual do {produtos[codigo]['nome']} é de {produtos[codigo]['quantidade']} . ")
                print(40*'#')
                input('Pressione ENTER para voltar.')
                continue

            produtos[codigo]['quantidade'] -= quantidade_venda
            valor_venda = quantidade_venda * produtos[codigo]['preco']
            print(f"Valor da venda : {valor_venda:.2f}")
            
            vendas [id_venda] = {'id_cliente': id_cliente, 'codigo': codigo,'quantidade': quantidade_venda,'valor': valor_venda}
            
            print()
            print('Venda registrada com sucesso!')
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
                id_cliente = vendas[id_venda]['id_cliente']
                codigo = vendas[id_venda]['codigo']
                
                print(f'''
Dados da venda : {id_venda}
Nome do cliente : {clientes[id_cliente]['nome']}
Nome do produto : {produtos[codigo]['nome']}
Quantidade vendida : {vendas[id_venda]['quantidade']}
Valor da venda : R$ {vendas[id_venda]['valor']:.2f}
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
                id_cliente = vendas[id_venda]['id_cliente']
                codigo = vendas[id_venda]['codigo']
                quantidade_antiga = vendas[id_venda]['quantidade']
                
                print()
                print('Informações atuais da venda:')
                print(f'''
Cliente = {clientes[id_cliente]['nome']}
Produto = {produtos[codigo]['nome']}
Quantidade = {quantidade_antiga}
Valor total = R$ {vendas[id_venda]['valor']:.2f}
                ''')
                print('------------------------------------------')
                print('Digite os novos dados desta venda: ')
                novo_id_cliente = input('Novo ID do Cliente : ')
                if novo_id_cliente not in clientes or clientes[novo_id_cliente]['ativo'] == False:
                    print('Cliente inválido ou inativo!')
                    input('Aperte ENTER para voltar.')
                    continue

                nova_quantidade = int(input('Digite a nova quantidade : '))
            
                diferenca = nova_quantidade - quantidade_antiga
                if diferenca > produtos[codigo]['quantidade']:
                    print('Estoque insuficiente para esse aumento!')
                    input('Aperte ENTER para voltar.')
                    continue
                produtos[codigo]['quantidade'] -= diferenca
                novo_valor = nova_quantidade * produtos[codigo]['preco']
                
                vendas[id_venda]['id_cliente'] = novo_id_cliente
                vendas[id_venda]['quantidade'] = nova_quantidade
                vendas[id_venda]['valor'] = novo_valor
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
                id_cliente = vendas[id_venda]['id_cliente']
                codigo = vendas[id_venda]['codigo']
                nome_produto = produtos[codigo]['nome']
                nome_cliente = clientes[id_cliente]['nome']
                excluir = input(f"Deseja cancelar a venda de {nome_produto} para {nome_cliente}? (1-Sim / 2-Não) : ")
                print()
                if excluir == '1':
                    quantidade_devolvida = vendas[id_venda]['quantidade']
                    if codigo in produtos:
                        produtos[codigo]['quantidade'] += quantidade_devolvida
                        print('Estoque devolvido com sucesso!')
                    else:
                        print('O produto inexistente, o estoque não foi devolvido.')
                    
                    del vendas[id_venda]
                    print('Venda excluída com sucesso! ')
            
            else:
                print('Não há nenhuma venda registrada com esse ID.')
                print()
                print(40*'#')
                input('Pressione ENTER para voltar.')

        elif p3 == '0':
            break
        else:
            limpar_tela()
            print('Digite uma opção válida!')
            input('Pressione ENTER para voltar.')
    return vendas,clientes, produtos 