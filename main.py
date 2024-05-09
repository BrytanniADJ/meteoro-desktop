# imports principais
import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QTableWidget, QErrorMessage
from sqlite3 import Cursor
import mysql
import mysql.connector
from mysql.connector import Error
import mysql.connector
from tkinter import *

app = QtWidgets.QApplication([])
# conexão com banco de dados
banco = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = '123456',
    database = 'meteoro_calcados'
)

# definição de funções (telas) login.ui
def chamar_principal():
    global usuario
    login.close()
    principal.show()
    principal.text_usu.setText(f"{usuario}")
# pag-inicial.ui
def inicial_estoque(): # cadastros
    principal.close()
    cadastros.close()
    estoque.show()

def cadastros_inicial(): # cadastro de produtos
    principal.close()
    cadastros.show()

def disconect():
    principal.close()
    login.show()

def exit():
    login.close()

def cadastros_inicial():
    principal.close()
    cadastros.show()

# exit das páginas
def exit_geral():
    principal.close()
    estoque.close()
    cadastros.close()
    login.show

def voltar():
    estoque.close()
    cadastros.close()
    principal.show()

def buscarProd():
    import mysql.connector

    # Estabelecer a conexão com o banco de dados
    banco = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='123456',
        database='meteoro_calcados'
    )
    cursor = banco.cursor()

    colunas = f"nome_produto, tamanho_produto, modelo_produto, cor_produto, marca_produto, preco_custo, preco_venda, qtd_produto"
    prodCod = cadastros.prodCod.text()

    try:
        query = f"SELECT {colunas} FROM produtos WHERE cod_produto = {prodCod}"
        cursor.execute(query)

        selecao = cursor.fetchall()

        prodNome = cadastros.prodNome.setText(str(selecao[0][0]))
        prodTamanho = cadastros.boxTamanho.setText(str(selecao[0][1]))
        prodModelo = cadastros.prodModelo.setText(str(selecao[0][2]))
        prodCor = cadastros.prodCor.setText(str(selecao[0][3]))
        prodMarca = cadastros.prodMarca.setText(str(selecao[0][4]))
        prodPrecoCusto = cadastros.prodPrecoCusto.setText(str(selecao[0][5]))
        prodPrecoVenda = cadastros.prodPrecoVenda.setText(str(selecao[0][6]))
        prodQtd = cadastros.prodQuant.setText(str(selecao[0][7]))
    except:
        erro_produto = QtWidgets.QErrorMessage()
        erro_produto.showMessage('Código não existente')
        erro_produto.exec_()
def buscarFun():
    import mysql.connector

    # Estabelecer a conexão com o banco de dados
    banco = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='123456',
        database='meteoro_calcados'
    )
    cursor = banco.cursor()

    if cadastros.radioCliente.isChecked():
        tabela = 'cliente'
    else:
        tabela = 'funcionario'

    colunas = f"nome_{tabela}, sobrenome_{tabela}, cpf_{tabela}, telefone_{tabela}, email_{tabela}, endereco_{tabela}"
    funCod = cadastros.funCod.text()

    try:
        query = f"SELECT {colunas} FROM {tabela} WHERE cod_{tabela} = {funCod}"
        cursor.execute(query)

        selecao = cursor.fetchall()

        funNome = cadastros.funNome.setText(str(selecao[0][0]))
        funSobre = cadastros.funSobre.setText(str(selecao[0][1]))
        funCPF = cadastros.funCPF.setText(str(selecao[0][2]))
        funTell = cadastros.funTell.setText(str(selecao[0][3]))
        funEmail = cadastros.funEmail.setText(str(selecao[0][4]))
        endCod = cadastros.endCod.setText(str(selecao[0][5]))

        buscarFun2()
        
    except:
        erro_login = QtWidgets.QErrorMessage()
        erro_login.showMessage('Código não existente')
        erro_login.exec_()

def buscarFun2():
    cursor = banco.cursor()
    endCod = cadastros.endCod.text()

    colunas = f"cep, estado, cidade, bairro, rua, numero_casa"
    query = f"SELECT {colunas} FROM endereco WHERE cod_endereco = {endCod}"
    cursor.execute(query)
    selecao = cursor.fetchall()
    cursor.close()

    endCep = cadastros.funCep.setText(str(selecao[0][0]))
    endEstado = cadastros.funEstado.setText(str(selecao[0][1]))
    endCidade = cadastros.funCidade.setText(str(selecao[0][2]))
    endBairro = cadastros.funBairro.setText(str(selecao[0][3]))
    endRua = cadastros.funRua.setText(str(selecao[0][4]))
    endNumero = cadastros.funNmr.setText(str(selecao[0][5]))

