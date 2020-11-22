from datetime import date
import datetime

class Registro:
    def __init__(self):
        self.fecha = ""
        self.imc = ""
        self.peso = ""
        self.altura = ""

class Persona:

    def __init__(self):
        self.rut = ""
        self.nombre = ""
        self.apellido = ""
        self.fecha_nacimiento = ""
        self.sexo = ""
        self.actividad = ""
        lista_registros = []
        self.registros = lista_registros

    def Calcular(self, fecha_registro, peso, altura):
        # calculo para el imc
        try:
            imc = peso / (altura * altura)
            registro = Registro()
            registro.imc = imc
            registro.fecha = fecha_registro
            self.registros.append(registro)
            print("El imc calculado fue:", imc)
        except:
            print("Dato invalido para realizar el calculo...")

    def listar_imc_por_sexo(self):
        for registro in self.registros:
            print("Para el IMC", registro.imc, "Con fecha", registro.fecha," ")
            if self.sexo == "M":
                if registro.imc < 20:
                    print("Bajo Peso\n")
                elif 20 <= registro.imc < 25:
                    print("Normal\n")
                elif 25 <= registro.imc < 30:
                    print("Obesidad Leve\n")
                elif 30 <= registro.imc < 41:
                    print("Obesidad Severa\n")
                elif 41 <= registro.imc:
                    print("Obesidad Muy Severa\n")
            elif self.sexo == "F":
                if registro.imc < 20:
                    print("Bajo Peso\n")
                elif 20 <= registro.imc < 24:
                    print("Normal\n")
                elif 24 <= registro.imc < 29:
                    print("Obesidad Leve\n")
                elif 29 <= registro.imc < 38:
                    print("Obesidad Severa\n")
                elif 38 <= registro.imc:
                    print("Obesidad Severa\n")

    def listar_imc_por_edad_sexo(self):
        edad = self.calculateAge()

        if 19 <= edad <= 24:
            if self.sexo == "F":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 18.9 <= registro.imc <= 22.1:
                        print("Óptimo\n")
                    elif registro.imc <= 25:
                        print("Bueno\n")
                    elif registro.imc <= 29.6:
                        print("SobrePeso\n")
                    elif 29.6 < registro.imc :
                        print("Malo (Obesidad)\n")
            elif self.sexo == "M":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 10.8 <= registro.imc <= 14.9:
                        print("Óptimo\n")
                    elif registro.imc <= 19:
                        print("Bueno\n")
                    elif registro.imc <= 23.3:
                        print("SobrePeso\n")
                    elif 23.3 < registro.imc :
                        print("Malo (Obesidad)\n")
        elif 25 <= edad <= 29:
            if self.sexo == "F":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 18.9 <= registro.imc <= 22:
                        print("Óptimo\n")
                    elif registro.imc <= 25.4:
                        print("Bueno\n")
                    elif registro.imc <= 29.8:
                        print("SobrePeso\n")
                    elif 29.8 < registro.imc :
                        print("Malo (Obesidad)\n")
            elif self.sexo == "M":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 12.8 <= registro.imc <= 16.5:
                        print("Óptimo\n")
                    elif registro.imc <= 20.3:
                        print("Bueno\n")
                    elif registro.imc <= 24.4:
                        print("SobrePeso\n")
                    elif 24.4 < registro.imc :
                        print("Malo (Obesidad)\n")
        elif 30 <= edad <= 34:
            if self.sexo == "F":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 19.7 <= registro.imc <= 22.7:
                        print("Óptimo\n")
                    elif registro.imc <= 26.4:
                        print("Bueno\n")
                    elif registro.imc <= 30.5:
                        print("SobrePeso\n")
                    elif 30.5 < registro.imc :
                        print("Malo (Obesidad)\n")
            elif self.sexo == "M":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 14.5 <= registro.imc <= 18:
                        print("Óptimo\n")
                    elif registro.imc <= 21.5:
                        print("Bueno\n")
                    elif registro.imc <= 25.2:
                        print("SobrePeso\n")
                    elif 25.2 < registro.imc :
                        print("Malo (Obesidad)\n")
        elif 35 <= edad <= 39:
            if self.sexo == "F":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 21 <= registro.imc <= 22.7:
                        print("Óptimo\n")
                    elif registro.imc <= 27.7:
                        print("Bueno\n")
                    elif registro.imc <= 31.5:
                        print("SobrePeso\n")
                    elif 31.5 < registro.imc :
                        print("Malo (Obesidad)\n")
            elif self.sexo == "M":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 16.1 <= registro.imc <= 19.4:
                        print("Óptimo\n")
                    elif registro.imc <= 22.6:
                        print("Bueno\n")
                    elif registro.imc <= 26.1:
                        print("SobrePeso\n")
                    elif 26.1 < registro.imc :
                        print("Malo (Obesidad)\n")
        elif 40 <= edad <= 44:
            if self.sexo == "F":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 22.6 <= registro.imc <= 25.6:
                        print("Óptimo\n")
                    elif registro.imc <= 29.3:
                        print("Bueno\n")
                    elif registro.imc <= 32.8:
                        print("SobrePeso\n")
                    elif 32.8 < registro.imc :
                        print("Malo (Obesidad)\n")
            elif self.sexo == "M":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 17.5 <= registro.imc <= 20.5:
                        print("Óptimo\n")
                    elif registro.imc <= 23.6:
                        print("Bueno\n")
                    elif registro.imc <= 26.9:
                        print("SobrePeso\n")
                    elif 26.9 < registro.imc :
                        print("Malo (Obesidad)\n")
        elif 45 <= edad <= 49:
            if self.sexo == "F":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 24.3 <= registro.imc <= 27.3:
                        print("Óptimo\n")
                    elif registro.imc <= 30.9:
                        print("Bueno\n")
                    elif registro.imc <= 34.1:
                        print("SobrePeso\n")
                    elif 34.1 < registro.imc :
                        print("Malo (Obesidad)\n")
            elif self.sexo == "M":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 18.6 <= registro.imc <= 21.5:
                        print("Óptimo\n")
                    elif registro.imc <= 24.5:
                        print("Bueno\n")
                    elif registro.imc <= 27.6:
                        print("SobrePeso\n")
                    elif 27.6 < registro.imc :
                        print("Malo (Obesidad)\n")
        elif 50 <= edad <= 54:
            if self.sexo == "F":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 26.6 <= registro.imc <= 29.7:
                        print("Óptimo\n")
                    elif registro.imc <= 33.1:
                        print("Bueno\n")
                    elif registro.imc <= 36.2:
                        print("SobrePeso\n")
                    elif 36.2 < registro.imc :
                        print("Malo (Obesidad)\n")
            elif self.sexo == "M":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 19.8 <= registro.imc <= 22.7:
                        print("Óptimo\n")
                    elif registro.imc <= 25.6:
                        print("Bueno\n")
                    elif registro.imc <= 28.7:
                        print("SobrePeso\n")
                    elif 28.7 < registro.imc :
                        print("Malo (Obesidad)\n")

        elif 55 <= edad <= 59:
            if self.sexo == "F":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 27.4 <= registro.imc <= 30.7:
                        print("Óptimo\n")
                    elif registro.imc <= 34:
                        print("Bueno\n")
                    elif registro.imc <= 37.3:
                        print("SobrePeso\n")
                    elif 33.7 < registro.imc :
                        print("Malo (Obesidad)\n")
            elif self.sexo == "M":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 20.2 <= registro.imc <= 23.2:
                        print("Óptimo\n")
                    elif registro.imc <= 26.2:
                        print("Bueno\n")
                    elif registro.imc <= 29.3:
                        print("SobrePeso\n")
                    elif 29.3 < registro.imc :
                        print("Malo (Obesidad)\n")
        elif 56 <= edad:
            if self.sexo == "F":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 27.4 <= registro.imc <= 30.7:
                        print("Óptimo\n")
                    elif registro.imc <= 34:
                        print("Bueno\n")
                    elif registro.imc <= 37.3:
                        print("SobrePeso\n")
                    elif 33.7 < registro.imc :
                        print("Malo (Obesidad)\n")
            elif self.sexo == "M":
                for registro in self.registros:
                    print("Para el IMC", registro.imc, "Con fecha", registro.fecha, " ")
                    if 20.3 <= registro.imc <= 23.5:
                        print("Óptimo\n")
                    elif registro.imc <= 26.7:
                        print("Bueno\n")
                    elif registro.imc <= 29.8:
                        print("SobrePeso\n")
                    elif 29.8 < registro.imc :
                        print("Malo (Obesidad)\n")
        return

    def Mostrar(self):
        print("\n")
        print("Los datos Ingresados son:")
        print("nombre:", self.nombre)
        print("apellido:", self.apellido)
        print("sexo:", self.sexo)
        print("es atleta/normal:", self.actividad)

    def calculateAge(self):
        date_str = self.fecha_nacimiento  # The date - 29 Dec 2017
        format_str = '%d/%m/%Y'  # The format
        datetime_obj = datetime.datetime.strptime(date_str, format_str)
        today = date.today()
        age = today.year - datetime_obj.year - ((today.month, today.day) < (datetime_obj.month, datetime_obj.day))
        return age

