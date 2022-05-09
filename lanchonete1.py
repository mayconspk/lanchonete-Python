print("Bem vindo ao Rei do Lanche! ")
print()

nomeCliente = input("Qual o seu nome? ")
print()
lancheP = 12.50
lancheM = 14.50
lancheG = 16.50
comboBatataRefri = 10.00

print(f'Olá {nomeCliente} Escolha uma das opções abaixo')
lanche_pedido = int(input("[1]X-Burguer P - R$12,50" + "\n" + "[2]X-Burguer M - R$14,50" + "\n" + "[3]X-Burguer G - R$16,50" + "\n" + "Digite a opção desejada: "))
print()
bata_pedido = input("Batata e Refri + R$10,00" + "\n" + "Aceita o combo com Batata e Refrigerante [s] ou [n]: ")
print()
if bata_pedido == 's':
    if lanche_pedido == 1:
        valorPedido = lancheP + comboBatataRefri
        print(f"O combo de lanche P + Batata e Refrigerante ficou: R${valorPedido}")
    elif lanche_pedido == 2:
        valorPedido = lancheM + comboBatataRefri
        print(f"O combo de lanche M + Batata e Refrigerante ficou: R${valorPedido}")
    elif lanche_pedido == 3:
        valorPedido = lancheG + comboBatataRefri
        print(f"O combo de lanche G + Batata e Refrigerante ficou: R${valorPedido}")

elif bata_pedido == 'n':
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
    print("Cabelo para de ser tchola e responde direito")

valorPagamento = float(input("Qual o valor entregue para pagamento? "))
troco = valorPagamento - valorPedido

notinha = input("Deseja gerar uma notinha Sim[s] ou Não[n]? ")
print()
if notinha == 's':
    with open('cupomfiscal.txt', 'w')as cupom:
        valorPagamento = str(valorPagamento)
        valorPedido = str(valorPedido)
        troco = str(troco)
        cupom.write(str("............NOTA FISCAL........." + "\n"))
        cupom.write(str(f'Nome do cliente................{nomeCliente}' + '\n'))
        cupom.write(str(f'Valor pago:..................R${valorPagamento}' + '\n'))
        cupom.write(str(f'Valor do pedido:.............R${valorPedido}' + '\n'))
        cupom.write(str(f'Troco:.......................R${troco}' + '\n'))
        cupom.write(str('================================' + '\n'))
        print(f"Seu troco deu R${troco} tenha uma ótima refeição e volte sempre!")
else:
    print(f"Seu troco deu R${troco} tenha uma ótima refeição e volte sempre")