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
            elif "2" == op:
                app = App()
                for i in range(len(self.lista_personas)):
                    print('Identificado: {} Nombre: {}'.format(
                        i, self.lista_personas[i][0]))

                posicion_persona = int(
                    input('Ingresa identificador persona: '))
                persona = self.lista_personas[posicion_persona]
                peso = int(persona[1])
                altura = int(persona[2])
                sexo = persona[6]
                calculo_imc = app.calcularIMC(peso, altura)
                estado_nutricional = app.mostrarEstadoNutricional(
                    sexo, calculo_imc)
                print('\tEl imc de {} es {} y su estado nutricional es {}\n'.format(
                    persona[0], calculo_imc, estado_nutricional))

            elif "1" == op:
                app = App()
                nombre = input("ingrese nombre ")
                peso = input("ingrese peso ")
                altura = input("ingrese altura ")
                run = input("ingrese run ")
                correo = input("ingrese correo ")
                sexo = input("ingrese sexo (F,H) ")

                if not app.validarCorreo(correo):
                    print("\el correo no es valido ")
                elif not app.validadSexo(sexo):
                    print("\el sexo no es valido ")
                else:
                    password = app.calcularContrasena(correo, run)
                    persona = Persona(nombre, peso, altura, run, correo,
                                      password, app.parseSexo(sexo))
                    app.registrarPersona(self.lista_personas, persona)
                    app.escribirArchivo(self.lista_personas)

                input("presione enter para continuar")
