nota_1 = float (input("qual a sua primeira nota:"))
nota_2 = float (input("qual a sua segunda nota:"))
media = (nota_1 + nota_2) / 2
print ("sua media final foi:", media)
if media >= 70:
    print("aprovado")
elif media >= 40:
    print("reprovado")
else:
    print("final")
if media >= 90 and media >= 100:
    print("conceito a")
elif media >= 70 and media >= 90:
    print("conceito b")
elif media >= 40 and media >= 70:
    print("conceito c")
else:
    print("conceito d")