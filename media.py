print("------------------------------------")
#variaveis / entrada 
n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota : '))
print("------------------------------------")

# regra de negócio / lógica
m = (n1+n2)/2

# saida
print(f'A sua média foi : {m:.1f}')

if m >= 7:
	print("Parabéns, você está aprovado")
else: 
	print("Não foi dessa vez. faça a reposição da disciplina")

