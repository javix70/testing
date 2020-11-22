# -*- coding: utf-8 -*-
import unittest
from unittest.mock import mock_open, patch

from imc import App, Persona


class TestApp(unittest.TestCase):

    def test_guardar_en_lista_datos_de_persona(self):
        nombre = "javier",
        peso = 50
        altura = 160,
        run = "11112-9",
        correo = "yo@mi.cl",
        password = "yo1111"
        sexo = "H"
        persona = Persona(nombre, peso, altura, run, correo, password, sexo)
        lista_personas = []
        resultado_esperado = [
            [nombre, peso, altura, run, correo, password, sexo]]
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
        resultado = app.calcularContrasena(correo, rut)
        resultado_esperado = 'yo1934'
        self.assertEqual(resultado, resultado_esperado)

    def test_escribir_archivo(self):
        app = App()
        nombre = "fran"
        peso = "55"
        altura = "155"
        run = "18621995-3"
        correo = "fran@fran.cl"
        password = "fran1861"
        sexo = "F"
        lista_personas = [[nombre, peso,altura, run, correo, password, sexo]]
        resultado_esperado = ','.join(lista_personas[0])
        
        with patch("imc.open", mock_open(), create=True) as mock_file:
            app.escribirArchivo(lista_personas)
        mock_file.assert_called_once_with("test.txt", "w+")
        mock_file.return_value.write.assert_called_once_with(resultado_esperado)
