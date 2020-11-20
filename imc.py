# -*- coding: utf-8 -*-
import re

lista_personas = []

def registrarPersona(nombre, run, correo, password):
    lista_personas.append([nombre, run, correo, password])

def calcularIMC(peso,altura):
    return peso/altura**2

def mostrarEstadoNutricional():
    pass

def validarCorreo(correo):
    pattern = r'^\w+[\w|\d]*@\w+[\w|\d]*.\w{2,3}$'
    return re.match(pattern, correo)

def calcularContrasena(correo,rut):
    return  correo.split('@')[0] + rut[:4]
