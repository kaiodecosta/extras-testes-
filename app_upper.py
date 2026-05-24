def main():
    texto = input('Texto: ')
    novo_texto = Upper(texto)
    print(f'{novo_texto}')
    
    
def Upper(texto):
    novo_texto = ''
    for letra in texto:
        if 97 <= ord(letra) <= 122:
            letra_maiuscula = ord(letra) - 32
            novo_texto += chr(letra_maiuscula)
        else:
            novo_texto += letra
    return novo_texto
            
main()