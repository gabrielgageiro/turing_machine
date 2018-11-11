from enum import Enum

class Tipo(Enum):
    Inicial = 1
    Final = 2
    Vazio = 3

class Estado:
    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo