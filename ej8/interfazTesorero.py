from zope.interface import Interface
from zope.interface import implementer


class ITesorero(Interface):

    def gastosSueldoPorEmpleado(self, dni):
        pass

class IDirector(Interface):
    def modificarBasico(self, dni, nuevoBasico):
        pass

    def modificarPorcentajeporcargo(self, dni, nuevoPorcentaje):
        pass

    def modificarPorcentajeporcategoria(self, dni, nuevoPorcentaje):
        pass

    def modificarImporteextra(self, dni, nuevoImporteExtra):
        pass
