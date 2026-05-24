def main():
    contador = 0
    n = obter_inteiro('Insira um número: ')
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end= " - ")
            contador += 1
    
    print('Fim')
    print(f'Esse número possui {contador} divisores')

def obter_inteiro(a:str):
    while True:
        try: 
           return int(input(a))
        except:
            print("Favor inserir um número válido.")
        
            
main()
                