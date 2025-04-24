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
    if mt > 5 and mp > 5:
        mf = (0.3 * mp) + (0.7 * mt)
    elif mt < mp:
        mf = mt
    else:
        mf = mp

    print('\n---------------------------------------------------------------------------------------------')
    cadastro_alunos.append([
        f"[{nome}], NOTAS TEÓRICAS: [{T1}], {T2}], NOTAS PRÁTICAS: [{P1}, {P2}] MÉDIA TEÓRICA E PRÁTICA: [{mt:.2f}, {mp:.2f}], MÉDIA FINAL: [{mf:.2f}]"])
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


        # o menu 2 não está funcionando



    elif menu == 2:
        pesquisa_aluno = input('\nNome do(a) aluno(a): ')
        for aluno in cadastro_alunos:
            if aluno[0] == pesquisa_aluno:
                print(aluno)
                break
        else:
            print("Aluno(a) não encontrado no sistema.")
    elif menu == 3:

        

# O nome do aluno com maior Média Final (MF)
# O nome do aluno com menor Média Final (MF)
# Percentual dos alunos com Média Final (MF) superior a 5.0