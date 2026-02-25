# Operadores logicos son los siguientes:
# and, or y not



# Operador and = Todos tienen que ser verdaderos 
# para que se cumpla la condicion
licencia = True
edad = 14

if edad >= 18 and licencia:
  print("Puedes conducir")
else:
  print("No puedes conducir!!!")

# Operador or = Con uno que sea verdadero la condicion
# se cumple, todas las condiciones tienen que ser False 
# Para que no se cumplan la condicion

if edad >= 18 or licencia:
  print("Puedes conducir")
else:
  print("No tienes permitido conducir")


# Operador de negacion, niega la condición, si es False
# lo pasa a True y si es True lo pasa a False

es_fin_de_semana = False

if not es_fin_de_semana:
  print("Hay que ir a trabajar")
else:
  print("Puedes descansar")

# If añidados 
tiene_dinero=True
if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quedate en casa")
else:
  print("No puedes entrar a la disco")