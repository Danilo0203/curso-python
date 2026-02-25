###
# 01 - Setencias condicionales (if, elif, else)
# Permiten ejecutar bloques de codigo solo si se cumplen ciertas condiciones
###


import os 
os.system("clear")

print("\n Sentencia simple condicional if")

edad = 18
if edad >= 18:
  print('Eres mayor de edad')

print("\n Sentencia simple condicional else")
edad = 15
if edad >= 18:
  print('Eres mayor de edad')
else:
  print("Eres menor de edad")


print("\n Sentencia simple condicional elif")

nota = 10

if nota >=9:
  print('Excelente')
elif nota >=7:
  print('Buena nota')
elif nota >= 5:
  print("Bien")
else:
  print('No aprobo')


