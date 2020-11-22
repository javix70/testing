import os
 
def menu():
  """ Función que limpia la pantalla y muestra nuevamente el menu 	"""
  os.system('clear') # Limpia la pantalla
  print ("Selecciona una opción")
  print ("\t[1] - Ingresar Notas")
  print ("\t[2] - Mostrar Notas ")
  print ("\t[3] - tercera opción")
  print ("\t[4] - cuarta opción")
  print ("\t[9] - salir")
def insertar_notas(lista,n):
    for i in range(n):
      nota=float(input("Inserte una nota: "))
      lista.append(nota)
    print("Ha insertado "  + str(n) + " notas")
def mostrar_notas(lista):
  print(lista)

 
notas=[] 
while True:  	# Mostramos el menu
  menu()      # solicituamos una opción al usuario
  opcionMenu = input("inserta un numero valor >> ")
  if opcionMenu=="1": 
    largo=int(input("¿Cuántas notas requiere ingresar ? ")) 
    insertar_notas(notas,largo)
    input("Has pulsado la opción 1...\npulsa una tecla para continuar>> ")
  elif opcionMenu=="2":
      mostrar_notas(notas)
      input("Has pulsado la opción 2...\npulsa una tecla para continuar>> ")
  elif opcionMenu=="3":
	  print ("")
	  input("Has pulsado la opción 3...\npulsa una tecla para continuar>> ")
  elif opcionMenu=="4":
	  print ("")
	  input("Has pulsado la opción 4...\npulsa una tecla para continuar>> ")
  elif opcionMenu=="9":
    print ("")
    break
  else:
    print ("")
    input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")