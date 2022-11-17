import sqlite3

def conectar():
  con = sqlite3.connect("dc_universe.db")

  cur = con.cursor()

  return con, cur

