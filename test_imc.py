# -*- coding: utf-8 -*-
import unittest
from imc import App, Persona

class TestApp(unittest.TestCase):

    def test_guardar_en_lista_datos_de_persona(self):
      nombre = "javier",
      run = "11112-9",
      correo = "yo@mi.cl",
      password = "yo1111"
      persona = Persona(nombre, run, correo, password)
      lista_personas = []
      resultado_esperado = [[nombre, run, correo, password]]
      app = App()
      app.registrarPersona(lista_personas, persona)
      self.assertEqual(lista_personas, resultado_esperado)

    def test_calcular_imc(self):
      peso = 80
      altura = 1.80
      resultado_esperado = 24.69
      app = App()
      resultado_imc = app.calcularIMC(peso, altura)
      self.assertEqual(resultado_imc, resultado_esperado)

    def test_mostrar_estado_nutricional(self):
      app = App()
      self.assertEqual(app.mostrarEstadoNutricional("M", 19.0), "Bajo Peso")
      self.assertEqual(app.mostrarEstadoNutricional("M", 20.0), "Normal")
      self.assertEqual(app.mostrarEstadoNutricional("M", 24.9), "Normal")
      self.assertEqual(app.mostrarEstadoNutricional("M", 25.0), "Obesidad Leve")
      self.assertEqual(app.mostrarEstadoNutricional("M", 29.9), "Obesidad Leve")
      self.assertEqual(app.mostrarEstadoNutricional("M", 30.0), "Obesidad Severa")
      self.assertEqual(app.mostrarEstadoNutricional("M", 40.9), "Obesidad Severa")
      self.assertEqual(app.mostrarEstadoNutricional("M", 41.0), "Obesidad Muy Severa")
      self.assertEqual(app.mostrarEstadoNutricional("F", 19.0), "Bajo Peso")
      self.assertEqual(app.mostrarEstadoNutricional("F", 20.0), "Normal")
      self.assertEqual(app.mostrarEstadoNutricional("F", 23.9), "Normal")
      self.assertEqual(app.mostrarEstadoNutricional("F", 24.0), "Obesidad Leve")
      self.assertEqual(app.mostrarEstadoNutricional("F", 28.9), "Obesidad Leve")
      self.assertEqual(app.mostrarEstadoNutricional("F", 29.0), "Obesidad Severa")
      self.assertEqual(app.mostrarEstadoNutricional("F", 37.9), "Obesidad Severa")
      self.assertEqual(app.mostrarEstadoNutricional("F", 38.0), "Obesidad Muy Severa")

    def test_validar_correo_correcto(self):
      correo1 = "yo@mi.cl"
      correo2 = "yo.soy.argentino@mi.com.ar"
      app = App()
      resultado1 = app.validarCorreo(correo1)
      resultado2 = app.validarCorreo(correo2)
      self.assertTrue(resultado1)
      self.assertTrue(resultado2)

    def test_validar_correo_incorrecto(self):
      correo = "no.es.un.correo.valido"
      app = App()
      resultado = app.validarCorreo(correo)
      self.assertFalse(resultado)

    def test_calcular_contrasena(self):
      rut = '19341549-0'
      correo = "yo@mi.cl"
      app = App()
      resultado = app.calcularContrasena(correo,rut)
      resultado_esperado = 'yo1934'
      self.assertEqual(resultado, resultado_esperado)
