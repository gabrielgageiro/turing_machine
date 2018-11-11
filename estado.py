from enum import Enum

class Tipo(Enum):
    Inicial = 0
    Final = 1
    Vazio = 2

class Estado:
    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo