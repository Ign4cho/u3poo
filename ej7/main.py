from clasePersonal import Personal
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocInvestigador import DocInvestigador
from claseDeApoyo import DeApoyo
from claseLista import Manejador
from claseObjectEncoder import ObjectEncoder
from claseMenu import Menu

if __name__ == '__main__':
    jsonF = ObjectEncoder()
    agentes = Manejador()
    menu = Menu()
    d = jsonF.leerJSONArchivo('personal.json')
    agentes = jsonF.decodificarDiccionario(d)
    band = True
    while band == True:
        opc = menu.opcion()
        if opc == 1:
            unAgente = agentes.crearAgente()
            pos = int(input('Ingrese la posición donde lo quiere insertar'))
            agentes.insertarElemento(unAgente, pos)
        elif opc == 2:
             unAgente = agentes.crearAgente()
             agentes.agregarElemento(unAgente)
        elif opc == 3:
            pos = int(input('Ingrese la posición que donde se encuentra el agente que quiere ver'))
            agentes.mostrarElemento(pos)
        elif opc == 4:
            carrera = input('Ingrese la carrera')
            agentes.mostrarDocInv(carrera)
        elif opc ==5:
            area = input('Ingrese el area')
            agentes.cuentaPorArea(area)
        elif opc ==6:
            agentes.muestraLista()
        elif opc == 7:
            cat = input('Categoria: ')
            agentes.listaPorCategoria(cat)
        elif opc == 8:
            d = agentes.toJSON()
            jsonF.guardarJSONArchivo(d, 'personal.json')
            print('carga exitosa')
        elif opc == 9:
            band = False
            print('Goodbye')


