import Aula4_16_11_2022c as db

con, cur = db.conectar()

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o): ")

sql = "SELECT MAX(pessoa_id)+1 from pessoas"

cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"

else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)

con.commit()

con.close()