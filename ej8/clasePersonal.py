import abc
from abc import ABC

class Personal:
    __cuil: str
    __apellido: str
    __nombre: str
    __sueldoBasico: float
    __antiguedad: int

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, areaInvestigacion='', tipoInvestigacion='', carrera='', cargo='', catedra=''):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = float(sueldoBasico)
        self.__antiguedad = int(antiguedad)

    @abc.abstractmethod
    def getTipo(self):
        pass

    def getCuil(self):
        return self.__cuil

    @abc.abstractmethod
    def toJSON(self):
        pass

    @abc.abstractmethod
    def calcularSueldo(self):
        pass

    def getCuil(self):
        return self.__cuil

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldoBasico(self):
        return self.__sueldoBasico

    def getAntiguedad(self):
        return self.__antiguedad

    def setBasico(self, nuevo):
        self.__sueldoBasico = nuevo
