nome = input("Qual seu nome: ")
ano_atual = int(input("Em que ano estamos: "))
nascimento = int(input("Em que ano voçê nasceu: "))
idade = (int (ano_atual - nascimento))
print(f"{nome} Sua idade e {idade} anos atualmente no ano de {ano_atual}")