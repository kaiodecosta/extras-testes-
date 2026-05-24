def main():
    texto = input('Texto: ')
    separador = input('Separador: ')
    lista = Split(texto, separador)
    
    print(lista)
    
def Split(texto, separador):
    string_temp = ''
    lista = []
    for caractere in texto:
        if caractere == separador:
            lista.append(string_temp)
            string_temp = ''
        else:
            string_temp += caractere
    lista.append(string_temp)
    return lista

main()
            