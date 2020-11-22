
ide = 0
lista_persona = []
lista_imc =[]
#Agregamos la persona a la Lista de registros
def AgregarPersona(lista_persona,ide):
    nombre = input("Ingrese nombre: ")
    sexo = input("Ingrese Sexo(M o F): ")
    edad = int(input("Ingrese edad:"))
    tipo = input("Es deportista?(Si o No): ")
    lista_persona.append([ide, nombre, sexo, edad, tipo])
    
#Mostramos la lista de las personas registradas              
def MostrarLista(lista_persona):
    print("Listado de personas registradas")
    for persona in lista_persona:
        print(persona)
def Calcular IMC(peso, altura):
	If peso > 0 and altura > 0: 
	return peso/(altura*altura)

