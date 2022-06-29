from clasePersonal import Personal

class Docente(Personal):
    __carrera: str
    __cargo: str
    __catedra: str
    __porcentaje = None


    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
        self.__porcExc = 50
        self.__porcSemi = 20
        self.__porcSim = 10

    def __str__(self):
        return f'docente creado {self.__carrera}'

    @classmethod
    def getTipo(self):
        return 'Docente'

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
                areaInvestigacion = '',
                tipoInvestigacion='',
                carrera= self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        return d

    def getCarrera(self):
        return self.__carrera

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

    def calcularSueldo(self):
        su = super().getSueldoBasico()
        su = (1 + super().getAntiguedad()/100)* super().getSueldoBasico()
        if self.__porcentaje == None:
            if self.__cargo == 'exclusivo':
                su += (50/100) * super().getSueldoBasico()
            elif self.__cargo == 'semiexclusivo':
                su += (20/100) * super().getSueldoBasico()
            elif self.__cargo == 'simple':
                su += (10/100) * super().getSueldoBasico()
        else:
            su += (self.__porcentaje/100)*super().getSueldoBasico()
        return su

    def setPorcentaje(self, nuevo):
        self.__porcentaje = nuevo
