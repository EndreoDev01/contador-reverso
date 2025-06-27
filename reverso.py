# reverso.py

def ler_contador():
    try:
        with open("contador.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 100  # começa de 100

def salvar_contador(valor):
    with open("contador.txt", "w") as f:
        f.write(str(valor))

contador = ler_contador()
contador -= 1
salvar_contador(contador)

print(f"Contador reverso: {contador}")