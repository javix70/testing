# -*- coding: utf-8 -*-
import re


class Persona:
    def __init__(self, nombre, peso, altura, run, correo, password, sexo):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.run = run
        self.correo = correo
        self.password = password
        self.sexo = sexo


class App:
    def __init__(self):
        pass

    def registrarPersona(self, lista_personas, persona):
        lista_personas.append([
            persona.nombre,
            persona.peso,
            persona.altura,
            persona.run,
            persona.correo,
            persona.password,
            persona.sexo,
        ])

    def calcularIMC(self, peso, altura):
        return round(peso/altura**2, 2)

    def mostrarEstadoNutricional(self, sexo, imc):
        estado_nutriconal = ""
        if sexo == "M":
            if imc < 20.0:
                estado_nutriconal = "Bajo Peso"
            elif 20.0 <= imc < 25.0:
                estado_nutriconal = "Normal"
            elif 25.0 <= imc < 30.0:
                estado_nutriconal = "Obesidad Leve"
            elif 30.0 <= imc < 41.0:
                estado_nutriconal = "Obesidad Severa"
            elif 41.0 <= imc:
                estado_nutriconal = "Obesidad Muy Severa"
        elif sexo == "F":
            if imc < 20.0:
                estado_nutriconal = "Bajo Peso"
            elif 20.0 <= imc < 24.0:
                estado_nutriconal = "Normal"
            elif 24.0 <= imc < 29.0:
                estado_nutriconal = "Obesidad Leve"
            elif 29.0 <= imc < 38.0:
                estado_nutriconal = "Obesidad Severa"
            elif 38.0 <= imc:
                estado_nutriconal = "Obesidad Muy Severa"
        return estado_nutriconal

    def validarCorreo(self, correo):
        pattern = r'[\w\d!#$%&\'*+\/=?^_\`{|}~-]+(?:\.[\w\d!#$%&\'*+\/=?^_\`{|}~-]+)*@(?:[\w\d](?:[\w\d-]*[\w\d])?\.)+[\w\d](?:[\w\d-]*[\w\d])?'
        return re.match(pattern, correo)

    def validarSexo(self, sexo):
        listaValida = ['f', 'F', 'mujer',
                       'Mujer', 'm', 'M', 'Hombre', 'hombre']
        if sexo in listaValida:
            return True

    def parseSexo(self, sexo):
        listaValida = {
            'f': 'F',
            'F': 'F',
            'mujer': 'F',
            'Mujer': 'F',
            'm': 'H',
            'M': 'H',
            'Hombre': 'H',
            'hombre': 'H'
        }
        return listaValida[sexo]

    def calcularContrasena(self, correo, run):
        return correo.split('@')[0] + run[:4]

    def escribirArchivo(self, lista_personas):
        test_txt = open("test.txt", "w+")
        for i in lista_personas:
            largo = len(i) - 1
            test_txt.write(','.join(i))
        test_txt.close()
