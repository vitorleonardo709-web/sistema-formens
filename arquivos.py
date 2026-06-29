import os 
import pickle


def recupera_produtos():
    try:
        arq_produtos = open("produtos.dat", "rb")
        produtos = pickle.load(arq_produtos)
        arq_produtos.close()  
    except:
        produtos = {
            '1' : {'nome' : 'Perfume kaiak','preco' : 20.0,'quantidade' : 10}, 
            '2' : {'nome' : 'Calca Jeans','preco' :  40.0,'quantidade' : 8}, 
            '3': {'nome' : 'Camisa regata','preco' : 45.0,'quantidade' : 5}}
        arq_produtos = open("produtos.dat", "wb")
        pickle.dump(produtos, arq_produtos)
        arq_produtos.close()
    return produtos



def recupera_clientes():
    try:
        arq_clientes = open("clientes.dat", "rb")
        clientes = pickle.load(arq_clientes)
        arq_clientes.close() 
    except:
        clientes = {
            '1' : {'nome' : 'João Pedro', 'email' : 'joaopedro@gmail.com','telefone' : '8499956-7234', 'ativo' : True}, 
            '2' : {'nome' : 'Lucas', 'email' : 'lucasbarboza@gmail.com','telefone' : '8499825-8462', 'ativo' : True}, 
            '3' : {'nome' : 'Gabriel','email' : 'gabrielsantos@gmail.com','telefone' : '8499731-9364', 'ativo' : True}}
        arq_clientes = open("clientes.dat", "wb")
        pickle.dump(clientes, arq_clientes)
        arq_clientes.close()
    return clientes



import pickle

def recupera_vendas():
    try:
        arq_vendas = open("vendas.dat", "rb")
        vendas = pickle.load(arq_vendas)
        arq_vendas.close() 
    except:
        vendas = {
            '1' : {'id_cliente' : '1', 'codigo' : '1', 'quantidade' : 2, 'valor' : 40.0}, 
            '2' : {'id_cliente' : '2', 'codigo' : '2', 'quantidade' : 2, 'valor' : 16.0}, 
            '3' : {'id_cliente' : '3', 'codigo' : '3', 'quantidade' : 1, 'valor' : 45.0}
        } 
        arq_vendas = open("vendas.dat", "wb")
        pickle.dump(vendas, arq_vendas)
        arq_vendas.close()
    return vendas



def salva_produtos(produtos):
    arq_produtos = open("produtos.dat", "wb")
    pickle.dump(produtos, arq_produtos)
    arq_produtos.close()

def salva_clientes(clientes):
    arq_clientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

def salva_vendas(vendas):
    arq_vendas = open("vendas.dat", "wb")
    pickle.dump(vendas, arq_vendas)
    arq_vendas.close()