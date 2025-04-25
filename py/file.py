print("\nPROGRAMA DE CADASTRO E CÁLCULO DE NOTAS")
print("\nBEM VINDO AO SISTEMA DE CADASTRO DAS NOTAS DOS ALUNOS")
print("\n A PARTIR DESSE PROGRAMA VOCÊ PODERÁ:")
print("- Cadastrar nomes e notas de alunos")
print("- Calcular as médias teóricas, práticas e a final.")
print("- Consultar alunos com maior/menor média.")
print("- Obter o percentual de alunos com média final acima de 5.")
print("\n<<<Tecle algo para iniciar o programa>>>")
input()

cadastro_alunos = []
num_alunos = int(input("QUANTIDADE DE ALUNOS A CADASTRAR:"))

for i in range(num_alunos):
    aluno = []
    print(f"\nCADASTRO DO(A) ALUNO {i + 1}")
    nome = input("\nDIGITE O NOME DO ALUNO:")

    TEORIA = []

    T1 = float(input("\nDIGITE A NOTA DA PROVA TEÓRICA (T1): "))
    while T1 < 0 or T1 > 10:
        print("\nNOTA INVÁLIDA!! DIGITE UM NÚMERO ENTRE 0 E 10.")
        T1 = float(input("\nDIGITE A NOTA DA PROVA TEÓRICA (T1): "))

    T2 = float(input("\nDIGITE A NOTA DA PROVA TEÓRICA (T2): "))
    while T2 < 0 or T2 > 10:
        print("\nTNOTA INVÁLIDA!! DIGITE UM NÚMERO ENTRE 0 E 10.")
        T2 = float(input("\nDIGITE A NOTA DA PROVA TEÓRICA (T2): "))

    TEORIA.append(T1)
    TEORIA.append(T2)

    PRATICA = []

    P1 = float(input("\nDIGITE A NOTA DE PROJETO (P1): "))
    while P1 < 0 or P1 > 10:
        print("\nNOTA INVÁLIDA!! DIGITE UM NÚMERO ENTRE 0 E 10.")
        P1 = float(input("\nDIGITE A NOTA DE PROJETO (P1): "))

    P2 = float(input("\nDIGITE A NOTA DE PROJETO (P2): "))
    while P2 < 0 or P2 > 10:
        print("\nNOTA INVÁLIDA!! DIGITE UM NÚMERO ENTRE 0 E 10.")
        P2 = float(input("DIGITE A NOTA DE PROJETO (P2): "))

    PRATICA.append(P1)
    PRATICA.append(P2)

    mt = (0.4 * T1) + (0.6 * T2)
    mp = (P1 + P2) / 2
    if mt > 5 and mp > 5:
        mf = (0.3 * mp) + (0.7 * mt)
    elif mt < mp:
        mf = mt
    else:
        mf = mp
    MEDIATEORICA = [mt]
    MEDIAPRATICA = [mp]
    MEDIAFINAL = [mf]
    print('\n---------------------------------------------------------------------------------------------')
    cadastro_alunos.append(nome)
    cadastro_alunos.append(TEORIA)
    cadastro_alunos.append(PRATICA)
    cadastro_alunos.append(MEDIATEORICA)
    cadastro_alunos.append(MEDIAPRATICA)
    cadastro_alunos.append(MEDIAFINAL)
#    cadastro_alunos.append(aluno)
    print(f"\nCADASTRO DO(A) ALUNO(A) {nome} CONCLUÍDO COM SUCESSO!")
    print('\n---------------------------------------------------------------------------------------------')

menu = 0

while menu != 6:
    print("\n<< MENU >>")
    print('\n')
    print("1. Consultar boletim dos alunos")
    print("2. Consultar um aluno")    
    print("3. Nome do aluno com maior Média Final (MF)")
    print("4. Nome do aluno com menor Média Final (MF)")
    print("5. Percentual de alunos com Média Final (MF) acima de 5")
    print("6. Sair")

    menu = int(input("\nDigite sua escolha: "))

    if menu == 1:
        print("\nBOLETIM DOS ALUNOS:")
        for aluno in cadastro_alunos:
            print('\n')
            print(aluno)
            # for i in range(0, len(cadastro_alunos), 6): \ if cadastro_alunos[i] == nome_aluno:
    elif menu == 2:
        nome_aluno = input('\nNome do(a) aluno(a): ')
        for aluno in cadastro_alunos:
            cadastro_alunos == nome_aluno
            print('\nINFORMAÇÕES DO ALUNO PESQUISADO')
            print('\n')
            print(aluno)
            break
        else:
            print("Aluno(a) não encontrado no sistema.")
    elif menu == 3:
        maior_mf = 0
        for aluno in cadastro_alunos:
           # mf = aluno[-1] # ultimo elemento  
            if mf > maior_mf:  
                maior_mf = mf
                aluno_maiormf = aluno[0] 
                print(f"Aluno com maior média final: {aluno_maiormf}, Média Final: {maior_mf}")

# O nome do aluno com maior Média Final (MF)
# O nome do aluno com menor Média Final (MF)
# Percentual dos alunos com Média Final (MF) superior a 