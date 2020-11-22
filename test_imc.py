# -*- coding: utf-8 -*-
import unittest
from imc import registrarPersona, lista_personas, calcularIMC, validarCorreo, calcularContrasena

class TestImc(unittest.TestCase):

    def setUp(self):
      lista_personas = []

    def test_guardar_en_lista_datos_de_persona(self):
      nombre = "javier",
      run = "11112-9",
      correo = "yo@mi.cl",
      password = "yo1111"
      resultado_esperado = [[nombre, run, correo, password]]
      registrarPersona(nombre, run, correo, password)
      self.assertEqual(lista_personas, resultado_esperado)

    def test_calcular_imc(self):
      peso = 80
      altura = 1.80
      resultado_esperado = 24.69
      resultado_imc = calcularIMC(peso, altura)
      self.assertEqual(resultado_imc, resultado_esperado)

    def test_validar_correo_correcto(self):
      correo = "yo@mi.cl"
      resultado = validarCorreo(correo)
      self.assertTrue(resultado)

    def test_validar_correo_incorrecto(self):
      correo = "no.es.un.correo.valido"
      resultado = validarCorreo(correo)
      self.assertFalse(resultado)

    def test_calcular_contrasena(self):
      rut = '19341549-0'
      correo = "yo@mi.cl"
      resultado = calcularContrasena(correo,rut)
      resultado_esperado = 'yo1934'
      self.assertEqual(resultado, resultado_esperado)
