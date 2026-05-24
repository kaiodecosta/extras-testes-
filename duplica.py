def main():
    texto = input('Texto: ')
    duplica(texto)
    
    
        
def duplica(texto):
    texto_novo = ''
    for i in texto:
        texto_novo += i + i
        
    print(texto_novo)

main()