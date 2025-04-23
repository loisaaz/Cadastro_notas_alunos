#PAGINA INICIAL
print("\nPROGRAMA DE CADASTRO E CÁLCULO DE NOTAS")
print("\nBEM VINDO AO SISTEMA DE CADASTRO DAS NOTAS DOS ALUNOS")
#print("ALGORITMOS DE PROGRAMAÇÃO,PROJETOS E COMPUTAÇÃO")
print("\n A PARTIR DESSE PROGRAMA VOCÊ PODERÁ:")
print("- Cadastrar nomes e notas de alunos")
print("- Calcular as médias teóricas, práticas e a final.")
print("- Consultar alunos com maior/menor média.")
print("- Obter o percentual de alunos com média final acima de 5.")
print("\n<<<Tecle algo para iniciar o programa>>>")
input()

#PARTE 1
cadastro_alunos = []
num_alunos = int(input("QUANTIDADE DE ALUNOS A CADASTRAR:"))

for i in range(num_alunos):
    aluno = []
    print(f"\nCADASTRO DO(A) ALUNO {i + 1}")
    nome = input("\nDIGITE O NOME DO ALUNO:")
    
    T1 = float(input("\nDIGITE A NOTA DA PROVA TEÓRICA (T1): "))
    while T1 < 0 or T1 > 10:
        print("\nNOTA INVÁLIDA!! DIGITE UM NÚMERO ENTRE 0 E 10.")
        T1 = float(input("\nDIGITE A NOTA DA PROVA TEÓRICA (T1): "))

    T2 = float(input("\nDIGITE A NOTA DA PROVA TEÓRICA (T2): "))
    while T2 < 0 or T2 > 10:
        print("\nNOTA INVÁLIDA!! DIGITE UM NÚMERO ENTRE 0 E 10.")
        T2 = float(input("\nDIGITE A NOTA DA PROVA TEÓRICA (T2): "))

    P1 = float(input("\nDIGITE A NOTA DE PROJETO (P1): "))
    while P1 < 0 or P1 > 10:
        print("\nNOTA INVÁLIDA!! DIGITE UM NÚMERO ENTRE 0 E 10.")
        P1 = float(input("\nDIGITE A NOTA DE PROJETO (P1): "))

    P2 = float(input("\nDIGITE A NOTA DE PROJETO (P2): "))
    while P2 < 0 or P2 > 10:
        print("\nNOTA INVÁLIDA!! DIGITE UM NÚMERO ENTRE 0 E 10.")
        P2 = float(input("DIGITE A NOTA DE PROJETO (P2): "))

    mt = (0.4 * T1) + (0.6 * T2)
    mp = (P1 + P2) / 2
    mf = (0.3 * mp) + (0.7 * mt)
    print('\n---------------------------------------------------------------------------------------------')
    cadastro_alunos.append([f"{nome}, Média teórica: {mt:.2f}, Média prática: {mp:.2f}, Média final: {mf:.2f}"])
    print(f"\nCADASTRO DO(A) ALUNO(A) {nome} CONCLUÍDO COM SUCESSO!")
    print('\n---------------------------------------------------------------------------------------------')

for aluno in cadastro_alunos:
    print(aluno) 
    print('\n---------------------------------------------------------------------------------------------')

