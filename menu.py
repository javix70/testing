# -*- coding: utf-8 -*-
from imc import App, Persona

class Menu:

    def __init__(self, lista_personas):
        self.lista_personas = lista_personas

    def iniciar(self):

        while True:
            print("(1) Registrar Persona")
            print("(2) Calcular IMC")
            print("(3) Salir del sistema")
            op = input("\tElija un a opcion: ")
            if "3" == op:
                break
            elif "1" == op:
                app = App()
                nombre = input("ingrese nombre")
                run = input("ingrese run")
                correo = input("ingrese correo")
                sexo = input("ingrese sexo")

                if not app.validarCorreo(correo):
                    print("\el correo no es valido")
                elif not app.validadSexo(sexo):
                    print("\el sexo no es valido")
                else:
                    password = app.calcularContrasena(correo, run)
                    persona = Persona(nombre, run, correo, password, app.parseSexo(sexo))
                    app.registrarPersona(self.lista_personas, persona)
                input("presione enter para continuar")
