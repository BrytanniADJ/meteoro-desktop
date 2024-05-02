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

def salvar_banco1():
    funCod = cadastro_fun.lineCod.Text()
    funNome = cadastro_fun.lineNome.Text()
    funSobre = cadastro_fun.lineSobre.Text()
    funCPF = cadastro_fun.lineCPF.Text()
    funTell = cadastro_fun.lineTell.Text()
    funEmail = cadastro_fun.lineEmail.Text()
    funCep = cadastro_fun.lineCep.Text()
    funRua = cadastro_fun.lineRua.Text()
    funNmr = cadastro_fun.lineNmr.Text()
    funBairro = cadastro_fun.lineBairro.Text()
    funCidade = cadastro_fun.lineCidade.Text()
    funEstado = cadastro_fun.boxEstado.


# definição de funções (campos)
def campos_login():
    # criar um cursor
    cursor = banco.cursor()

    # consulta (query) para verificar login
    query = "SELECT * FROM funcionario WHERE CONCAT(nome_funcionario, ' ', sobrenome_funcionario) = %s AND REGEXP_REPLACE(cpf_funcionario, '[^0-9]', '') = %s"
    parametros = (login.inserir_usuario.text(), login.inserir_senha.text()) # parametro de comparação
    # executar consultaadfd
    cursor.execute(query, parametros)

    if cursor.fetchone() is not None:
        login.close()
        chamar_principal()
    else:
        erro_login = QtWidgets.QErrorMessage()
        erro_login.showMessage('Usuário e/ou senha inválidos.')
        erro_login.exec_()

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
cadastro_fun.bt_salvar.clicked.connect(salvar_banco1)

#exibir telas
login.show()#, cadastro.show(), estoque.show(), pag_inicial.show()

#rodar o programa
app.exec_()