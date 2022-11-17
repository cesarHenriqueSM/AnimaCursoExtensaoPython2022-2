#1° passo: importar a biblioteca sqlite3

import sqlite3

#2° passo: criando uma conexão com o banco de dados

con = sqlite3.connect("dc_universe.db")

#3° passo: criar um objeto do tipo cursor

cur = con.cursor()

#4° passo: Comando SQL do DB

sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5° passo: 

cur.execute(sql)

personagens = cur.fetchall()

for personagem in personagens:
  print(personagem)

for personagem in personagens:
  print(f"Nome: {personagem[1]} ({personagem[3]})")