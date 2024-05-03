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
    login.close()
    principal.show()
# pag-inicial.ui
def inicial_estoque(): # cadastros
    principal.close()
    estoque.show()
    
def cadastro_prod_inicial(): # cadastro de produtos
    principal.close()
    cadastro_prod.show()

def disconect():
    principal.close()
    login.show()

def exit():
    login.close()

def cadastro_fun_inicial():
    principal.close()
    cadastro_fun.show()

# exit das páginas
def exit_geral():
    principal.close()
    estoque.close()
    cadastro_prod.close()
    # consulta.close()
    login.show

def voltar():
    estoque.close()
    cadastro_prod.close()
    cadastro_fun.close()
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
    funCod = cadastro_fun.lineCod.text()
    funNome = cadastro_fun.lineNome.text()
    funSobre = cadastro_fun.lineSobre.text()
    funCPF = cadastro_fun.lineCPF.text()
    funTell = cadastro_fun.lineTell.text()
    funEmail = cadastro_fun.lineEmail.text()

    endCep = cadastro_fun.lineRua.text()
    endEstado = cadastro_fun.lineEstado.text()
    endCidade = cadastro_fun.lineCidade.text()
    endBairro = cadastro_fun.lineBairro.text()
    endRua = cadastro_fun.lineRua.text()
    endNumero = cadastro_fun.lineNmr.text()

    # Determinar a tabela e as colunas
    if cadastro_fun.radioCliente.isChecked():
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

    funCod = cadastro_fun.lineCod.setText('')
    funNome = cadastro_fun.lineNome.setText('')
    funSobre = cadastro_fun.lineSobre.setText('')
    funCPF = cadastro_fun.lineCPF.setText('')
    funTell = cadastro_fun.lineTell.setText('')
    funEmail = cadastro_fun.lineEmail.setText('')

    endCep = cadastro_fun.lineRua.setText('')
    endEstado = cadastro_fun.lineEstado.setText('')
    endCidade = cadastro_fun.lineCidade.setText('')
    endBairro = cadastro_fun.lineBairro.setText('')
    endRua = cadastro_fun.lineRua.setText('')
    endNumero = cadastro_fun.lineNmr.setText('')


def banco_cad_fun0():
    import mysql.connector

    banco = mysql.connector.connect(
        host = 'localhost',
        port = '3306',
        user = 'root',
        password = '123456',
        database = 'meteoro_calcados'
    )

    cursor = banco.cursor()

    funCod = cadastro_fun.lineCod.text()
    funNome = cadastro_fun.lineNome.text()
    funSobre = cadastro_fun.lineSobre.text()
    funCPF = cadastro_fun.lineCPF.text()
    funTell = cadastro_fun.lineTell.text()
    funEmail = cadastro_fun.lineEmail.text()

    endCep = cadastro_fun.lineRua.text()
    endEstado = cadastro_fun.lineEstado.text()
    endCidade = cadastro_fun.lineCidade.text()
    endBairro = cadastro_fun.lineBairro.text()
    endRua = cadastro_fun.lineRua.text()
    endNumero = cadastro_fun.lineNmr.text()

    if cadastro_fun.radioCliente.isChecked():
        opcao = 'cliente'
        table = 'funcionario'
    else:
        opcao = 'funcionario'
        table = 'cliente'

    colunas = f"nome_{table}, sobrenome_{table}, cpf_{table}, telefone_{table}, email_{table}"

    query = f"INSERT INTO %s ({colunas}) VALUES (%s, %s, %s, %s, %s)"
    values = (opcao, funNome, funSobre, funCPF, funTell, funEmail)
    cursor.execute(query, values)

    query2 = "INSERT INTO endereco (cep, estado, cidade, bairro, rua, numero_casa) VALUES (%s, %s, %s, %s, %s, %s)"
    values2 = (endCep, endEstado, endCidade, endBairro, endRua, endNumero)
    cursor.execute(query2, values2)

    banco.commit()

    funCod = cadastro_fun.lineCod.setText('')
    funNome = cadastro_fun.lineNome.setText('')
    funSobre = cadastro_fun.lineSobre.setText('')
    funCPF = cadastro_fun.lineCPF.setText('')
    funTell = cadastro_fun.lineTell.setText('')
    funEmail = cadastro_fun.lineEmail.setText('')

    endCep = cadastro_fun.lineRua.setText('')
    endEstado = cadastro_fun.lineEstado.setText('')
    endCidade = cadastro_fun.lineCidade.setText('')
    endBairro = cadastro_fun.lineBairro.setText('')
    endRua = cadastro_fun.lineRua.setText('')
    endNumero = cadastro_fun.lineNmr.setText('')

    banco.commit()
    cursor.close()
    banco.close()
# definição de funções (campos)
def campos_login():
    chamar_principal()
    # criar um cursor
    cursor = banco.cursor()

    # consulta (query) para verificar login
    query = "SELECT * FROM funcionario WHERE CONCAT(nome_funcionario, ' ', sobrenome_funcionario) = %s AND REGEXP_REPLACE(cpf_funcionario, '[^0-9]', '') = %s"
    parametros = (login.inserir_usuario.text(), login.inserir_senha.text()) # parametro de comparação
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

# Def erros

# definição das viriáveis
principal = uic.loadUi('telas\pag_inicial.ui')
login = uic.loadUi('telas\login.ui')
estoque = uic.loadUi('telas\estoque.ui')
cadastro_prod = uic.loadUi('telas\cadastro_prod.ui')
cadastro_fun = uic.loadUi('telas\cadastro_fun.ui')


# funções 'botões'
login.bt_login.clicked.connect(campos_login) # botão 'login' --> tela 'principal'
login.bt_exit.clicked.connect(exit)
principal.bt_cad_pro.clicked.connect(cadastro_prod_inicial) # botão 'cadastro de produtos' --> tela 'cadastro'
principal.bt_estoque.clicked.connect(inicial_estoque) # botão 'estoque' --> tela 'estoque']
principal.bt_cad_fun.clicked.connect(cadastro_fun_inicial)
principal.bt_disconnect.clicked.connect(disconect)
# botão voltar
cadastro_fun.bt_voltar.clicked.connect(voltar)
estoque.bt_voltar.clicked.connect(voltar)
cadastro_prod.bt_voltar.clicked.connect(voltar)

# cadastros
cadastro_fun.bt_salvar.clicked.connect(banco_cad_fun)

#exibir telas
login.show()#, cadastro.show(), estoque.show(), pag_inicial.show()

#rodar o programa
app.exec_()