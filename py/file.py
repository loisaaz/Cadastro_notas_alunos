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
    aluno = []
    print(f"\nCADASTRO DO(A) ALUNO {i + 1}")
    print('\n------------------------------------------------')
    nome = input("DIGITE O NOME DO ALUNO:")
    T1 = float(input("DIGITE A NOTA DA PROVA TEÓRICA (T1): "))
    while T1 < 0 or T1 > 10:
        print("Nota inválida. Digite um número entre 0 e 10.")
        T1 = float(input("DIGITE A NOTA DA PROVA TEÓRICA (T1): "))

    T2 = float(input("DIGITE A NOTA DA PROVA TEÓRICA (T2): "))
    while T2 < 0 or T2 > 10:
        print("Nota inválida. Digite um número entre 0 e 10.")
        T2 = float(input("DIGITE A NOTA DA PROVA TEÓRICA (T2): "))

    P1 = float(input("DIGITE A NOTA DE PROJETO (P1): "))
    while P1 < 0 or P1 > 10:
        print("Nota inválida. Digite um número entre 0 e 10.")
        P1 = float(input("DIGITE A NOTA DE PROJETO (P1): "))

    P2 = float(input("DIGITE A NOTA DE PROJETO (P2): "))
    while P2 < 0 or P2 > 10:
        print("Nota inválida. Digite um número entre 0 e 10.")
        P2 = float(input("DIGITE A NOTA DE PROJETO (P2): "))

    mt=0,4*T1+0,6*T2
    mp= (P1+P2)/2
    mf= 0,3*mp + 0,7*mt
    print('\n------------------------------------------------')
    cadastro_alunos.append([nome, mt, mp, mf])
    print(f"\nCADASTRO DO ALUNO {nome} CONCLUÍDO COM SUCESSO!")
    for aluno in cadastro_alunos:
        print(f"'{aluno[0]}', MÉDIA TEÓRICA: {aluno[1]}, MÉDIA PRÁTICA: {aluno[2]}, MÉDIA FINAL {aluno[3]}") # essa linha urge de ajustes
        print('\n------------------------------------------------')
# AO INVES DE MOSTRAR AS INFO INSERIDAS NUMA LISTA, DEVEMOS JA MOSTRAR OUTRO RESULTADO, OU SEJA AS NOTAS CALCULADAS
