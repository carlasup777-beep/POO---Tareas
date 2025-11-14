from personas import Persona
import datetime


class Cliente(Persona):
    """ Define la info de la clase persona """
    def __init__(self, id:int, cedula:str, nombre, email, vip:bool):
        Persona.__init__(self, cedula=cedula, nombre=nombre, email=email)
        self._id = id
        self._vip = vip
        self._FechaRegistro = datetime.datetime.now()

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, nuevo_id):
        self._id = nuevo_id

    @property
    def vip(self):
        return self._vip
    @vip.setter
    def vip(self, vip):
        self._vip = vip

    def __str__(self):
        return f'Cliente: {self.__dict__.__str__()}'

if __name__ == '__main__':
    Cl1 = Cliente(id="12", cedula="0963278944", nombre="Pablo Piccaso", email="PicaPico@gmail.com", vip=True)
    print(Cl1)
