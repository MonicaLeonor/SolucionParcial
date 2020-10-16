import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma(numero1, numero2):
    suma = numero1 + numero2
    return suma


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""


# start-->
def sumaPares():
    result = 0
    for numero in range(0, 1001, 2):
        result = result + numero
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->
def areaTotalCilindro(radio, altura):
    areaLat =  areaLateral(5,7)  #2*math.pi*radio*altura
    areaCir = areaCirculo(5)  #2*math.pi*radio*radio
    result = areaLat + areaCir
    return round(result,2)



def areaLateral(radio,altura):
    result = 2*math.pi*radio*altura
    return round(result,2)


def areaCirculo(radio):
    result = 2*math.pi*radio*radio
    return round(result,2)


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cilindro:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def areaTotalCilindro(self):
        areaLat =  areaLateral(5,7) #2*math.pi*self.radio*self.altura
        areaCir = areaCirculo(5) #2*math.pi*self.radio*self.radio
        result = areaLat + areaCir
        return round(result,2)


"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento
"""


class Restaurante:
    def _init_(self):
        pizzaDict["nombre":nombre,"lugar":lugar,"costo":costo,"conDescuento":boolean,"descuento":descuento]

    
    def ordenar(self):
        pass

    def costoTotal(self):
        return 0

    def costoTotalConDescuento(self):
        return 0


class Pizza:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/MonicaLeonor/SolucionParcial.git"
