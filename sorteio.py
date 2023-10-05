import random

# Solicita os dois números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número (deve ser maior que o primeiro): "))

# Verifica se o segundo número é maior que o primeiro
if num2 <= num1:
    print("Erro: o segundo número deve ser maior que o primeiro.")
else:
    # Gera um número aleatório entre os dois números fornecidos
    num_aleatorio = random.randint(num1, num2)
    
    # Exibe o número aleatório gerado
    print(f"Um número aleatório entre {num1} e {num2} é: {num_aleatorio}")

