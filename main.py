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

def banco_cad_fun():
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

    # Obter os dados do formulário
    funCod = cadastros.funCod.text() # não irá se usar na query
    funNome = cadastros.funNome.text()
    funSobre = cadastros.funSobre.text()
    funCPF = cadastros.funCPF.text()
    funTell = cadastros.funTell.text()
    funEmail = cadastros.funEmail.text()

    endCep = cadastros.funRua.text()
    endEstado = cadastros.funEstado.text()
    endCidade = cadastros.funCidade.text()
    endBairro = cadastros.funBairro.text()
    endRua = cadastros.funRua.text()
    endNumero = cadastros.funNmr.text()

    # Determinar a tabela e as colunas
    if cadastros.radioCliente.isChecked():
        tabela = 'cliente'
    else:
        tabela = 'funcionario'

    colunas = f"nome_{tabela}, sobrenome_{tabela}, cpf_{tabela}, telefone_{tabela}, email_{tabela}"

    # Query SQL para inserir dados do formulário
    query = f"INSERT INTO {tabela} ({colunas}) VALUES (%s, %s, %s, %s, %s)"
    values = (funNome, funSobre, funCPF, funTell, funEmail)
    cursor.execute(query, values)

    # Query SQL para inserir endereço
    query2 = "INSERT INTO endereco (cep, estado, cidade, bairro, rua, numero_casa) VALUES (%s, %s, %s, %s, %s, %s)"
    values2 = (endCep, endEstado, endCidade, endBairro, endRua, endNumero)
    cursor.execute(query2, values2)

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

    endCep = cadastros.funRua.setText('')
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
# botão voltar
cadastros.bt_voltar.clicked.connect(voltar)
estoque.bt_voltar.clicked.connect(voltar)

# cadastros
cadastros.bt_salvarFun.clicked.connect(banco_cad_fun)
cadastros.bt_salvarProd.clicked.connect(banco_cad_prod)

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