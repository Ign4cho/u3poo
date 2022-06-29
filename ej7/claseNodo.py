
class Nodo:
    __personal = None
    __siguiente = None

    def __init__(self, unPersonal):
        self.__siguiente = None
        self.__personal = unPersonal

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__personal
