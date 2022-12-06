# Pedra Papel Tesoura
# Vamos jogar! Você tem que retornar qual jogador ganhou! Em caso de empate retornar Draw!.

# Exemplos (Entrada1, Entrada2 --> Saída):
# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!

def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == 'scissors' and p2 == 'paper':
        return "Player 1 won!"
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    elif p1 == 'rock' and p2 == 'scissors':
        return "Player 1 won!"
    else:
        return "Player 2 won!"

# Resolução mais eficiente
# def rps(p1, p2):
#     beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!