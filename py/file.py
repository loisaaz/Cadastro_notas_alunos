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
    mf = (0.3 * mp) + (0.7 * mt)
    print('\n---------------------------------------------------------------------------------------------')
    cadastro_alunos.append([f"'{nome}', 'Média teórica: {mt:.2f}', 'Média prática: {mp:.2f}', 'Média final: {mf:.2f}'"])
    print(f"\nCADASTRO DO(A) ALUNO(A) {nome} CONCLUÍDO COM SUCESSO!")
    print('\n---------------------------------------------------------------------------------------------')
for aluno in cadastro_alunos:
    print(aluno) 
    print('\n---------------------------------------------------------------------------------------------')

print("\nPROGRAMA DE CADASTRO E CÁLCULO DE NOTAS")
print('\n<<< MENU >>>')
menu = int(input('\nCONSULTAR ALUNO(A) = 1 | CONSULTAR ALUNO COM MAIOR MÉDIA FINAL = 2 \nCONSULTAR ALUNO COM MENOR MÉDIA FINAL = 3 | PERCENTUAL DE ALUNOS COM MÉDIA FINAL SUPERIOR A 5 = 4 \nDIGITE SUA ESCOLHA:')) 
if menu == 1:
    nome_consulta = input('\nDIGITE O NOME DO ALUNO: ')
#    for aluno in cadastro_alunos: 
#        if algo == nome_consulta: 
#            print(f"\nINFORMAÇÕES DO(A) ALUNO(A) {aluno[0]}:")
#            print(aluno) 
#        else:
#            print("\nALUNO NÃO CADASTRADO NO SISTEMA.")
#elif menu == 2:

    
# O nome do aluno com maior Média Final (MF)
# O nome do aluno com menor Média Final (MF)
# Percentual dos alunos com Média Final (MF) superior a 5.0