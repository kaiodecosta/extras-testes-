from fun_io import obter_real, escrever, obter_texto

def main():
    nome = obter_texto('qual seu nome? ')
    peso = obter_real(' qual seu peso? (kg): ')
    altura = obter_real('qual sua altura? (m): ')
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    
    escrever(f'{nome}, seu imc é {imc:.2f} e sua classificação é {classificacao}')


def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc


def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso normal.'
    elif imc < 25:
        return 'Peso normal.'
    elif imc < 30:
        return 'Exesso de peso'
    elif imc < 35:
        return 'Obesidade 1'
    elif imc < 40:
        return 'Obesidade 2'
    else:
        return 'Obesidade 3'
    

main()