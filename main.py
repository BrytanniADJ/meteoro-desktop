# imports principais
import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QTableWidget, QErrorMessage, QTimeEdit
from PyQt5.QtCore import QTimer, QTime
from sqlite3 import Cursor
from PyQt5.uic import loadUi
import mysql
import mysql.connector
from mysql.connector import Error
from tkinter import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from datetime import datetime
import time
from datetime import datetime
import threading

app = QtWidgets.QApplication([])
# conexão com banco de dados
# banco = mysql.connector.connect(
#     host = 'localhost',
#     port = '3306',
#     user = 'root',
#     password = '123456',
#     database = 'meteoro_calcados'
# )

# definição de funções (telas) login.ui
def chamar_principal():
    global usuario
    login.close()
    principal.show()
#    principal.text_usu.setText(f"{usuario}")
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
    vendas.close()
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
        query = f"SELECT {colunas} FROM produtos WHERE cod_produto = %s"
        values = (prodCod, )
        cursor.execute(query, values)

        selecao = cursor.fetchall()

        prodNome = cadastros.prodNome.setText(str(selecao[0][0]))
        prodTamanho = cadastros.boxTamanho.setCurrentText(str(selecao[0][1]))
        prodModelo = cadastros.prodModelo.setText(str(selecao[0][2]))
        prodCor = cadastros.prodCor.setText(str(selecao[0][3]))
        prodMarca = cadastros.prodMarca.setText(str(selecao[0][4]))
        prodPrecoCusto = cadastros.prodPrecoCusto.setText(str(selecao[0][5]))
        prodPrecoVenda = cadastros.prodPrecoVenda.setText(str(selecao[0][6]))
        prodQtd = cadastros.prodQuant.setText(str(selecao[0][7]))
    except:
        erro_produto = QtWidgets.QErrorMessage()
        erro_produto.showMessage('Código não existente [buscarProd]')
        erro_produto.exec_()
    finally:
        cursor.close()
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
        erro_login.showMessage(f"Código não existente de {tabela}")
        erro_login.exec_()

def buscarFun2():
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
    endCod = cadastros.endCod.text()
    colunas = f"cep, estado, cidade, bairro, rua, numero_casa"

    try:
        query1 = f"SELECT {colunas} FROM endereco WHERE cod_endereco = {endCod}"
        cursor.execute(query1)

        selecao1 = cursor.fetchall()

        endCep = cadastros.funCep.setText(str(selecao1[0][0]))
        endEstado = cadastros.funEstado.setText(str(selecao1[0][1]))
        endCidade = cadastros.funCidade.setText(str(selecao1[0][2]))
        endBairro = cadastros.funBairro.setText(str(selecao1[0][3]))
        endRua = cadastros.funRua.setText(str(selecao1[0][4]))
        endNumero = cadastros.funNmr.setText(str(selecao1[0][5]))

    except:
        erro_login = QtWidgets.QErrorMessage()
        erro_login.showMessage(f"Erro de script ou código não existentes em Endereços")
        erro_login.exec_()

    finally:
        cursor.close()

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
    
    colunas = "nome_produto, tamanho_produto, modelo_produto, cor_produto, marca_produto, preco_custo, preco_venda, qtd_produto"

    if botao == 'salvar':
        try:
            query = f"INSERT INTO produtos({colunas}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (prodNome, boxTamanho, prodModelo, prodCor, prodMarca, prodPrecoCusto, prodPrecoVenda, prodQuant)
            cursor.execute(query, values)
        except:
            erro_salvar= QtWidgets.QErrorMessage()
            erro_salvar.showMessage('Código não existente')
            erro_salvar.exec_()
            print("Código não existente [Salvar]")
    elif botao == 'excluir':
        try:
            query = f"DELETE FROM produtos WHERE cod_produto = {prodCod}"
            cursor.execute(query, )
        except:
            erro_salvar= QtWidgets.QErrorMessage()
            erro_salvar.showMessage('Código não existente')
            erro_salvar.exec_()
            print("Código não existente [excluir]")
    elif botao == 'update':
        try:
            query = f"UPDATE produtos SET cod_endereco = {prodCod}, nome_produto = {prodNome}, tamanho_produto = {boxTamanho}, modelo_produto = {prodModelo}, cor_produto = {prodCor}, marca_produto = {prodMarca}, preco_custo = {prodPrecoCusto}, preco_venda = {prodPrecoVenda}, qtd_produto = {prodQuant}"
            cursor.execute(query, )
        except:
            erro_salvar= QtWidgets.QErrorMessage()
            erro_salvar.showMessage('Código não existente')
            erro_salvar.exec_()
            print("Código não existente [update]")
    else:
        print("Problema no script de produtos.")

    banco.commit()
    cursor.close()

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
    chamar_principal()
    global usuario
