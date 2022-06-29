from clasePersonal import Personal
from claseDocente import Docente
from claseInvestigador import Investigador


class DocInvestigador(Docente, Investigador):
    __categoriaIncentivo: str
    __importeExtra: float

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra, categoriaIncentivo, importeExtra):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, categoria, areaInvestigacion, tipoInvestigacion, carrera, cargo, catedra)
        self.__categoriaIncentivo = categoriaIncentivo
        self.__importeExtra = float(importeExtra)

    def __str__(self):
        s = f'\nNombre: {super().getNombre()} -- Apellido: {super().getApellido()} \nCuil: {super().getCuil()} -- Sueldo: {self.calcularSueldo()}'
        s += f'\nCategoria incentivo {self.__categoriaIncentivo}\n'
        return s

    @classmethod
    def getTipo(self):
        return 'Docente Investigador'

    def getCategoria(self):
        return self.__categoriaIncentivo

    def getImpExtra(self):
        return self.__importeExtra

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
                areaInvestigacion = super().getAreaInv(),
                tipoInvestigacion=super().getTipoInv(),
                carrera=super().getCarrera(),
                cargo=super().getCargo(),
                catedra=super().getCatedra(),
                categoriaIncentivo = self.__categoriaIncentivo,
                importeExtra = self.__importeExtra
            )
        )
        return d

    def calcularSueldo(self):
        su = super().getSueldoBasico()
        su = (1 + super().getAntiguedad()/100)* super().getSueldoBasico()
        if super().getCargo() == 'exclusivo':
            su += 0.5 * super().getSueldoBasico()
        elif super().getCargo() == 'semiexclusivo':
            su += 0.2 * super().getSueldoBasico()
        elif super().getCargo() == 'simple':
            su += 0.1 * super().getSueldoBasico()
        su += self.__importeExtra
        return su

    def setImporte(self, nuevo):
        self.__importeExtra = nuevo
