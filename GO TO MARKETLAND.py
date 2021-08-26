import pymysql.cursors
from datetime import date

dataatual = date.today()

datadia = dataatual.day
datames = dataatual.month
dataano = dataatual.year

conexao = pymysql.connect(

    host='localhost',
    user='root',
    passwd='',
    db='gmhistorico',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor

)




def linhabranca():
    print('\033[1;30m-\033[m' * 40)


def linhavermelha():
    print('\033[7;30m=\033[m' * 40)


carrinho = []
carrinhop = []
# Produtos
cup = 3.50
ket = 4.75
cremedeleite = 1.99

# ESTANTE DE PRODUTOS
print(' \033[1;33mPRODUTOS DISPONÍVEIS E SUAS INDENTIFICAÇÕES\033[m')
linhabranca()
print('\033[1;30mCUP NOODLES\033[m = \033[1;34mN1\033[m')
print()
print('\033[1;30mKETCHUP SABOR DA ARTE TRADICIONAL\033[m = \033[1:34mN2\033[m')
print()
print('\033[1;30mCREME DE LEITE\033[m = \033[1;34mN3\033[m')

linhabranca()

# NOME DOS PRODUTOS
n1 = 'CUP NOODLES'
n2 = 'KETCHUP SABOR DA ARTE TRADICIONAL'
n3 = 'CREME DE LEITE'

# CONTAGEM DOS PRODUTOS
cn = 0
kt = 0
cm = 0

# Perguntas de preferencias
op = int(input('\033[1;33mQUANTAS OPÇÕES DE QUANTIDADE VOCÊ VAI QUERER?\033[m '))
print()
carteira = float(input('\033[1;32mDECLARE SUA CARTEIRA R$:\033[m \n'))
print('\033[1;36m=\033[m' * 45)

# CABEÇA DO PROGRAMA
for i in range(0, op):
    a = str(input('\033[1;33mINSIRA O PRODUTO QUE VOCÊ QUER USANDO SOMENTE AS IDENTIFICAÇÕES:\033[m ')).upper()
    if a == 'N1':
        print()
        print('\033[1;33mVOCÊ ESCOLHEU O \033[1:30m{}\033[m\033[m'.format(n1))
        print()
        x = str(input('\033[1;32mCONFIRMAR O PRODUTO?\033[m ')).upper()
        if x == 'S':
            print('\033[1;33m{} ADICIONADO AO CARRINHO\033[m'.format(n1))
            cn += 1
            print()
            print(f'\033[1;37mVOCE ADICIONOU \033[1;30m{cn}\033[m \033[1;30m{n1}\033[m\033[m')
            linhabranca()
            carrinho.append(cup)
            carrinhop.append(n1)

    elif a == 'N2':
        print('\033[1;33mVOCÊ ESCOLHEU O \033[1;30m{}\033[m\033[m'.format(n2))
        print()
        s = str(input('\033[1;32mCONFIRMAR O PRODUTO?\033[m ')).upper()
        if s == 'S':
            print(f'\033[1;33m{n2} adicionado ao carrinho')
            kt += 1
            print()
            print(f'\033[1;37mVOCE ADICIONOU\033[m \033[1;30m{kt}\033[m \033[1;30m{n2}\033[m')
            linhabranca()
            carrinho.append(ket)
            carrinhop.append(n2)

    elif a == 'N3':
        print(f'\033[1;33mVOCÊ ESCOLHEU O \033[1;30m{n3}\033[m\033[m')
        print()
        cl = str(input('\033[1;32mCONFIRMAR O PRODUTO?\033[m ')).upper()
        if cl == 'S':
            print(f'\033[1;33m{n3} adicionado ao carrinho')
            cm += 1
            print()
            print(f'\033[1;37mVOCE ADICIONOU\033[m \033[1;30m{cm}\033[m \033[1;30m{n3}\033[m')
            linhabranca()
            carrinho.append(cremedeleite)
            carrinhop.append(n3)

    elif a == 'N':
        break

# SOMAS E FINALIZAÇOES DAS COMPRAS
print(carrinho)
soma = 0
for c in carrinho:
    soma += c

#HISTORICO
with conexao.cursor() as cursor:
    cursor.execute('insert into historico (dia, mes, ano, produtos, total) values("{}", "{}", "{}", "{}", "{}")'.format(datadia, datames, dataano, carrinhop, soma))
    conexao.commit()


print(f'\033[1;30mO VALOR DA SUA COMPRA DEU:\033[m \033[1;32m\n{soma:.2f}\033[m')
print()


if soma > carteira:
    f = soma - carteira
    print(
        f'\033[1;30MVOCE NÃO TEM DINHEIRO SUFICIENTE, AINDA FALTAM \033[1;32m{f:.2f}R$\033[m PARA EFETUAR ESSA COMPRA')
troco = carteira - soma
if troco <= 0:
    print('\033[1;32mNÃO SOBROU TROCO\033[m')
else:
    print(f'\033[1;30mSEU TROCO DEU: \033[1;32m\n{troco:.2f}\033[m')
print()
print('ATUALIZAÇÃO 1.0')

