from clasePersonal import Personal

class Investigador(Personal):
    __areaInvestigacion: str
    __tipoInvestigacion: str

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra)
        self.__areaInvestigacion = areaInvestigacion
        self.__tipoInvestigacion = tipoInvestigacion

    def __str__(self):
        return f'creado, {self.getCuil()}'

    @classmethod
    def getTipo(self):
        return 'Investigador'

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                cuil = super().getCuil(),
                apellido = super().getApellido(),
                nombre = super().getNombre(),
                sueldoBasico = super().getSueldoBasico(),
                antiguedad = super().getAntiguedad(),
                categoria = '',
                areaInvestigacion = self.__areaInvestigacion,
                tipoInvestigacion=self.__tipoInvestigacion,
                carrera='',
                cargo='',
                catedra=''
            )
        )
        return d

    def getAreaInv(self):
        return self.__areaInvestigacion

    def getTipoInv(self):
        return self.__tipoInvestigacion

    def calcularSueldo(self):
        su = super().getSueldoBasico()
        su *= 1 + super().getAntiguedad()/100
        return su
