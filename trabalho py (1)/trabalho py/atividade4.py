compra = int(input("valor da compra:"))
d = int(input("valor do desconto:"))
valor_sem_desconto = compra
valor_do_desconto = (d / 100) * 100
valor_com_desconto = valor_sem_desconto- valor_do_desconto
print ("sem o desconto:", valor_sem_desconto)
print (" desconto:", valor_do_desconto)
print ("com o desconto:", valor_com_desconto)

