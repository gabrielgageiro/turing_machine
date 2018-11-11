from direcao import Direcao

class Fita:
    def __init__(self,palavra,alfabeto):
        self.alfabeto = alfabeto + '$#'
        self.posicao_cabecote = 0
        self.__init_fita(palavra)

    def __init_fita(self,palavra):
        fita = '$'
        for letra in (l for l in palavra if l in self.alfabeto):
            fita += letra
        fita += '#'
        self._fita = list(fita)

    def escrever(self,letra):
        if self.posicao_cabecote < 1 or letra not in self.alfabeto:
            return
        self._fita[self.posicao_cabecote] = letra

        if self.posicao_cabecote == len(self._fita) - 1:
            self._fita += '#'

    def ler(self):
        if self.posicao_cabecote < 0 or self.posicao_cabecote > len(self._fita) -1:
            raise Exception ('Posicao ' + str(self.posicao_cabecote) + 'Fora do alcance da fita')
        return self._fita[self.posicao_cabecote]

    def _remover_elemento(self):
        for i in range(len(self._fita) -1,1,-1):
            if self._fita[i] == '#' and self._fita[i-1] == '#':
                del self._fita[-1:]
            else:
                break

    def get_fita(self):
        self._remover_elemento()
        return ''.join(self._fita)

    def get_tamanho(self):
        return len(self._fita)

    def mover_cabecote(self,direcao):
        if direcao == Direcao.Direita:
            self.posicao_cabecote += 1
        elif direcao == Direcao.Esquerda:
            self.posicao_cabecote -= 1

        if self.posicao_cabecote > len(self._fita) - 1:
            self._fita += '#'
        if self.posicao_cabecote < 0:
            self.posicao_cabecote = 0