# -*- coding: utf-8 -*-
import re

class Persona:
    def __init__(self, nombre, run, correo, password, sexo):
        self.nombre = nombre
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
            persona.run,
            persona.correo,
            persona.password
        ])

    def calcularIMC(self, peso, altura):
        return peso/altura**2

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
                estado_nutriconal = "Obesidad Severa"
        return estado_nutriconal

    def validarCorreo(self, correo):
        pattern = r'^\w+[\w|\d]*@\w+[\w|\d]*.\w{2,3}$'
        return re.match(pattern, correo)

    def validadSexo(self, sexo):
        listaValida = ['f','F','mujer','Mujer','h','H','Hombre','hombre']
        if sexo in listaValida:
            return True

    def parseSexo(self, sexo):
        listaValida = {
            'f': 'F',
            'F': 'F',
            'mujer': 'F',
            'Mujer': 'F',
            'h': 'H',
            'H': 'H',
            'Hombre': 'H',
            'hombre': 'H'
        }
        return listaValida[sexo]

    def calcularContrasena(self, correo,run):
        return  correo.split('@')[0] + run[:4]
