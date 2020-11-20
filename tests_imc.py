# -*- coding: utf-8 -*-

import unittest
from imc import *

class TestsImc(unittest.TestCase):

    def setUp(self):
      lista_personas = []


    def guardar_en_lista_datos_de_persona(self):
       resultado_esperado = [
        [nombre="javier",
        run= "11112-9", 
        correo="yo@mi.cl",
        password= "yo1111"]
       ]
        registrarPersona(nombre, run, correo, password)

        self.assertEqual(lista_personas, resultado_esperado)