#bancos
def banco_cad_fun():
    import mysql.connector
    global botao

    # Estabelecer a conexão com o banco de dados
    banco = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='123456',
        database='meteoro_calcados'
    )
    cursor = banco.cursor()

    funCod = cadastros.funCod.text() # não irá se usar na query
    funNome = cadastros.funNome.text()
    funSobre = cadastros.funSobre.text()
    funCPF = cadastros.funCPF.text()
    funTell = cadastros.funTell.text()
    funEmail = cadastros.funEmail.text()

    endCod = cadastros.endCod.text()
    endCep = cadastros.funRua.text()
    endEstado = cadastros.funEstado.text()
    endCidade = cadastros.funCidade.text()
    endBairro = cadastros.funBairro.text()
    endRua = cadastros.funRua.text()
    endNumero = cadastros.funNmr.text()

    if cadastros.radioCliente.isChecked():
        tabela = 'cliente'
    else:
        tabela = 'funcionario'

    colunas = f"nome_{tabela}, sobrenome_{tabela}, cpf_{tabela}, telefone_{tabela}, email_{tabela}, endereco_{tabela}"

    if botao == 'salvar':
        try:
            # Query SQL para inserir dados do formulário
            query = f"INSERT INTO {tabela} ({colunas}) VALUES (%s, %s, %s, %s, %s)"
            values = (funNome, funSobre, funCPF, funTell, funEmail, endCod)
            cursor.execute(query, values)

            # Query SQL para inserir endereço
            query2 = "INSERT INTO endereco (cod_endereco, cep, estado, cidade, bairro, rua, numero_casa) VALUES (%s, %s, %s, %s, %s, %s)"
            values2 = (endCod, endCep, endEstado, endCidade, endBairro, endRua, endNumero)
            cursor.execute(query2, values2)
        except:
            erro_salvar= QtWidgets.QErrorMessage()
            erro_salvar.showMessage('Código não existente')
            erro_salvar.exec_()
            print("Código não existente [salvar]")

    elif botao == 'excluir':
        try:
            # Query SQL para inserir dados do formulário
            query = f"DELETE FROM {tabela} WHERE cod_{tabela} = {funCod}"
            cursor.execute(query)

            # Query SQL para inserir endereço
            query = f"DELETE FROM endereco WHERE cod_endereco = {endCod}"
            cursor.execute(query)
        except:
            erro_salvar= QtWidgets.QErrorMessage()
            erro_salvar.showMessage('Código não existente')
            erro_salvar.exec_()
            print("Código não existente [excluir]")

    elif botao == 'update':
        try:
            # Query SQL para inserir dados do formulário
            query = f"UPDATE {tabela} SET nome_{tabela} = {funNome}, sobrenome_{tabela} = {funSobre}, cpf_{tabela} = {funCPF}, telefone_{tabela} = {funTell}, email_{tabela} = {funEmail}, endereco_{tabela} = {endCod} WHERE cod_{tabela} = {funCod}"
            cursor.execute(query)

            # Query SQL para inserir endereço
            query = f"UPDATE endereco SET cod_endereco = {endCod}, cep = {endCep}, estado = {endEstado}, cidade = {endEstado}, bairro = {endBairro}, rua = {endRua}, numero_casa = {endNumero}"
            cursor.execute(query)
        except:
            erro_salvar= QtWidgets.QErrorMessage()
            erro_salvar.showMessage('Código não existente')
            erro_salvar.exec_()
            print("Código não existente [update]")
    else:
        print("Erro nas condições")

    # Commit e fechamento de conexão
    banco.commit()
    cursor.close()
    banco.close()

    funCod = cadastros.funCod.setText('') # apagando valores da table
    funNome = cadastros.funNome.setText('')
    funSobre = cadastros.funSobre.setText('')
    funCPF = cadastros.funCPF.setText('')
    funTell = cadastros.funTell.setText('')
    funEmail = cadastros.funEmail.setText('')

    endCod = cadastros.endCod.setText('')
    endCep = cadastros.funCep.setText('')
    endEstado = cadastros.funEstado.setText('')
    endCidade = cadastros.funCidade.setText('')
    endBairro = cadastros.funBairro.setText('')
    endRua = cadastros.funRua.setText('')
    endNumero = cadastros.funNmr.setText('')

