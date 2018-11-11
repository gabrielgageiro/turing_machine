from maquina import MaquinaTuring
from estado import Tipo,Estado
from movimento import Movimento
from direcao import Direcao
from fita import Fita

fita = Fita('***','*')

estados = [
    Estado('q0', Tipo.Inicial),
    Estado('q1', Tipo.Vazio),
    Estado('qf', Tipo.Final)
]

movimentos = [
    Movimento('q0','$','q1','$',Direcao.Direita),
    Movimento('q1','*','q1','*',Direcao.Direita),
    Movimento('q1','#','qf','*',Direcao.Mantem),
]

mt = MaquinaTuring(estados,movimentos,fita)
mt.processo()

print(mt.get_fita())