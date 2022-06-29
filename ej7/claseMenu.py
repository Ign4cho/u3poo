
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
        print('9- Salir')

    def getOpc(self):
        opc = input('Opción: ')
        while opc not in ['1','2','3','4','5','6','7','8','9']:
            opc = input('Opción incorrecta, intente nuevamente: ')
        return int(opc)
