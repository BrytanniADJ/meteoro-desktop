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

#conexão com banco de dados
banco = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = '123456',
    database = 'meteoro_calcados'
)

# definição das viriáveis
principal = uic.loadUi('telas\pag_inicial.ui')
login = uic.loadUi('telas\login.ui')
estoque = uic.loadUi('telas\estoque.ui')
cadastro = uic.loadUi('telas\cadastro.ui')

# definição de funções (telas)
def chamar_principal():
    login.close()
    principal.show()
    
def chamar_cadastro():
    principal.close()
    cadastro.show()
    
# definição de funções (campos)
def campos_login():
    # criar um cursor
    cursor = banco.cursor()

    # consulta (query) para verificar login
    query = 'SELECT * FROM funcionario WHERE email_funcionario = "%s" and cpf_funcionario = "%s"'
    parametros = (login.inserir_usuario.text(), login.inserir_senha.text()) # parametro de comparação

    # executar consulta
    cursor.execute(query, parametros)

    if cursor.
        chamar_principal()
    else:
        mensagem_erro = QtWidgets.QErrorMessage()
        mensagem_erro.showMessage('Por favor, preencha o campo de senha.')
        mensagem_erro.exec_()

# funções 'botões'
login.bt_login.clicked.connect(campos_login) # botão 'login' --> tela 'principal'
principal.bt_tela_cad.clicked.connect(chamar_cadastro) # botão 'cadastro de produtos' --> tela 'cadastro'

#exibir telas
login.show()#, cadastro.show(), estoque.show(), pag_inicial.show()

#rodar o programa
app.exec_()