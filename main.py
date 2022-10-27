nome = input("Digite seu nome: ")
idade = int(input("Olá, "+nome+", qual a sua idade? "))
dobro = idade * 2
genero = input("Informe seu gênero usando M para masculino, F para feminino ou O para outro(s): ")
print(f"{nome}, o dobro de sua idade é igual a {dobro} anos.")
if idade>=18 and genero == "M":
  print("Você já é maior de idade! Legal, já pode beber ou dirigir! Mas lembre-se, if (beber and dirigir):  print(Cadeia)!")
  print("Você precisa/precisou prestar serviço militar obrigatório.")
elif idade>=18:
  print("Você já é maior de idade! Legal, já pode beber ou dirigir! Mas lembre-se, if (beber and dirigir):  print(Cadeia)!")
elif idade<18 and genero == "M":
  maioridade = int(18-idade)
  print("Faltam {} anos para sua maioridade. Aproveite enquanto é tempo! Lembre-se que aos 18 anos você deve se alistar obrigatoriamente.".format(maioridade))

elif idade<18:
  maioridade = int(18-idade)
  print("Faltam {} anos para sua maioridade. Aproveite enquanto é tempo!".format(maioridade))