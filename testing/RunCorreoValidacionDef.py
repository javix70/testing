def Runvalido(run):
  return len(str(run))==7 or len(str(run))==8
  #retorna True o False

def primerosTresDigitos(run):
   return int(str(run)[0:3])

def Correovalido(email):
    caracterBuscado="@"
    for c in email:
      if c==caracterBuscado:
        return True
    return False

def obtenerPass(apellido,run_valido):
  return apellido.lower() + str(primerosTresDigitos(run_valido))
 
 #Programa Principal
apellido=input("Ingrese apellido del Cliente: ")
while apellido != "-1":
  cuenta=input("Ingrese correo electrónico del cliente: ")
  while not (Correovalido(cuenta)):
      input("Correo Inválido ")
      cuenta=input("Ingrese correo electrónico del cliente: ")
    
  run=int(input("Ingresa SOLO los números de RUN: "))
  while not Runvalido(run):
    input("RUN Inválido ")
    run=int(input("Ingresa SOLO los números de RUN: "))
  print("Su cuenta validada es: ", cuenta)
  print("Su contraseña es: ",obtenerPass(apellido, run))
  print("FELICIDADES, Ya puede ingresar a www.jugandoloteria.com")
  apellido=input("Ingrese apellido del Cliente: ")