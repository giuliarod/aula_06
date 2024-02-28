import random

p1 = input('Jogador 1, digite o seu nome:')
p2 = input('Jogador 2, digite o seu nome:')
n = [4, 3, 2, 1]
for c in n:
    randomico = random.randint(1,10)
                          
    jogador1 = int(input(f'{p1}, por favor, digite o seu número:'))
    jogador2 = int(input(f'{p2}, é sua vez! Por favor, digite o seu número:'))
    c = c - 1

    if jogador1 == randomico and jogador2 == randomico:
        print(f'Empate! {p1} e {p2} acertaram!')
        break
    
    if randomico == jogador1:
        print(f'Você acertou, {p1}! O número é {randomico}')
        break
    
    if randomico == jogador2:
        print(f'Você acertou, {p2}! O número é {randomico}')
        break

    elif randomico != jogador1 or jogador2 and randomico > 0:
        print(f'Vocês erraram! O número correto é {randomico}, restam apenas {c} vida(s)')
        if c == 0:
            print(f'Suas vidas acabaram, game over :( total de vida(s)>>{c}')
            break



        