#    usuario = "Bianca" # substituir quando finalizar o programa
    # criar um cursor
#    cursor = banco.cursor()

    # consulta (query) para verificar login
    # query = "SELECT * FROM funcionario WHERE CONCAT(nome_funcionario, ' ', sobrenome_funcionario) = %s AND REGEXP_REPLACE(cpf_funcionario, '[^0-9]', '') = %s"
    # parametros = (login.inserir_usuario.text(), login.inserir_senha.text()) # parametro de comparação
    # # usuario = f"{login.inserir_usuario.text()},' ',{login.inserir_senha.text()}"
    # # executar consultaadfd
    # cursor.execute(query, parametros)

    # if cursor.fetchone() is not None:
    #     chamar_principal()
    # else:
    #     erro_login = QtWidgets.QErrorMessage()
    #     erro_login.showMessage('Usuário e/ou senha inválidos.')
    #     erro_login.exec_()

    # cursor.close()
    # banco.close()

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

# PÁGINA VENDAS --------------------------
def vendas_push():
    import mysql.connector

    banco = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='123456',
        database='meteoro_calcados'
    )
    
    cursor = banco.cursor()
    lineCod = vendas.lineCod.text()

    if vendas.lineCod.text() != '':
        try:
            cursor.execute(f"SELECT preco_venda, CONCAT(nome_produto,' - [ ',qtd_produto,' ]') FROM produtos WHERE cod_produto = {lineCod}")
            global selecao_venda
            selecao_venda = cursor.fetchall()
            lineUnit = vendas.lineUnit.setText(str(selecao_venda[0][0]))
            lineResta = vendas.lineResta.setText(str(selecao_venda[0][1]))

        except:
            erro_login = QtWidgets.QErrorMessage()
            erro_login.showMessage(f"Código não existente")
            erro_login.exec_()
            print("Vendas - Cursor execute - falha")

    cursor.close()
    pag_vendas()

def vendas_push2():
    global botao
    import mysql.connector

    banco = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='123456',
        database='meteoro_calcados'
    )
    
    cursor = banco.cursor()

    lineCod = vendas.lineCod.text()
    lineUnit = vendas.lineUnit.text()
    lineQuant = vendas.lineQuant.text()
    lineDesc = vendas.lineDesc.text()
    lineResta = vendas.lineResta.text()

    Cp1 = vendas.lineCP1.text()

    lineSTotal = vendas.lineSTotal.text()
    lineDesc = vendas.lineDesc.text()
    lineTotal = vendas.lineTotal.text()

    agora = datetime.now()
    data = agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M:%S")

    cursor.execute(f"SELECT nome_produto FROM produtos WHERE cod_produto = {lineCod}")
    selecao_item = cursor.fetchall()

    if botao == 'salvar':
        try:
            lineUnit = float(vendas.lineUnit.text())
            lineQuant = float(vendas.lineQuant.text())
            vendas_total = lineQuant * lineUnit
            query = "INSERT INTO vendas VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (lineCod, lineResta, lineUnit, lineQuant, data, hora, vendas_total)
            cursor.execute(query, values)
            banco.commit()

            cursor.execute("SELECT cod, Item, valor_unit, quantidade, data, hora FROM vendas")
            selecao = cursor.fetchall()

            vendas.tableVendas.setRowCount(len(selecao))
            vendas.tableVendas.setColumnCount(6)

            for i in range(len(selecao)):
                for j in range(6):
                    vendas.tableVendas.setItem(i, j, QtWidgets.QTableWidgetItem(str(selecao[i][j])))

        except:
            erro_login = QtWidgets.QErrorMessage()
            erro_login.showMessage(f"Código não existente")
            erro_login.exec_()
            print("Vendas - For i, j - falha")

        finally:
            cursor.execute("SELECT SUM(total) FROM vendas")
            resultado = cursor.fetchall()
            
            total = resultado[0][0]
            Stotal = resultado[0][0]

            lineTotal = vendas.lineTotal.setText(f"{total}")
            lineSTotal = vendas.lineSTotal.setText(f"{Stotal}")
        
    elif botao == 'excluir':
        cursor.execute(f"DELETE FROM vendas WHERE cod = {lineCod}")
        banco.commit()

        lineCod = vendas.lineCod.setText('')
        cursor.execute("SELECT cod, Item, valor_unit, quantidade, data, hora FROM vendas")
        selecao = cursor.fetchall()

        vendas.tableVendas.setRowCount(len(selecao))
        vendas.tableVendas.setColumnCount(6)

        for i in range(len(selecao)):
            for j in range(6):
                vendas.tableVendas.setItem(i, j, QtWidgets.QTableWidgetItem(str(selecao[i][j])))

    elif botao == 'cancelar':
        cursor.execute(f"TRUNCATE TABLE vendas")
        banco.commit()
        vendas.close()
        vendas.show()

    # elif botao == 'finalizar':

    # else:
    lineCod = vendas.lineCod.setText('')
    lineUnit = vendas.lineUnit.setText('')
    lineQuant = vendas.lineQuant.setText('0')
    lineResta = vendas.lineResta.setText('')
    lineValor = vendas.lineValor.setText('')

    cursor.close()

