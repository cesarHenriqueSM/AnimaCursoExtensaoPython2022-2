#exibir de 1 até 10
cont=1

while(cont<=10):
  print(cont)
  cont = cont +1

#Laço for (pythonfor = or each)
 #fruta ="morango"
#lista
frutas = ["morango","laranja","uva"]
#mostrar todas
print(frutas)
#quero exibir apenas a 3a frutas
print(frutas[2])
#Exibir quantas frutas tem na minha lista?
print(len(frutas))

frutas.append("manga")
print(frutas)
i=0
while(i<4):
  print(frutas[i])
  i = i+1
print("Exemplo das frutas com while")
frutas.append("pêra")
i=0
while(i<len(frutas)):
  print(frutas[i])
  i=i+1

print("Exemplo com FOR")
for fruta in frutas:
  print(fruta)