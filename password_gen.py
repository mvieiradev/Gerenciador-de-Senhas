import random
import string

def gerar_senha():
    tamanho = int(input("Quantos caracteres você deseja na senha? "))
    
    usar_letras = input("Deseja incluir letras na senha? (s/n): ").lower() == 's'
    usar_numeros = input("Deseja incluir números na senha? (s/n): ").lower() == 's'

    caracteres = ''
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits

    if not caracteres:
        print("Você precisa escolher pelo menos letras ou números. Tente novamente.")
        return None

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso
senha_gerada = gerar_senha()

if senha_gerada:
    print("Senha gerada:", senha_gerada)