def vendas_campo():
    if vendas.lineQuant.text() != '':
        lineQuant = float(vendas.lineQuant.text())
        lineUnit = float(vendas.lineUnit.text())

        valor = round(lineQuant * lineUnit, 2)
        lineValor = vendas.lineValor.setText(f"{valor}")

def vendas_campo1():
    global desconto_cp1
    desconto_cp1 = 0
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
    cp1 = vendas.lineCP1.text()
    
    if cp1 != '':
        try:
            query = "SELECT desconto FROM promocao WHERE cod = %s"
            cursor.execute(query, (cp1,))
            result = cursor.fetchone()
            
            if result:
                desconto_cp1 = (float(vendas.lineSTotal.text()) * float(result[0]))
                total -= desconto_cp1
                desc = vendas.lineDesc.setText(f"{desconto_cp1:.2f}")
                vendas.lineTotal.setText(f"{total:.2f}")
            else:
                raise ValueError("Código não existente")

        except ValueError as e:
            erro_login = QtWidgets.QErrorMessage()
            erro_login.showMessage(str(e))
            erro_login.exec_()
            print("Vendas, promoção campo 1")
        except mysql.connector.Error as err:
            erro_login = QtWidgets.QErrorMessage()
            erro_login.showMessage(f"Erro de banco de dados: {err}")
            erro_login.exec_()
            print(f"Erro de banco de dados: {err}")
        finally:
            cursor.close()
            banco.close()

def pag_vendas():
    principal.close()
    vendas.show()

def vendas_salvar():
    global botao
    botao = 'salvar'
    vendas_push2()

def vendas_excluir():
    global botao
    botao = 'excluir'
    vendas_push2()

def vendas_cancelar():
    global botao
    botao = 'cancelar'
    vendas_push2()

def vendas_finalizar():
    global botao
    botao = 'finalizar'
    vendas_push2()

# definição das viriáveis
principal = uic.loadUi('telas/pag_inicial.ui')
login = uic.loadUi('telas/login.ui')
estoque = uic.loadUi('telas/estoque.ui')
cadastros = uic.loadUi('telas/cadastro.ui')
vendas = uic.loadUi('telas/pag_vendas.ui')

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

principal.bt_vendas.clicked.connect(pag_vendas)

vendas.bt_voltar.clicked.connect(voltar)
vendas.lineCod.editingFinished.connect(vendas_push)
vendas.lineQuant.editingFinished.connect(vendas_campo)
vendas.lineCP1.editingFinished.connect(vendas_campo1)
vendas.bt_salvar.clicked.connect(vendas_salvar)
vendas.bt_excluir.clicked.connect(vendas_excluir)
vendas.bt_cancelar.clicked.connect(vendas_cancelar)
vendas.bt_finalizar.clicked.connect(vendas_finalizar)
# vendas.bt_Atualiza.clicked.connect()

#exibir telas
login.show()

#rodar o programa
app.exec_()