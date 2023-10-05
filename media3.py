aluno = str(input("Digite o nome do Aluno : "))
nota1 = float(input("Digite a primeira nota : "))
nota2 = float(input("Digite a segunda nota : "))
nota3 = float(input("Digite a terceira nota : "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média das notas é: {media:.2f}")

if media >= 7 :
	print("Aluno :  "+aluno+ " está aprovado")
else :
	print("Aluno : "+aluno+" foi reprovado")







