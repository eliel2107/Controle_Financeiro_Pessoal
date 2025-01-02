import sqlite3 as lite


#criando conexão
con = lite.connect("dados.db")


# Funções de Inserções -------------------------------------------------
#Inserir categorias
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria(nome) VALUES (?)"
        cur.execute(query, i)

#Inserir Receitas
def inserir_receitas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas(categoria, adicionado_em,valor) VALUES (?,?,?)"
        cur.execute(query, i)

#Inserir Gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas(categoria, retirado_em,valor) VALUES (?,?,?)"
        cur.execute(query, i)

# Funções para deletar -------------------------------------------------
# Deletar receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id= ?"
        cur.execute(query, i)

# Deletar gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id= ?"
        cur.execute(query, i)

# Fuções para ver dados ---------------

# Ver Categorias
def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens 


# Ver Receitas
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens 

# Ver Gastos
def ver_gsatos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens