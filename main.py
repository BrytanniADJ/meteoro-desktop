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
    funCod = cadastro_fun.lineCod.text() # não irá se usar na query
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

    funCod = cadastro_fun.lineCod.setText('') # apagando valores da table
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

    prodCod = cadastro_fun.prodCod.text()
    prodNome = cadastro_prod.prodNome.text()
    boxTamanho = cadastro_prod.boxTamanho.currentIndex()
    prodModelo = cadastro_prod.prodModelo.text()
    prodCor = cadastro_prod.prodCor.text()
    prodMarca = cadastro_prod.prodMarca.text()
    prodPrecoCusto = cadastro_prod.prodPrecoCusto.text()
    prodPrecoVenda = cadastro_prod.prodPrecoVenda.text()
    prodQuant = cadastro_prod.prodQuant.text()
    

    query = "INSERT INTO produtos(nome_produto, tamanho_produto, modelo_produto, cor_produto, marca_produto, preco_custo, preco_venda, qtd_produto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (prodNome, boxTamanho, prodModelo, prodCor, prodMarca, prodPrecoCusto, prodPrecoVenda, prodQuant)

    cursor.execute(query, values)

    banco.commit()
    cursor.close()
    banco.close()

    prodCod = cadastro_fun.prodCod.setText()
    prodNome = cadastro_prod.prodNome.setText('')
    prodModelo = cadastro_prod.prodModelo.setText('')
    prodCor = cadastro_prod.prodCor.setText('')
    prodMarca = cadastro_prod.prodMarca.setText('')
    prodPrecoCusto = cadastro_prod.prodPrecoCusto.setText('')
    prodPrecoVenda = cadastro_prod.prodPrecoVenda.setText('')
    prodQuant = cadastro_prod.prodQuant.setText('')
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

    global coluna
    database = ""
    cont = 1

    cursor.execute("SELECT MAX(cod_produto) FROM produtos")
    maior_cod = cursor.fetchone()[0]

    for cont in range(maior_cod):
        query = f"SELECT cod_produto, nome_produto, tamanho_produto, modelo_produto, cor_produto, marca_produto, qtd_produto FROM produtos WHERE {coluna}"
        cursor.execute(query) # 
        linha = cursor.fetchone()

        if linha:
            linha_formatada = "\t".join(map(str, linha))
            database += f"\n\t{linha_formatada}"

        cont = cont + 1

    estoque.query.setText(database)

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
cadastro_prod.bt_salvar.clicked.connect(banco_cad_prod)

# select table
estoque.bt_cod.clicked.connect(banco_pesquisa_prod)

#exibir telas
login.show()#, cadastro.show(), estoque.show(), pag_inicial.show()

#rodar o programa
app.exec_()