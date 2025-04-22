#PAGINA INICIAL
print("\nPROGRAMA DE CADASTRO E CÁLCULO DE NOTAS")
print("\nBEM VINDO AO SISTEMA DE CADASTRO DAS NOTAS DOS ALUNOS")
#print("ALGORITMOS DE PROGRAMAÇÃO,PROJETOS E COMPUTAÇÃO")
print("\n A PARTIR DESSE PROGRAMA VOCÊ PODERÁ:")
print("- Cadastrar nomes e notas de alunos")
print("- Calcular as médias teóricas, práticas e a final.")
print("- Consultar alunos com maior/menor média.")
print("- Obter o percentual de alunos com média final acima de 5.")
print("\n<<<Tecle algo para iniciar o programa.>>>")
input()

#PARTE 1
cadastro_alunos = []

num_alunos = int(input("QUANTIDADE DE ALUNOS A CADASTRAR:"))
for i in range(num_alunos):
    print(f"\nCadastro do aluno {i + 1}")
    nome = input("DIGITE O NOME DO ALUNO:")
    T1 = float(input("DIGITE A NOTA DA PROVA TEÓRICA (T1):"))
    T2 = float(input("DIGITE A NOTA DA PROVA TEÓRICA (T2):"))
    P1 = float(input("DIGITE A NOTA DE PROJETO (P1):"))
    P2 = float(input("DIGITE A NOTA DE PROJETO (P2):"))
    print('----------------------------------------')
    if T1 or T2 or P1 or P2 < 0 or T1 or T2 or P1 or P2 > 10: 
        print("\nATENÇÃO! ! !")
        print("\nINSIRA UMA NOTA DE 0 - 10")
        nome = input("DIGITE O NOME DO ALUNO:")
        T1 = float(input("DIGITE A NOTA DA PROVA TEÓRICA (T1):"))
        T2 = float(input("DIGITE A NOTA DA PROVA TEÓRICA (T2):"))
        P1 = float(input("DIGITE A NOTA DE PROJETO (P1):"))
        P2 = float(input("DIGITE A NOTA DE PROJETO (P2):"))
    #adicionar uma condição --> ex: a nota digitada deve estar entre 0 a 10

cadastro_alunos.append([nome, T1, T2, P1, P2])
print("\nCadastro dos Alunos:")
for aluno in cadastro_alunos:
    print(f"Nome: {aluno[0]}, T1: {aluno[1]}, T2: {aluno[2]}, P1: {aluno[3]}, P2: {aluno[4]}")