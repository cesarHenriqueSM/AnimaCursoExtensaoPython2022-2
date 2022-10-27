nome = input("Aluno, informe seu nome: ")
nota = float(input("Digite sua nota: "))
if(nota == 10):
  print("{}, cê é o bichão memo ein doido...".format(nome))

elif(nota>=6 and nota<10):
  print("É... tá bão.")

elif(nota<6 and nota >=0):
  print("{}, você é fraco, lhe falta ódio.".format(nome))

else:
  print("Nota inválida, fera.")