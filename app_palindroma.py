def main():
    texto = input('Texto: ')
    
    txt_inverso = texto[::-1]
    
    checar_se_palindroma(texto, txt_inverso)
    
    
def checar_se_palindroma(texto, txt_inverso):
    if texto == txt_inverso:
        print('Essa palavra é uma Palíndroma!!')
    else:
        print('Essa palavra não é uma Palíndroma.')
    
main()
        