print('Vamos calcular sua média!')
print('\n')
input('Aperte enter para continuar.')
print('\n')

notas = []
pesos = []

def med_s(j,k):
    soma = 0
    for i in j:
        soma += i
    media = soma/k
    return media
def med_p(i,j):
    mult_l = [a*b for a,b in zip(i,j)]
    for a in mult_l:
        dividendo += a
    for b in j:
        divisor += b
    media = dividendo/divisor
    return media
def nota():
    vez = 1
    v_nops = False
    while len(notas) < np:
        while v_nops == False:
            nota = input('Insira a nota da prova ' + str(vez) + ': ')
            try:
                nota = float(nota)
                if nota < 0 or nota > 10:
                    print('A nota não pode ser maior do que DEZ e menor do que ZERO.')
                else:
                    v_nops = True
            except:
                print('Utilize ponto no lugar de vírgula para separar os decimais.')
        notas.append(nota)
        vez += 1
        v_nops = False
def peso():
    vez = 1
    v_nops = False
    while len(pesos) < np:
        while v_nops == False:
            peso = input('Insira o peso da prova ' + str(vez) + ': ')
            try:
                peso = float(peso)
                if peso < 0 or peso > 1:
                    print('O peso da nota não pode ser menor do que zero'
                          'e maior do que dez.')
                else:
                    v_nops = True
            except:
                print('Utilise ponto no lugar de vírgula para separar os decimais')
        pesos.append(peso)
        vez += 1
        v_nops = False

v_med = False
while v_med == False:
    t_med = input('Qual o tipo de média você gostaria de calcular?\n Para'
        ' média simples digite "S", ou "P" para média ponderada? ').strip().lower()
    if t_med != 's' and t_med != 'p':
        print('Digite "S" para média simples ou "P" para média ponderada.')
    else:
        v_med = True

print('\n')

v_nops = False
while v_nops == False:
    np = input('Quantas provas você teve? ')
    try:
        np = float(np)
        if np <= 1:
            print('O número de provas feitas não pode ser inferior a 1.')
        else:
            v_nops = True
    except:
        print('Digite um número inteiro.')

if t_med == 's':
  nota()


elif t_med == 'p':
    peso()
    nota()


else:
    print('Reveja sua escolhar')

print(med_s(notas, np))
print(med_p(notas,pesos))


# #-----------------------------------------------------------------------------------------------------------
# def media_p(ps1,ps2,p1,p2):
#     media_ponderada = ((ps1*p1)+(ps2*p2))/(ps1+ps2)
#     return(media_ponderada)
# def media()
# #------------------------------------------------------------------------------------------------------------
# print('Sua média ponderada é de ',media_p(peso1,peso2,prova1,prova2))
#
# print('Aperte enter para sair')
