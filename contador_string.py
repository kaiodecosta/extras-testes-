def main():
    texto = input('Insira um texto: ')
    maiusculas = qtd_maiusculas(texto)
    minusculas = qtd_minusculas(texto)
    numeros = qtd_numeros(texto)
    
    resultado = f'''
    >>> Resultado <<<
    Tamanho: {len(texto)}
    Qtd_maiusculas: {maiusculas}
    Qtd_minusculas: {minusculas}
    Qtd_numeros: {numeros}
    '''
    
    print(resultado)
    
def qtd_maiusculas(texto):
    contador = 0
    for i in texto:
        if 97 <= ord(i) <= 122:
            contador += 1
            
    return contador

def qtd_minusculas(texto):
    contador = 0
    for i in texto:
        if 65 <= ord(i) <= 90:
            contador += 1
            
    return contador

def qtd_numeros(texto):
    contador = 0
    for i in texto:
        if 48 <= ord(i) <= 57:
            contador += 1
            
    return contador

main()