def banco_cad_prod():
    import mysql.connector

    # Estabelecer a conexão com o banco de dados
    banco = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='123456',
        database='meteoro_calcados'
    )
    cursor = banco.cursor()

    prodCod = cadastros.prodCod.text()
    prodNome = cadastros.prodNome.text()
    boxTamanho = cadastros.boxTamanho.currentIndex()
    prodModelo = cadastros.prodModelo.text()
    prodCor = cadastros.prodCor.text()
    prodMarca = cadastros.prodMarca.text()
    prodPrecoCusto = cadastros.prodPrecoCusto.text()
    prodPrecoVenda = cadastros.prodPrecoVenda.text()
    prodQuant = cadastros.prodQuant.text()
    

    query = "INSERT INTO produtos(nome_produto, tamanho_produto, modelo_produto, cor_produto, marca_produto, preco_custo, preco_venda, qtd_produto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (prodNome, boxTamanho, prodModelo, prodCor, prodMarca, prodPrecoCusto, prodPrecoVenda, prodQuant)

    cursor.execute(query, values)

    banco.commit()
    cursor.close()
    banco.close()

    prodCod = cadastros.prodCod.setText('')
    prodNome = cadastros.prodNome.setText('')
    prodModelo = cadastros.prodModelo.setText('')
    prodCor = cadastros.prodCor.setText('')
    prodMarca = cadastros.prodMarca.setText('')
    prodPrecoCusto = cadastros.prodPrecoCusto.setText('')
    prodPrecoVenda = cadastros.prodPrecoVenda.setText('')
    prodQuant = cadastros.prodQuant.setText('')

# definição de funções (campos)
def campos_login():
    global usuario
    usuario = "Bianca" # substituir quando finalizar o programa
    chamar_principal()
    # criar um cursor
    cursor = banco.cursor()

    # consulta (query) para verificar login
    query = "SELECT * FROM funcionario WHERE CONCAT(nome_funcionario, ' ', sobrenome_funcionario) = %s AND REGEXP_REPLACE(cpf_funcionario, '[^0-9]', '') = %s"
    parametros = (login.inserir_usuario.text(), login.inserir_senha.text()) # parametro de comparação
    # usuario = f"{login.inserir_usuario.text()},' ',{login.inserir_senha.text()}"
    # executar consultaadfd
    cursor.execute(query, parametros)

    if cursor.fetchone() is not None:
        chamar_principal()
    else:
        erro_login = QtWidgets.QErrorMessage()
        erro_login.showMessage('Usuário e/ou senha inválidos.')
        erro_login.exec_()

    cursor.close()
    banco.close()

# atualização, exclusão, salvamento...
def salvar_prod():
    global botao
    botao = 'salvar'
    banco_cad_prod()

def excluir_prod():
    global botao
    botao = 'excluir'
    banco_cad_prod()

def update_prod():
    global botao
    botao = 'update'
    banco_cad_prod()

def salvar_fun():
    global botao
    botao = 'salvar'
    banco_cad_fun()

def excluir_fun():
    global botao
    botao = 'excluir'
    banco_cad_fun()

def update_fun():
    global botao
    botao = 'update'
    banco_cad_fun()

# pesquisas
def botao_pesquisa_cod():
    global coluna
    coluna = 'cod_produto'
    banco_pesquisa_prod()

def botao_pesquisa_nome():
    global coluna
    coluna = 'nome_produto'
    banco_pesquisa_prod()

def botao_pesquisa_tamanho():
    global coluna
    coluna = 'tamanho_produto'
    banco_pesquisa_prod()

def botao_pesquisa_modelo():
    global coluna
    coluna = 'modelo_produto'
    banco_pesquisa_prod()

def botao_pesquisa_cor():
    global coluna
    coluna = 'cor_produto'
    banco_pesquisa_prod()

def botao_pesquisa_marca():
    global coluna
    coluna = 'marca_produto'
    banco_pesquisa_prod()

def botao_pesquisa_qtd():
    global coluna
    coluna = 'qtd_produto'
    banco_pesquisa_prod()

