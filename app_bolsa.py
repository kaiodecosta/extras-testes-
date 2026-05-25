import os

def main():
    acoes = ['000']
    menu = '''
    -=-=-=- Bolsa de Valores -=-=-=-
    Mostrar ações (1) _____________
    Adicionar ação (2) ____________
    Remover ação (3) ______________
    Ação mais valiosa (4) _________
    Ação menos valiosa (5) ________
    Capital total da bolsa (6) ____
    Sair (0) ______________________
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Inserir opção:  '''
    while True:
        limpar_tela()
        comando = obter_numero_faixa(menu, 6, 0)
        
        if comando == 1:
            limpar_tela()
            if acoes  == ['000']:
                print('Não existe nenhuma ação registrada.')
            else:
                limpar_tela()
                for acao in acoes:
                    if not acao == '000':
                        print(acao)
            input('Pressione enter para voltar ao menu.')
            
        elif comando == 2:          #adiciona uma ação de acordo com o modelo correto
            limpar_tela()
            while True:
                print('Caso queira sair sem adicionar uma ação, digite "0".')
                adicionar = input('Insira aqui a ação (Código, Nome, Preço das ações, Quant. de ações): ')
                if adicionar == '0':
                    limpar_tela()
                    break
                else:
                    adicionar = adicionar.split()

                    if checar_se_correto(adicionar, acoes) == 'codigo':
                        limpar_tela()
                        print('Ação não adicionada! Uma ação com esse código já existe.')
                        print('')

                    elif checar_se_correto(adicionar, acoes) == 'tipagem':
                        limpar_tela()
                        print('Ação não adicionada! Tipagem incorreta.')
                        print('Digite um número maior que 0, tanto para o preço quanto para a quantidade!')
                        print('')
                        
                    elif checar_se_correto(adicionar, acoes) == 'tipagem2':
                        limpar_tela()
                        print('Ação não adicionada! Tipagem incorreta.')
                        print('Digite uma ação conforme o modelo mostrado (com um espaço entre as diferentes caractestísticas)!')
                        print('')

                    elif checar_se_correto(adicionar, acoes) == 'correto':
                        acoes.append(adicionar)
                        input('Ação adicionada!')
                        limpar_tela()
                        break
                
        elif comando == 3:          #remove uma ação selecionada
            if acoes == ['000']:
                print('Não é possível remover a ação. Não existe nenhuma ação registrada.')
            else:
                limpar_tela()
                if acao != '000':
                    for index in range(1, (len(acoes))):
                        print(f'{index} - {acoes[index]}')
                print('Selecione A ação que você deseja remover')
                remover = obter_numero_faixa('',len(acao), 1)
                    
                print('Você realmente deseja remover a ação? Digite "1" para "Sim" e "0" para "Não"')
                decisao = obter_numero_faixa('', 1, 0)
                if decisao == 0:
                    limpar_tela()
                else:
                    acoes.pop(int(remover))
                    print('Ação removida.')
                    input('Pressione enter para voltar ao menu.')
                    
        elif comando == 4:          #mostra a ação mais valiosa
            if acoes == ['000']:
                print('Não existe nenhuma ação registrada.')
                input('Pressione enter para voltar ao menu.')
            else:
                limpar_tela()
                checar_mais_valiosa(acoes)
                input('Pressione enter para voltar ao menu.')
                
        elif comando == 5:          #mosta a ação menos valiosa
            if acoes == ['000']:
                print('Não existe nenhuma ação registrada.')
                input('Pressione enter para voltar ao menu.')
            else:
                limpar_tela()
                checar_menos_valiosa(acoes)
                input('Pressione enter para voltar ao menu.')
                
        elif comando == 6:          #calcula o capital total
            if acoes == ['000']:
                print('Não existe nenhuma ação registrada.')
                input('Pressione enter para voltar ao menu.')
            else:
                limpar_tela()
                calcular_capital(acoes)
                input('Pressione enter para voltar ao menu.')
                
        elif comando == 0:
            print('Você saiu!')
            break
        
def limpar_tela():          #limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    
def checar_se_correto(adicionar, acoes):            #checa se a ação está de acordo com o modelo e se tanto o preço quanto a quantidade são positivos diferentes de zero
    if len(adicionar) != 4:
        return 'tipagem2'
    elif float(adicionar[2]) < 1 or int(adicionar[3]) < 1:
            return 'tipagem'
    for acao in acoes:
        if str(acao[0]) == str(adicionar[0]):
            return 'codigo'
    else:
        return 'correto'
    
def checar_mais_valiosa(acoes):         #função para o comando 4
    maior = [1, 1, 1, 1]
    for acao in acoes:
        if acao == '000':
            continue
        else:
            valor = float(acao[2]) * int(acao[3])
            valor_maior = float(maior[2]) * int(maior[3])
            if valor > valor_maior:
                maior = acao
    print(f'A ação da {maior[1]} é a mais valiosa, custando R${float(maior[2]) * int(maior[3])}.')

def checar_menos_valiosa(acoes):            #função para o comando 5
    menor = [9, 9, 999999999, 999999]
    for acao in acoes:
        if acao == '000':
            continue
        else:
            valor = float(acao[2]) * int(acao[3])
            valor_menor = float(menor[2]) * int(menor[3])
            if valor < valor_menor:
                menor = acao
    print(f'A ação da {menor[1]} é a menos valiosa, custando R${float(menor[2]) * int(menor[3])}.')
    
def calcular_capital(acoes):            #função para o comando 6
    total = 0
    for acao in acoes:
        if acao == '000':
            continue
        else:
            valor = float(acao[2]) * int(acao[3])
            total += valor
    print(f'O valor total do capital desta bolsa é de R${total}')

def obter_numero(a:str):            #função que garante a obtenção de um número, em float
    while True:
        try:
            return float(input(a))
        except:
            print('Por favor insira um número.')
    
def obter_numero_faixa(a, maximo, minimo):          #garante que o número obtido está dentro de uma faixa selecionada pelo programador
    numero = obter_numero(a)
    while True:
        if minimo <= numero <= maximo:
            return numero
        else:
            print(f'Por favor insira um número entre {minimo} e {maximo}')
            numero = obter_numero(a)
            
       
main()
