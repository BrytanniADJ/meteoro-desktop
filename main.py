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
    
def cadastro_inicial(): # cadastro de produtos
    principal.close()
    cadastro.show()

# def consulta_inicial(): # não possui tela
#     principal.close()
#     consulta.show()
#cadastro.ui
#def cadastro_cadastro(): #função para cadastrar itens
#def estoque_cadastro(): # função para ver os cadastros

# exit das páginas
def exit_geral():
    principal.close()
    estoque.close()
    cadastro.close()
    login.show

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
cadastro = uic.loadUi('telas\cadastro.ui')

# funções 'botões'
login.bt_login.clicked.connect(campos_login) # botão 'login' --> tela 'principal'
principal.bt_tela_cad.clicked.connect(cadastro_inicial) # botão 'cadastro de produtos' --> tela 'cadastro'
principal.bt_estoque.clicked.connect(inicial_estoque) # botão 'estoque' --> tela 'estoque'
#principal.bt_consulta.clicked.connect(consulta_inicial)

#exibir telas
login.show()#, cadastro.show(), estoque.show(), pag_inicial.show()

#rodar o programa
app.exec_()