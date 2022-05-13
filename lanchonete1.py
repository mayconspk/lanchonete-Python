# Programa para testar habilidades em python
import os
os.system('cls')
print("Bem vindo ao Rei do Lanche! ")
nomeCliente = input("Qual o seu nome?\n>>")
lancheP = 12.50
lancheM = 14.50
lancheG = 16.50
comboBatataRefri = 10.00
print(f'Olá {nomeCliente} Escolha uma das opções abaixo:\n>>')
#menu basico pra ficar mais organizado
def main():
    print('''
    [1] - X-Burguer P - R$12,50
    [2] - X-Burguer M - R$14,50
    [3] - X-Burguer G - R$16,50
    ''')
    lanche_pedido = int(input("Digite a opção desejada:\n>>"))
    bata_pedido = input("Batata e Refri + R$10,00" + "\n" + "Aceita o combo com Batata e Refrigerante [s] ou [n]:\n>>")
    if bata_pedido == 's' or bata_pedido == 'S':
        if lanche_pedido == 1:
            valorPedido = lancheP + comboBatataRefri
            print(f"O combo de lanche P + Batata e Refrigerante ficou: R${valorPedido}")
        elif lanche_pedido == 2:
            valorPedido = lancheM + comboBatataRefri
            print(f"O combo de lanche M + Batata e Refrigerante ficou: R${valorPedido}")
        elif lanche_pedido == 3:
            valorPedido = lancheG + comboBatataRefri
            print(f"O combo de lanche G + Batata e Refrigerante ficou: R${valorPedido}")

    elif bata_pedido != 's' or bata_pedido != 'S':
        if lanche_pedido == 1:
            valorPedido = lancheP
            print(f"O valor do lanche P ficou: R${valorPedido}")
        elif lanche_pedido == 2:
            valorPedido = lancheM
            print(f"O valor do lanche M ficou: R${valorPedido}")
        elif lanche_pedido == 3:
            valorPedido = lancheG
            print(f"O valor do lanche G ficou: R${valorPedido}")
    else:
        print("Erro, tente novamente")
    valorPagamento = float(input("Qual o valor entregue para pagamento?\n>>"))
    troco = valorPagamento - valorPedido

    notinha = input("Deseja gerar uma Nf-E Sim[s] ou Não[n]?\n>>")
     #limpa tela
    os.system('cls')
    if notinha == 's':
        with open('Cupomfiscal.txt', 'w') as cupom:
            valorPagamento = str(valorPagamento)
            valorPedido = str(valorPedido)
            troco = str(troco)
            cupom.write(str("="*14 + "NOTA FISCAL" + "="*14 + "\n"))
            cupom.write(str(' Nome do cliente:' + '.'*13 + f'{nomeCliente}' + '\n'))
            cupom.write(str(' Valor do pedido:' + '.'*13 + 'R$' + f'{valorPedido}' + '\n'))
            cupom.write(str(' Valor pago:' + '.'*18 + 'R$' + f'{valorPagamento}' + '\n'))
            cupom.write(str(' Troco:' + '.'*23 + 'R$' + f'{troco}' + '\n'))
            cupom.write(str('='*39 + '\n'))
            print(f"Seu troco deu R${troco}")
            cupom.close()
        #relatorio do dia
        with open('Relatorio_geral.txt', 'a+') as cupom:
            valorPagamento = str(valorPagamento)
            valorPedido = str(valorPedido)
            troco = str(troco)
            cupom.write(str("="*14 + "NOTA FISCAL" + "="*14 + "\n"))
            cupom.write(str(' Nome do cliente:' + '.'*13 + f'{nomeCliente}' + '\n'))
            cupom.write(str(' Valor do pedido:' + '.'*13 + 'R$' + f'{valorPedido}' + '\n'))
            cupom.write(str(' Valor pago:' + '.'*18 + 'R$' + f'{valorPagamento}' + '\n'))
            cupom.write(str(' Troco:' + '.'*23 + 'R$' + f'{troco}' + '\n'))
            cupom.write(str('='*39 + '\n'))
            cupom.close()
            cupom_imprimir = str(input('Deseja imprimir sua nota fiscal Sim[s] ou Não[n]?\n>>'))
            #limpa tela
            os.system('cls')
            #imprime na tela tudo que esta no aquivo nf-e
            if cupom_imprimir == 's' or cupom_imprimir == 'S':
                with open("Cupomfiscal.txt","r", encoding="utf-8") as cupom: texto = cupom.read()
                print(texto)
            else:
                print("Tenha uma ótima refeição e volte sempre!")
    else:
        print(f"Seu troco deu R${troco} tenha uma ótima refeição e volte sempre")
        #relatorio do dia
        with open('Relatorio_geral.txt', 'a+') as cupom:
                    valorPagamento = str(valorPagamento)
                    valorPedido = str(valorPedido)
                    troco = str(troco)
                    cupom.write(str("="*14 + "NOTA FISCAL" + "="*14 + "\n"))
                    cupom.write(str(' Nome do cliente:' + '.'*13 + f'{nomeCliente}' + '\n'))
                    cupom.write(str(' Valor do pedido:' + '.'*13 + 'R$' + f'{valorPedido}' + '\n'))
                    cupom.write(str(' Valor pago:' + '.'*18 + 'R$' + f'{valorPagamento}' + '\n'))
                    cupom.write(str(' Troco:' + '.'*23 + 'R$' + f'{troco}' + '\n'))
                    cupom.write(str('='*39 + '\n'))
                    cupom.close()
main()        