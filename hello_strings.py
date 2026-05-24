def main():
    nome = input('nome: ')
    em_caixa_alt = upper(nome)
    print(em_caixa_alt)
    
def upper(a):
    novo_nome = ''
    for i in a:
        novo_nome += upper_caracter(i)
    return novo_nome
    
def upper_caracter(a):
    if verificar_se_caixa_alta(a):
        novo_codigo = ord(a) - 32
        novo_nome = chr(novo_codigo)
        return novo_nome
    else:
        return a
    
def verificar_se_caixa_alta(a):
    if ord(a) >= 92 and ord(a) <= 122:
        return True

main()