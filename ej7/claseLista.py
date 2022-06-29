from clasePersonal import Personal
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocInvestigador import DocInvestigador
from claseDeApoyo import DeApoyo
from claseNodo import Nodo
from zope.interface import Interface
from zope.interface import implementer
from interfaceLista import ILista

@implementer(ILista)
class Manejador:
    __comienzo = None
    def __init__(self):
        self.__comienzo = None

    def agregarElemento(self, unPersonal):
        nodo = Nodo(unPersonal)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def insertarElemento(self, unPersonal, pos):
        band = True
        contador = 0
        actual = self.__comienzo
        while contador <= pos and actual is not None:
            contador+=1
            actual = actual.getSiguiente()
        if actual is None:
            band = False

        if band == False:
            print('La posición no se encuentra en el arreglo')
        else:
            if pos == 0:
                unNodo = Nodo(unPersonal)
                unNodo.setSiguiente(actual)
                self.__comienzo = unNodo
                print('Carga exitosa')
            else:
                unNodo = Nodo(unPersonal)
                unNodo.setSiguiente(actual.getSiguiente())
                actual.setSiguiente(unNodo)
                print('Carga exitosa')

    def mostrarElemento(self, pos):
        contador = 0
        actual = self.__comienzo
        while contador < pos and actual is not None:
            contador += 1
            actual = actual.getSiguiente()
        if actual == None:
            print('No hay ningún agente en esa posición')
        else:
            unPersonal = actual.getDato()
            print(f'En la posición {pos} se encuentra un {unPersonal.getTipo()}')

    def crearAgente(self):
        print('Que tipo de agente quiere crear\n1-Personal de Apoyo\n2-Docente\n3-Investigador\n4-Docente Investigador')
        opc = int(input('Opcion: '))
        while opc not in [1,2,3,4]:
            opc = int(input('Opción incorrecta, intente nuevamente.'))
        unAgente = None
        cuil = input('Cuil: ')
        ap = input('Apellido: ')
        nom = input('Nombre: ')
        sb = input('Sueldo Basico (float): ')
        anti = input('Antiguedad (int): ')
        if opc == 1:
            categoria = input('Categoria (de 1 a 22): ')
            unAgente = DeApoyo(cuil,ap,nom, sb, anti, categoria, '','','','','')
        elif opc == 2:
            carrera = input('Carrera: ')
            cargo = input('Cargo (exlusivo, semiexclusivo, simple): ')
            catedra = input('Catedra: ')
            unAgente = Docente(cuil, ap, nom, sb, anti,'', '','', carrera, cargo, catedra)
        elif opc == 3:
            area = input('Area de investigación: ')
            tipo = input('Tipo de investigación: ')
            unAgente = Investigador(cuil, ap, nom, sb, anti,'', area, tipo, '', '', '')
        elif opc == 4:
            carrera = input('Carrera: ')
            cargo = input('Cargo (exlusivo, semiexclusivo, simple): ')
            catedra = input('Catedra: ')
            area = input('Area de investigación: ')
            tipo = input('Tipo de investigación: ')
            catinc = input('Categoria de incentivo (I, II, III, IV, V): ')
            impextra = input('Importe extra por investigación y docencia (float): ')
            unAgente = DocInvestigador(cuil,ap,nom, sb, anti,'', area, tipo, carrera, cargo, catedra, catinc, impextra)
        else:
            print('Error en la carga')
        return unAgente

    def toJSON(self):
        lista = []
        actual = self.__comienzo
        while actual is not None:
            lista.append(actual.getDato())
            actual = actual.getSiguiente()
        d = dict(
            __class__ = self.__class__.__name__,
            agentes=[agente.toJSON() for agente in lista]
        )
        return d

    def mostrarDocInv(self, carrera):
        lista = []
        actual = self.__comienzo
        while actual is not None:
            unAgente = actual.getDato()
            if isinstance(unAgente, DocInvestigador):
                if unAgente.getCarrera() == carrera:
                    lista.append(unAgente)
            actual = actual.getSiguiente()
        lista.sort(key = lambda DocInvestigador: DocInvestigador.getNombre())
        for agente in lista:
            print(agente)

    def cuentaPorArea(self, area):
        inv, dinv = 0, 0
        actual = self.__comienzo
        while actual is not None:
            unAgente = actual.getDato()
            if isinstance(unAgente, DocInvestigador) or isinstance(unAgente, Investigador):
                if unAgente.getAreaInv() == area:
                    if isinstance(unAgente, DocInvestigador):
                        dinv += 1
                    elif isinstance(unAgente, Investigador):
                        inv += 1

            actual = actual.getSiguiente()
        print(f'Cantidad de investigadores que trabajand en {area}\nInvestigadores: {inv}\nDocentes investigadores: {dinv}')

    def muestraLista(self):
        lista = []
        actual = self.__comienzo
        while actual is not None:
            lista.append(actual.getDato())
            actual = actual.getSiguiente()
        lista.sort(key=lambda Personal: Personal.getApellido())
        for agente in lista:
            print(f'\nAgente: {agente.getApellido()}, {agente.getNombre()}.')
            print(f'Tipo: {agente.getTipo()}    Sueldo: {agente.calcularSueldo()}\n')

    def listaPorCategoria(self, cat):
        lista = []
        acum = 0
        actual = self.__comienzo
        while actual is not None:
            agente = actual.getDato()
            if isinstance(agente, DocInvestigador) and agente.getCategoria() == cat:
                print(f'\nApellido: {agente.getApellido()} - Nombre: {agente.getNombre()} - importe extra: {agente.getImpExtra()}\n')
                acum += agente.getImpExtra()

            actual = actual.getSiguiente()
        print(f'\nDinero a solicitar en concepto de importes extra: ${acum}')

