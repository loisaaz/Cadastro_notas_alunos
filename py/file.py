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
        print("\nNOTA INVÁLIDA!! DIGITE UM NÚMERO ENTRE 0 E 10.")
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
        for i in range(0, len(cadastro_alunos), 6):
            nome = cadastro_alunos[i]
            TEORIA = cadastro_alunos[i+1]
            PRATICA = cadastro_alunos[i+2]
            mt = cadastro_alunos[i+3][0]
            mp = cadastro_alunos[i+4][0]
            mf = cadastro_alunos[i+5][0]
            print('\n')
            print(f"[{nome}], NOTAS TEÓRICAS: [{TEORIA[0]}, {TEORIA[1]}], NOTAS PRÁTICAS: [{PRATICA[0]}, {PRATICA[1]}] MÉDIA TEÓRICA E PRÁTICA: [{mt:.2f}, {mp:.2f}], MÉDIA FINAL: [{mf:.2f}]") 
    elif menu == 2:
        nome_aluno = input('\nDigite o nome do aluno(a): ')
        for i in range(0, len(cadastro_alunos), 6):
            if cadastro_alunos[i].lower() == nome_aluno.lower():
                print('\nINFORMAÇÕES DO ALUNO(A):')
                print(f"NOME: {cadastro_alunos[i]}, NOTAS TEÓRICAS: [{cadastro_alunos[i+1][0]}, {cadastro_alunos[i+1][1]}], NOTAS PRÁTICAS: [{cadastro_alunos[i+2][0]}, {cadastro_alunos[i+2][1]}] MÉDIA TEÓRICA E PRÁTICA: [{cadastro_alunos[i+3][0]:.2f}, {cadastro_alunos[i+4][0]:.2f}], MÉDIA FINAL: [{cadastro_alunos[i+5][0]:.2f}]")
                break
        else:
            print("Aluno(a) não encontrado no sistema.")
    elif menu == 3:
        maior_mf = 0
        aluno_maiormf = ''
        for i in range(0, len(cadastro_alunos), 6):
            mf = cadastro_alunos[i+5][0]  
            if mf > maior_mf:
                maior_mf = mf
                aluno_maiormf = cadastro_alunos[i]
        print(f"\nAluno(a) com maior média final: {aluno_maiormf}, MF: {maior_mf:.2f}")
    elif menu == 4:
        menor_mf = 10
        aluno_menormf = ''
        for i in range(0, len(cadastro_alunos), 6):
            mf = cadastro_alunos[i+5][0]  
            if mf < menor_mf:
                menor_mf = mf
                aluno_menormf = cadastro_alunos[i]
        print(f"\nAluno(a) com menor média final: {aluno_menormf}, MF: {menor_mf:.2f}")
    elif menu == 5:
            maior_5 = 0
            for i in range(5, len(cadastro_alunos), 6):  
                if cadastro_alunos[i][0] > 5:
                    maior_5 += 1
                    percentual = (maior_5 / num_alunos) * 100 
            print(f"\nPercentual de alunos com Média Final abaixo de 5: {percentual:.2f}%")
    elif menu == 6:
        print('Encerrando...')
        break