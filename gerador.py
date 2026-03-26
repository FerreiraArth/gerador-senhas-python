import random
import string

def gerar_senha(tamanho=12, usar_simbolos=True):
    letras = string.ascii_letters #abcABC
    numeros = string.digits #123
    simbolos = string.punctuation #!@#$%

    caracteres = letras + numeros

    if usar_simbolos:
        caracteres += simbolos

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho)) #Esconhe um caracter aleatorio varias vezes e junta tudo em uma string

    return senha

def main():
    print("=== Gerador de senhas seguras ===")
    
    tamanho = int(input("Digite o tamanho da senha: "))
    simbolos = input("Incluir simbulos? (s/n): ").lower() == 's'

    senha = gerar_senha(tamanho, simbolos)

    print(f"\nSenha gerada: {senha}")

if __name__ == "__main__":
    main()