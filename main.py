# imports
import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QTableWidget, QErrorMessage
from sqlite3 import Cursor
import mysql
import mysql.connector
from mysql.connector import Error

app = QtWidgets.QApplication([])

# carregamento de telas
pag_inicial = uic.loadUi('telas\pag_inicial.ui')
login = uic.loadUi('telas\login.ui')
estoque = uic.loadUi('telas\estoque.ui')
cadastro = uic.loadUi('telas\cadastro.ui')

#exibir telas
login.show(), cadastro.show(), estoque.show(), pag_inicial.show()

# # Lista de arquivos UI
# telas = ['pag_inicial.ui', 'login.ui', 'estoque.ui', 'cadastro.ui']

# # Carregamento e exibição das telas
# for tela in telas:
#     tela_carregada = uic.loadUi(os.path.join('telas', tela))
#     tela_carregada.show()

#rodar o programa
app.exec_()