chave = input("Digite a base de sua senha.")
senha = ""

for letra in chave:
    if letra in "Aa":
        senha = senha + "!"
    elif letra in "Bb":
        senha = senha + "@"
    elif letra in "Cc":
        senha = senha + "#"
    elif letra in "Dd":
        senha = senha + "$"
    elif letra in "Ee":
        senha = senha + "%"
    elif letra in "Ii":
        senha = senha + "¨"
    elif letra in "Oo":
        senha = senha + "&"
    elif letra in "Uu":
        senha = senha + "*"
    elif letra in "Rr":
        senha = senha + "("
    elif letra in "Yy":
        senha = senha + ")"
    else:
        senha = senha + letra
print(senha)
