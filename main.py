import pymysql
entrada = 0

def mostrar_tudo():
    conexao = pymysql.connect(
        host='den1.mysql4.gear.host',
        user='integredb1',
        password='Ao89Qen9i!A?',
        database='integredb1',
    )

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM estoque")

    resultado = cursor.fetchall()

    for produto in resultado:
        print(produto)


def encontrar_produto():
    conexao = pymysql.connect(
        host='den1.mysql4.gear.host',
        user='integredb1',
        password='Ao89Qen9i!A?',
        database='integredb1',
    )

    cursor = conexao.cursor()

    id = input('id do produto: ')

    try:
        cursor.execute("SELECT * FROM estoque WHERE Id =" + "'" + id + "'")

        resultado = cursor.fetchall()

        print(' Id: ' + str(resultado[0][0]) + '\n' + ' Nome do produto: ' + str(
            resultado[0][1]) + '\n' + ' Preço R$' + str(resultado[0][2]) + '\n'
              + ' Quantidade em estoque: ' + str(resultado[0][3]) + '\n' + ' Quantidade mínima: ' + str(
            resultado[0][4]))
    except:
        print('ID não encontrado no sistema')



def retirar_produto():
    conexao = pymysql.connect(
        host='den1.mysql4.gear.host',
        user='integredb1',
        password='Ao89Qen9i!A?',
        database='integredb1',
    )

    cursor = conexao.cursor()

    id = input('id do produto: ')

    try:
        cursor.execute("SELECT * FROM estoque WHERE Id =" + "'"+ id +"'")

        resultado = cursor.fetchall()

        print(' Id: ' + str(resultado[0][0]) + '\n' + ' Nome do produto: ' + str(
            resultado[0][1]) + '\n' + ' Preço R$' + str(resultado[0][2]) + '\n'
              + ' Quantidade em estoque: ' + str(resultado[0][3]) + '\n' + ' Quantidade mínima: ' + str(
            resultado[0][4]))
    except:
        print('ID não encontrado no sistema')



    cursor.execute("DELETE FROM estoque WHERE Id =" + "'" + id + "'")

    conexao.commit()

    print('---- PRODUTO REMOVIDO COM SUCESSO ----')



def cadastrar_produto():
    conexao = pymysql.connect(
        host='den1.mysql4.gear.host',
        user='integredb1',
        password='Ao89Qen9i!A?',
        database='integredb1',
    )

    cursor = conexao.cursor()

    com_sql = 'INSERT INTO estoque(Produto,Valor,Quantidade,QuantidadeMinima) VALUES (%s,%s,%s,%s)'

    var = (name, valor, quant,quant_min )
    cursor.execute(com_sql, var)

    conexao.commit()



while(entrada != 3):

    entrada = int(input('\nSISTEMA DE ESTOQUE\n OPÇÕES:\n 1 - adicionar produto no estoque\n '
                        '2 - retirar produto do estqoue\n 3 - fechar sistema\n'
                        ' 4 - encontrar produto \n 5 - mostrar todos os produtos do sistema \n'
                        'Insira um valor para operação:'))

    if(entrada == 1):
        name = input('Nome do Produto: ')
        valor = input('Valor do Produto: ')
        quant = input('Quantidade do Produto: ')
        quant_min = input('Quantidade Mínima do Produto: ')
        cadastrar_produto()

    if(entrada == 2):
        retirar_produto()

    if (entrada == 4):
        encontrar_produto()

    if (entrada == 5):
        mostrar_tudo()





