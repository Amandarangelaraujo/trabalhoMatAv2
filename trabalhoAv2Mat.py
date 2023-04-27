#fazer o baralho

from itertools import combinations
def gerar_baralho():
    naipes = ['copas', 'ouros', 'espadas', 'paus']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'valete', 'dama', 'rei', 'ás']
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append((naipe, valor))
    return baralho

#distribuir as cartas, recebendo o return da função gerar_baralho
def distribuir_cartas(baralho):
    import random
    #mistura aleatoriamente as cartas
    random.shuffle(baralho)
    mao_jogadores = []
    #vai distribuir 4 vezes, já que são quatro jogadores, 3 cartas

    for i in range (4):
        mao=[] #a vez de que receber
        for j in range(3): #a distribuição de cartas em si
            mao.append(baralho.pop(0)) #remove a carta da primeira posição e salva ela na lista mão
        mao_jogadores.append(mao) 
      
    mesa = []
    #distribuir as cartas da mesa
    for i in range(2):
        mesa.append(baralho.pop(0)) #tira de baralho as cartas e salva na variavel mesa

    #a função retorna a variável mao, que tem as cartas dos jogadores e mesa, que tem as cartas que estão na mesa
    return mao_jogadores, mesa

#atribuindo a variáveis fora das funções o seu retorno

baralho = gerar_baralho()
mao_jogadores,mesa = distribuir_cartas(baralho)

#definindo as cartas dos jogadores
jogadorNumero1=mao_jogadores[0]
jogadorNumero2=mao_jogadores[1]
jogadorNumero3=mao_jogadores[2]
jogadorNumero4=mao_jogadores[3]
print(f"{jogadorNumero1} \n {jogadorNumero2} \n {jogadorNumero3} \n {jogadorNumero4}" )


#combinar as cartas da mesa com as cartas da mão, depois fazer uma combinação dessas cartas para poder formar um trio.
#feito apenas com um jogador, depois pensar em como diminuir esse código para fazer para os outros jogadores.
print('##########')
print(jogadorNumero1)
cincoCartasJogador1=[]
for i in range(3):
    cincoCartasJogador1.append(jogadorNumero1[i])
for i in range(2):
    cincoCartasJogador1.append(mesa[i])

print('##########')
print(cincoCartasJogador1)

print('calcular as possibilidades de combinações entre essas cartas:')
comb = combinations([1, 2, 3], 2)
trioJogador1=combinations(cincoCartasJogador1, 3)

for i in list(trioJogador1):
    print (i)



#funcao de calcular os pontos
def calcular_ponto (jogadorNumero1, jogadorNumero2, jogadorNumero3, jogadorNumero4, mesa):
    print('oi oi oi')

        