def banco_pesquisa_prod():
    global coluna
    import mysql.connector
    from PyQt5 import QtWidgets

    banco = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='123456',
        database='meteoro_calcados'
    )

    cursor = banco.cursor()
    campo = estoque.linePesquisa.text()
    columns = 'cod_produto, nome_produto, tamanho_produto, modelo_produto, cor_produto, marca_produto, qtd_produto'

    if campo == '': 
        query = f"SELECT {columns} FROM produtos ORDER BY {coluna}"
    else:
        query = f"SELECT {columns} FROM produtos WHERE {coluna} = '{campo}'"

    try: # usar o try
        cursor.execute(query)
        selecao = cursor.fetchall()

        cursor.close()

        estoque.dataTree.setRowCount(len(selecao))
        estoque.dataTree.setColumnCount(7)

        for i in range(len(selecao)):
            for j in range(7):
                estoque.dataTree.setItem(i, j, QtWidgets.QTableWidgetItem(str(selecao[i][j])))
    except:
        erro_pesquisa = QtWidgets.QErrorMessage()
        erro_pesquisa.showMessage('Pesquisa não encontrada')
        erro_pesquisa.exec_()

def pesquisa_geral_prod():
    import mysql.connector
    from PyQt5 import QtWidgets

    banco = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='123456',
        database='meteoro_calcados'
    )

    cursor = banco.cursor()
    campo = estoque.linePesquisa.text()
    columns = 'cod_produto, nome_produto, tamanho_produto, modelo_produto, cor_produto, marca_produto, qtd_produto'
    query = f"SELECT {columns} FROM produtos"
    cursor.execute(query)
    selecao = cursor.fetchall()

    cursor.close()

    estoque.dataTree.setRowCount(len(selecao))
    estoque.dataTree.setColumnCount(7)

    for i in range(len(selecao)):
        for j in range(7):
            estoque.dataTree.setItem(i, j, QtWidgets.QTableWidgetItem(str(selecao[i][j])))
# Def erros

# definição das viriáveis
principal = uic.loadUi('telas\pag_inicial.ui')
login = uic.loadUi('telas\login.ui')
estoque = uic.loadUi('telas\estoque.ui')
cadastros = uic.loadUi('telas\cadastro.ui')

# funções 'botões'
login.bt_login.clicked.connect(campos_login) # botão 'login' --> tela 'principal'
login.bt_exit.clicked.connect(exit)
principal.bt_cad.clicked.connect(cadastros_inicial) # botão 'cadastro de produtos' --> tela 'cadastro'
principal.bt_estoque.clicked.connect(inicial_estoque) # botão 'estoque' --> tela 'estoque']
principal.bt_disconnect.clicked.connect(disconect)
cadastros.bt_consultaProd.clicked.connect(inicial_estoque)
cadastros.bt_consultaFun.clicked.connect(inicial_estoque)
# botão voltar
cadastros.bt_voltar.clicked.connect(voltar)
estoque.bt_voltar.clicked.connect(voltar)

# cadastros
cadastros.bt_salvarFun.clicked.connect(salvar_fun)
cadastros.bt_salvarProd.clicked.connect(salvar_prod)

cadastros.bt_excluirProd.clicked.connect(excluir_prod)
cadastros.bt_excluirFun.clicked.connect(excluir_fun)

cadastros.bt_updateFun.clicked.connect(update_fun)
cadastros.bt_updateProd.clicked.connect(update_prod)

cadastros.bt_buscarFun.clicked.connect(buscarFun)
cadastros.bt_buscarProd.clicked.connect(buscarProd)

# select table
estoque.bt_cod.clicked.connect(botao_pesquisa_cod)
estoque.bt_nome.clicked.connect(botao_pesquisa_nome)
estoque.bt_tamanho.clicked.connect(botao_pesquisa_tamanho)
estoque.bt_modelo.clicked.connect(botao_pesquisa_modelo)
estoque.bt_cor.clicked.connect(botao_pesquisa_cor)
estoque.bt_marca.clicked.connect(botao_pesquisa_marca)
estoque.bt_qtd.clicked.connect(botao_pesquisa_qtd)
estoque.bt_geral.clicked.connect(pesquisa_geral_prod)

#exibir telas
login.show()

#rodar o programa
app.exec_()