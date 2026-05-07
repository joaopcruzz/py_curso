numero_da_conta_do_banco = float (input("conta do banco:"))
saldo_da_conta = float (input("qual o saldo da conta:"))
valor_do_debito = float (input("qual o valor do debito:"))
valor_do_credito = float (input("qual o valor do credito:"))
saldo_atual = saldo_da_conta - valor_do_debito + valor_do_credito
print ("saldo atual:", saldo_da_conta)
if saldo_atual >= 0:
    print ("saldo positivo")
else:
    print ("saldo negativo")