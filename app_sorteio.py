import random
def main():
    numero = random.randint(1, 100)
    pontuacao = 100
    tentativa = 1
    print('Um número secreto entre 1 a 100 foi sorteado!! faça um chute')
    sorteado = int(input('Insira aqui o seu palpite: '))
    
    if sorteado == numero:
        print('Parabéns!! você acertou o número secreto!!!')
        print(f'Você acertou na {tentativa}° tentativa e a sua pontuação foi de {pontuacao} pontos')
    
    while numero != sorteado:
        
        tentativa += 1
        pontuacao -= 10
            
        if sorteado > numero:
            print('Errado! o número secreto é menor que esse.')
            print(f'Essa é a sua {tentativa}° tentativa e você está com {pontuacao} pontos!')
            sorteado = int(input('Insira aqui o seu outro palpite: '))
            
        if sorteado < numero:
            print('Errado! o número secreto é maior que esse.')
            print(f'Essa é a sua {tentativa}° tentativa e você está com {pontuacao} pontos!')
            sorteado = int(input('Insira aqui o seu outro palpite: '))
            
        if sorteado == numero:
            print('Parabéns!! você acertou o número secreto!!!')
            print(f'Você acertou na {tentativa}° tentativa e a sua pontuação foi de {pontuacao} pontos')
            break
            
        if tentativa == 10:
            print(f'Você já fez {tentativa} tentativas e agora está com {pontuacao-10} pontos, o número secreto era {numero}')
            break
        
main()
            
        