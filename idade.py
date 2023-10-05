import datetime

# Solicita o nome do usuário
nome = input("Qual é o seu nome? ")

# Solicita a data de nascimento do usuário
data_nascimento_str = input("Quando você nasceu (dd/mm/aaaa)? ")

# Converte a string da data de nascimento em um objeto datetime
data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Calcula a idade do usuário
hoje = datetime.datetime.today()
idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

# Exibe a idade do usuário
print(f"Olá, {nome}! Você tem {idade} anos.")

