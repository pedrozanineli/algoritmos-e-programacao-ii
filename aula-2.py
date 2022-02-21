"""
"Formatação"
"%d - inteiro"
"%f - ponto flutuante"
msg = " A media dos numeros é %4.2f" %(8656656.6164134)
print(msg)

print("%f + %f = %4.1f" %(15, 9.578421, 15+9.578421 ))

print("%d + %d = %d" %(5, 7.578421, 5+7.578421 ), end="!!!")
"""

"""
"Estrutura de Seleção"
dinheiro = 50000

if dinheiro>10000:
  imps = dinheiro * 0.1
  multa = dinheiro * 0.15
  print( "Valor do Imposto:", imps, "e da multa:", multa)

"""

"""
"Seleção com 2 ramos"
x=10

if x>0:
  print(x, "é maior do que zero.")
else:
  print(x, "é menos ou igual a zero.")

"""

"""
Seleção Aninhadas

Calcula ajuste de dinheiro, se tempo < 1 mantém , se tempo < 10 faz uma coisa, 
se tempo >= 10 faz outra:
"""

"""
dinheiro = 1000.50
tempo = 10

if tempo<1:
  print("Seu dinheiro continua:", dinheiro)
else:
  if tempo<10:
    dinheiro = dinheiro * 1.1
  else:
    dinheiro = dinheiro * 1.2
  print("Seu dinheiro apos o ajuste:", dinheiro)

"""


"""
Seleção com múltiplos ramos

Faremos um comando que funciona como calculadora.
"""
"""
valores = [5,9]     #Poderiamos pedir que o usuario informasse com:
#valores=input("Digite dois valores: ").split()
x = int(valores[0])
y = int(valores[1])
op = "+"            #Poderiamos pedir que o usuario informasse

if op=="+":
  resultado = x+y
elif op=="-":
  resultado = x-y
elif op=="*":
  resultado = x*y
elif op=="/":
  resultado = x/y
elif op=="**":
  resultado = x**y
print(x,op,y,"=",resultado)
"""

"""
Uso If - elif - else

Faremos um comando que funciona como calculadora.
"""
"""
valores = [5,9]     #Poderiamos pedir que o usuario informasse com:
#valores=input("Digite dois valores: ").split()
x = int(valores[0])
y = int(valores[1])
op = "+"            #Poderiamos pedir que o usuario informasse

if op=="+":
  resultado = x+y
elif op=="-":
  resultado = x-y
elif op=="*":
  resultado = x*y
elif op=="/":
  resultado = x/y
elif op=="**":
  resultado = x**y
else:
  resultado = None
if resultado == None:
  print(op, "Operador inexistente!!")
else:
  print(x,op,y,"=",resultado)
"""
"""
"While"
"Estrutura de repetição"
i=1
while i<=10:
  print(i, end=" ")
  i=i+1
print()
"""

"""
"For"
"Estrutura de Repetição"
for i in [2,3,4,5,6,7,8,9]:
  print(i, end=" ")
print()
"""

"""
"Range"

print(range(7))

print(range(7,20))

print(range(9,50,3))
"""
"""
"Vetor"
vetor=[4,3,2,1]

print(vetor[0])
print(vetor[3])

#Utilizando o range()
soma = 0
for i in range(3):
  soma = soma + vetor[i]
print(soma)

#Utilizando o len()
soma = 0
for i in range(len(vetor)):
  soma = soma + vetor[i]
print(soma)
"""
"""
#Leitura de todos os valores de uma vez:
valores = input("Digite os valores na mesma linha: ").split()

#Leitura um de cada vez:
valores=[None]*10
for i in range(len(valores)):
  valores[i] = input("Digite um valor: ")
"""
"""
"Exibição"
#Todos de uma vez:
numeros= [4,6,2,5,1,25,12,32]
print(numeros)

#Escrita um de cada vez:
numeros= [4,6,2,5,1,25,12,32]
for x in numeros:
  print(x, end=" ")
"""

"""
"Matriz"
aposta =  [[" ","X"," "],
          [" "," ","X"],
          [" ","X"," "],
          ["X"," "," "],
          [" ","X"," "],
          [" "," ","X"],
          [" ","X"," "]]
print(aposta)
"Para acessar os elementos desse vetor:"
aposta =  [[" ","X"," "],
          [" "," ","X"],
          [" ","X"," "],
          ["X"," "," "],
          [" ","X"," "],
          [" "," ","X"],
          [" ","X"," "]]
          

aposta       #Representa uma matriz de 7 linhas por 3 colunas

aposta[0]    #Representa a primeira linha da matriz

aposta[0][0] #Representa o caractere da primeira linha da primeira coluna
"""

"""
"String"
nome = "Ana"
print(len(nome)) # confima o comprimento ou quantidade de caracteres na string


print(nome[0])
print(nome[1])
print(nome[2])

"""
"Parei em TUPLA"

