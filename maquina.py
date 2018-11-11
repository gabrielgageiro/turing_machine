from estado import Tipo

class MaquinaTuring:
    def __init__(self, estados, movimentos, fita):
        self.estados = estados
        self.estado_inicial = self.get_estado_inicial()
        self.movimentos = movimentos
        self.fita = fita

    def get_fita(self):
        return self.fita.get_fita()

    def get_estado_inicial(self):
        return next(estado for estado in self.estados if estado.tipo == Tipo.Inicial)

    def processo(self,verbose=False):
        estado_atual = self.estado_inicial

        while estado_atual.tipo != Tipo.Final:
            letra_atual = self.fita.ler()
            estado_id = estado_atual.id

            movimento = next(m for m in self.movimentos if m.estado_atual == estado_id and m.letra_atual == letra_atual)

            estado_atual = next(estado for estado in self.estados if estado.id == movimento.estado_novo)

            self.fita.escrever(movimento.letra_nova)
            self.fita.mover_cabecote(movimento.direcao)
