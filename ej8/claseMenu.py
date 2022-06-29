from zope.interface import Interface
from zope.interface import implementer
from interfazTesorero import ITesorero, IDirector
from claseLista import Manejador

class Menu:

    def opcion(self):
        self.muestraMenu()
        return self.getOpc()

    def muestraMenu(self):
        print('1- Insertar agente a la colección')
        print('2- Agregar agente a la colección')
        print('3- Mostrar tipo de agente en una posición')
        print('4- Listar docentes investigadores por carrera')
        print('5- Contar investigadores y docentes investigadores por area de investigación')
        print('6- Generar listado ordenado por apellido')
        print('7- Listar docentes investigadores por categoría')
        print('8- Almacenar en archivo JSON')
        print('9- Iniciar sesión')
        print('10- Salir')

    def getOpc(self):
        opc = input('Opción: ')
        while opc not in ['1','2','3','4','5','6','7','8','9', '10', '11', '12']:
            opc = input('Opción incorrecta, intente nuevamente: ')
        return int(opc)

    def menuDirector(self):
        opc = 0
        print('1- Modificar Sueldo basico')
        print('2- Modificar porcentaje por cargo a un docente')
        print('3- Modificar porcentaje por categoria a un personal de apoyo')
        print('4- Modificar importe extra de un docInvestigador')
        while opc not in [1,2,3,4]:
            opc = int(input('Opcion'))
        return int(opc)

    def director(self, manejadorDirector: IDirector):
        opc = self.menuDirector()
        if opc == 1:
            dni = input('Dni: ')
            nuevo = float(input('Nuevo basico: '))
            manejadorDirector.modificarBasico(dni, nuevo)
        elif opc == 2:
            dni = input('Dni: ')
            nuevo = float(input('Nuevo porcentaje: '))
            manejadorDirector.modificarPorcentajeporcargo(dni, nuevo)
        elif opc == 3:
            dni = input('Dni: ')
            nuevo = float(input('Nuevo porcentaje: '))
            manejadorDirector.modificarPorcentajeporcategoria(dni, nuevo)
        elif opc == 4:
            dni = input('Dni: ')
            nuevo = float(input('Nuevo importe extra: '))
            manejadorDirector.modificarImporteextra(dni, nuevo)

    def tesorero(self, manejadorTesorero: ITesorero):
        dni = input('Ingrese dni del agente: ')
        manejadorTesorero.gastosSueldoPorEmpleado(dni)

