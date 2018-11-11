from estado import Estado

class Movimento:
    def __init__(self,estado_atual,letra_atual,estado_novo,letra_nova,direcao):
        self.estado_atual = estado_atual
        self.letra_atual = letra_atual
        self.estado_novo = estado_novo
        self.letra_nova = letra_nova
        self.direcao = direcao