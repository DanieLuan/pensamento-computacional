while True:
    numPlayer = int(input('Quantidade de jogadores? '))
    if numPlayer >= 1:
        break
print('Digite os dados para cada jogador:')
playerStats = []
for i in range(numPlayer):
    stats = input('').split(' ')
    stats.pop(0)
    playerStats.append(stats)
teamStats = [0,0,0,0,0,0]
for i in range(numPlayer):
    for j in range(6):
        teamStats[j] = teamStats[j] + int(playerStats[i][j])
print('=-'*20)
print('As estatísticas do jogo são as seguintes:')
print('Porntos de Saque: {:.2f} %'.format((teamStats[3] / teamStats[0]) * 100))
print('Pontos de Bloqueio: {:.2f} %'.format((teamStats[4] / teamStats[1]) * 100))
print('Pontos de Ataque: {:.2f} %'.format((teamStats[5] / teamStats[2]) * 100))
print('=-'*20)