lista_personas = []
# se define el menu
def Menu():
    while True:
        print("\n")
        print("\tMenu")
        print("[1] Ingresar a nueva Persona...")
        print("[2] Ingresar nuevo registro de IMC...")
        print("[3] Mostrar registros...")
        print("[4] Salir...")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            try:
                persona = Persona()
                persona.rut = input("Rut: ")
                persona.nombre = input("nombre: ")
                persona.apellido = input("apellido: ")
                persona.fecha_nacimiento = input("fecha nacimiento: ")
                persona.sexo = input("sexo M o F : ")
                persona.actividad = input("es usted atleta/normal: ")

                lista_personas.append(persona)
            except:
                print("Dato invalido.....")
                print("Regresando al menu principal...")

        elif opcion == 2:
            rut_persona = input("Ingrese rut persona a ingresar registros: ")
            for persona in lista_personas:
                print(persona.rut)
                if persona.rut == rut_persona:
                    persona.Mostrar()
                    fecha = input("Ingrese fecha en el formato dd/mm/yyyy que se peso")
                    peso = float(input("Ingrese su peso en kg, ej '0.0': "))
                    altura = float(input("Ingrese su altura en m: "))
                    persona.Calcular(fecha, peso, altura)
                    break

        elif opcion == 3:
            print("adios...")
            rut_persona = input("Ingrese rut persona a mostrar registros: ")
            for persona in lista_personas:
                if persona.rut == rut_persona:
                    persona.Mostrar()
                    persona.listar_imc_por_sexo()
                    persona.listar_imc_por_edad_sexo()
            break

        elif opcion == 4:
            break

        else:
            print("Opcion Invalida...")


if __name__ == "__main__":
    # se llama al menu para desplegarlo
    Menu()