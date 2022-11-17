import sqlite3

con = sqlite3.connect("dc_universe.db")

cur = con.cursor()

sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)'"

cur.execute(sql)

con.commit()

con.close()