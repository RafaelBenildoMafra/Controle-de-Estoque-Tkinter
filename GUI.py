import pymysql.cursors
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import sys


def analizar_estoque():
    anal = Tk()
    anal.iconbitmap('favicon.ico')
    anal.geometry('660x350')
    anal.title('Analizar Estoque')
    anal.configure(bg='#FFFFF0')

    conexao = pymysql.connect(
        host='den1.mysql4.gear.host',
        user='integredb1',
        password='Ao89Qen9i!A?',
        database='integredb1',
    )

    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM integredb1.estoque')

    resultado = cursor.fetchall()

    sum = 0
    list_quant = []
    list_produtos = []
    list_valores = []
    val = 0
    quan = 0

    for produto in resultado:
        list_produtos.append(produto[1])
        list_valores.append(float(produto[2].replace(',','.')))
        list_quant.append(float(produto[3]))

        sum += 1


    for x in list_valores:
        val = x + val

    media = val/len(list_valores)

    for x in list_valores:
        quan = x + quan




    frame_anal = LabelFrame(anal, padx=50, pady=20, bg='#FFFFF0', font="Verdana 20 ", fg='black', bd=3)
    frame_anal.grid(column=0, row=0, padx=100, pady=30)

    valor_label = Label(frame_anal, text='Valor Total: R$' + str(val), bg='#FFFFF0', font="Verdana 15 ", fg='black')
    valor_label.grid(row=1, column=0)

    valor_medio__label = Label(frame_anal, text='Valor Médio: R$' + str(round(media,2)), bg='#FFFFF0', font="Verdana 15 ", fg='black')
    valor_medio__label.grid(row=2, column=0)

    quant_label = Label(frame_anal, text='Quantidade Total: ' + str(quan), bg='#FFFFF0', font="Verdana 15 ", fg='black')
    quant_label.grid(row=0, column=0)

    quant_min_label = Label(frame_anal, text='Tipos de Produto: ' + str(sum), bg='#FFFFF0', font="Verdana 15 ", fg='black')
    quant_min_label.grid(row=3, column=0)

    quant_min_label = Label(anal, text='Para uma analize mais detalhada acessar a planilha no Power BI', bg='#FFFFF0', font="Verdana 15 ",fg='black')
    quant_min_label.grid(row=2, column=0)



    plt.figure(figsize=(20,15), dpi=80)
    plt.hlines(y=list_produtos[:50], xmin=0, xmax= list_quant, alpha=0.4, linewidth=3,color = 'orange')
    plt.grid(linestyle='--', alpha=0.5)
    plt.gca().set(ylabel='$Produto$', xlabel='$Qauntidade$')
    plt.yticks(list_produtos[:50], fontsize=12)
    plt.grid(linestyle='--', alpha=0.5)
    for x, y, tex in zip(list_quant, list_produtos[:50], list_quant):
        t = plt.text(x, y, round(tex, 2), horizontalalignment='right' if x < 0 else 'left',
                     verticalalignment='center', fontdict={'color': 'red' if x < 0 else 'green', 'size': 14})
    plt.title('Quantidade por Produto(Primeiros 50)', fontdict={'size': 20})
    plt.show()


def sair():
    sys.exit()

def editar_produto(id):
    global edit

    edit = Tk()
    edit.iconbitmap('favicon.ico')
    edit.geometry('700x300')
    edit.title('Editar Produto')
    edit.configure(bg='#FFFFF0')

    frame3 = LabelFrame(edit, padx=50, pady=20, bg='#FFFFF0', font="Verdana 9 ", fg='black', bd=3)
    frame3.grid(column=1, row=0, padx=100, pady=30)

    conexao = pymysql.connect(
        host='den1.mysql4.gear.host',
        user='integredb1',
        password='Ao89Qen9i!A?',
        database='integredb1',
    )

    cursor = conexao.cursor()

    ident = str(id)
    try:
        cursor.execute("SELECT * FROM estoque WHERE Id =" + "'" + ident + "'")
        resultado = cursor.fetchall()

        nome_label = Label(frame3, text='Nome do Produto ', bg='#FFFFF0', font="Verdana 9 ", fg='black')
        nome_label.grid(row=1, column=0, pady=(10, 0))

        valor_label = Label(frame3, text='Valor ', bg='#FFFFF0', font="Verdana 9 ", fg='black')
        valor_label.grid(row=2, column=0)

        quant_label = Label(frame3, text='Quantidade ', bg='#FFFFF0', font="Verdana 9 ", fg='black')
        quant_label.grid(row=3, column=0)

        quant_min_label = Label(frame3, text='Quantidade Minima ', bg='#FFFFF0', font="Verdana 9 ", fg='black')
        quant_min_label.grid(row=4, column=0)

        id_label = Label(frame3, text='Número de I.D:', bg='#FFFFF0', font="Verdana 9 ", fg='black')
        id_label.grid(row=0, column=0, columnspan=2)

        label_id = Label(frame3, text=str(resultado[0][0]), bg='#FFFFF0', font="Verdana 9 bold", fg='black')
        label_id.grid(row=0, column=1)

        name_edit = Entry(frame3, width=30, font="Verdana 8", borderwidth=1)
        name_edit.grid(row=1, column=1, padx=20, pady=(10, 0))

        valor_edit = Entry(frame3, width=30, font="Verdana 8", borderwidth=1)
        valor_edit.grid(row=2, column=1, padx=20)

        quant_edit = Entry(frame3, width=30, font="Verdana 8", borderwidth=1)
        quant_edit.grid(row=3, column=1, padx=20)

        quant_min_edit = Entry(frame3, width=30, font="Verdana 8", borderwidth=1)
        quant_min_edit.grid(row=4, column=1, padx=20)

        name_edit.insert(0, resultado[0][1])
        quant_edit.insert(0, resultado[0][3])
        quant_min_edit.insert(0, resultado[0][4])
        valor_edit.insert(0, resultado[0][2])

        confirm_button = Button(frame3, text="Confirmar", command=lambda: salvar(ident, name_edit.get(), quant_edit.get(), valor_edit.get(), quant_min_edit.get() ), font="Verdana 8 bold",fg='black', bg='#F5F5F5')
        confirm_button.grid(row=12, column=1, pady=20, padx=15, ipadx=40, ipady=3)

    except:
        edit.destroy()
        response = messagebox.showerror('Sistema de Controle de Estoque', 'Id não encontrado!')
        labelmsg = Label(edit, text=response)
        labelmsg.grid(row=0, column=0)




def salvar(ident, name_edit,valor_edit, quant_edit, quant_min_edit ):
    conexao = pymysql.connect(
        host='den1.mysql4.gear.host',
        user='integredb1',
        password='Ao89Qen9i!A?',
        database='integredb1',
    )

    print(name_edit)
    print(valor_edit)
    print(quant_edit)
    print(quant_min_edit)
    print(ident)
    cursor = conexao.cursor()

    cursor.execute("UPDATE estoque SET Produto =" + "'" + name_edit + "'" + ",Valor =" + "'" +  valor_edit + "'" + ", Quantidade =" + "'" + quant_edit + "'" + ", QuantidadeMinima=" + "'" + quant_min_edit + "'" + "Where id =" + "'" + ident + "'")

    conexao.commit()
    edit.destroy()


def mostrar_estoque():
    show = Tk()
    show.iconbitmap('favicon.ico')
    show.geometry('800x500')
    show.title(' Estoque')

    conexao = pymysql.connect(
        host='den1.mysql4.gear.host',
        user='integredb1',
        password='Ao89Qen9i!A?',
        database='integredb1',
    )

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM estoque")

    resultado = cursor.fetchall()

    scroll = Scrollbar(show)
    scroll.pack(side=RIGHT, fill=Y)

    listbox = Listbox(show, yscrollcommand = scroll.set)
    i = 0

    listbox.configure(bg = '#FFFFF0',font = "Verdana 8 bold", fg = 'black')

    while i < len(resultado):
        listbox.insert(END , '')
        listbox.insert(END,'          Id: ' + str(resultado[i][0]))
        listbox.insert(END, '------------------------------------------------')
        listbox.insert(END,' Nome do produto: ' + str(resultado[i][1]))
        listbox.insert(END,' Preço R$' + str(resultado[i][2]))
        listbox.insert(END,' Quantidade em estoque: ' + str(resultado[i][3]))
        listbox.insert(END,' Quantidade mínima: ' + str(resultado[i][4]))
        listbox.insert(END, '------------------------------------------------')
        listbox.pack(fill=BOTH, expand=1)
        scroll.config(command=listbox.yview())

        i += 1

def mostrar_produto():
    conexao = pymysql.connect(
        host='den1.mysql4.gear.host',
        user='integredb1',
        password='Ao89Qen9i!A?',
        database='integredb1',
    )

    cursor = conexao.cursor()

    ident = id.get()
    ident = str(ident)

    try:
        cursor.execute("SELECT * FROM estoque WHERE Id =" + "'" + ident + "'")
        resultado = cursor.fetchall()

        view = Tk()
        view.geometry('250x150')
        view.configure(bg='#FFFFF0')
        view.iconbitmap('favicon.ico')
        view.title('Dados do Produto')
        label = Label(view, text = ' \n Id: ' + str(resultado[0][0]) + '\n' + ' \n Nome do produto: ' + str(
            resultado[0][1]) + '\n' + ' \n Preço R$' + str(resultado[0][2]) + '\n'
              + ' \n Quantidade em estoque: ' + str(resultado[0][3]) + '\n' + ' \n Quantidade mínima: ' + str(
            resultado[0][4]), bg = '#FFFFF0', font = "Verdana 8 bold", fg = 'black')
        label.grid(row = 0, column = 0)
    except:
        view.destroy()
        response = messagebox.showerror('Sistema de Controle de Estoque', 'Id não encontrado!')
        labelmsg = Label(root, text=response)
        labelmsg.grid(row = 0, column = 0)


    id.delete(0, END)
    conexao.close()


def cadastrar_produto():
    if(name.get() == "" or valor.get() == "" or quant.get() == "" or quant_min.get() == "" ):
        response = messagebox.showerror('Sistema de Controle de Estoque', 'Preencha todos os Dados do Produto para inserir no Estoque')
        labelmsg2 = Label(root, text=response)
        labelmsg2.grid(row=0, column=0)

    else:
        conexao = pymysql.connect(
            host='den1.mysql4.gear.host',
            user='integredb1',
            password='Ao89Qen9i!A?',
            database='integredb1',
        )

        cursor = conexao.cursor()

        cursor.execute('SELECT Produto FROM integredb1.estoque')
        resultado = cursor.fetchall()

        prod = 0

        for produto in resultado:
            if (produto[0] == name.get()):
                prod += 1


        if (prod > 0):
            response = messagebox.showerror('Sistema de Controle de Estoque', 'Existe Um Produto Com Mesmo Nome No Estoque')
            labelmsg2 = Label(root, text=response)
            labelmsg2.grid(row=0, column=0)
        else:
            try:
                com_sql = 'INSERT INTO estoque(Produto,Valor,Quantidade,QuantidadeMinima) VALUES (%s,%s,%s,%s)'

                var = (name.get(), valor.get(), quant.get(), quant_min.get())
                cursor.execute(com_sql, var)

                conexao.commit()

                response = messagebox.showinfo('Sistema de Controle de Estoque', 'Produto Inserido com Sucesso!')
                labelmsg = Label(root, text=response)
                labelmsg.grid(row=0, column=0)
            except:
                response = messagebox.showerror('Sistema de Controle de Estoque', 'Não Foi Possivel Inserir o Produto')
                labelmsg1 = Label(root, text=response)
                labelmsg1.grid(row=0, column=0)

        if (prod > 1):
            response = messagebox.showerror('Sistema de Controle de Estoque', 'Foram encontrados ' + str(prod) + ' produtos com mesmo nome')
            labelmsg2 = Label(root, text=response)
            labelmsg2.grid(row=0, column=0)




        conexao.close()

        name.delete(0, END)
        valor.delete(0, END)
        quant.delete(0, END)
        quant_min.delete(0, END)

def retirar_produto():
    conexao = pymysql.connect(
        host='den1.mysql4.gear.host',
        user='integredb1',
        password='Ao89Qen9i!A?',
        database='integredb1',
    )

    cursor = conexao.cursor()
    ident = id.get()
    ident = str(ident)

    try:
        cursor.execute("SELECT * FROM estoque WHERE Id =" + "'" + ident + "'")

        resultado = cursor.fetchall()

        print(' Id: ' + str(resultado[0][0]) + '\n' + ' Nome do produto: ' + str(
            resultado[0][1]) + '\n' + ' Preço R$' + str(resultado[0][2]) + '\n'
              + ' Quantidade em estoque: ' + str(resultado[0][3]) + '\n' + ' Quantidade mínima: ' + str(
            resultado[0][4]))

        response = messagebox.showinfo('Sistema de Controle de Estoque', 'Produto Removido com Sucesso!')
        labelmsg = Label(root, text=response)
        labelmsg.grid(row=0, column=0)

    except:
        response = messagebox.showerror('Sistema de Controle de Estoque', 'Id não encontrado!')
        labelmsg1 = Label(root, text=response)
        labelmsg1.grid(row=0, column=0)

    cursor.execute("DELETE FROM estoque WHERE Id =" + "'" + ident + "'")

    conexao.commit()

    conexao.close()

    id.delete(0, END)


root = Tk()
root.iconbitmap('favicon.ico')
root.geometry('930x925')
root.title('Sistema de Controle de Estoque')
imagem = ImageTk.PhotoImage(file="logout.png")
root.resizable(0, 0)

root.configure(bg = '#FFFFF0')



conexao = pymysql.connect(
    host='den1.mysql4.gear.host',
    user='integredb1',
    password='Ao89Qen9i!A?',
    database='integredb1',
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM estoque")

resultado = cursor.fetchall()


frame1 = LabelFrame(root , padx = 10, pady = 20, bg = '#FFFFF0', font = "Verdana 9 ", fg = 'black', bd = 3)
frame1.grid(column = 0, row = 0, padx = 30, pady = 20)

frame2 = LabelFrame(root , padx = 10, pady = 20, bg = '#FFFFF0', font = "Verdana 9 ", fg = 'black', bd = 3)
frame2.grid(column = 1, row = 0, padx = 10, pady = 30, columnspan = 3)

frame3 = LabelFrame(root , padx = 10, pady = 5, bg = '#FFFFF0', font = "Verdana 9 ", fg = 'black', bd = 3)
frame3.grid(column = 0, row = 1, padx = 1, pady = 1)

frame4 = LabelFrame(root ,text = "SAIR", padx = 10, pady = 20, bg = '#FFFFF0', font = "Verdana 9 bold", fg = 'red', bd = 3)
frame4.grid(column = 0, row = 3, padx = 10, pady = 5)

frame5 = LabelFrame(root , text = 'COMPRAR', padx = 0, pady = 20, bg = '#FFFFF0', font = "Verdana 9 bold", fg = 'red', bd = 3)
frame5.grid(column = 1, row = 1, padx = 0, pady = 30)

frame6 = LabelFrame(root , text = 'PRÓXIMOS DE COMPRAR ', padx = 10, pady = 20, bg = '#FFFFF0', font = "Verdana 9 bold", fg = 'orange', bd = 3)
frame6.grid(column = 2, row = 1, padx = 10, pady = 30)

# CREATE TEXT BOXES
name = Entry(frame1, width=30, font = "Verdana 8", borderwidth = 1)
name.grid(row=0, column=1, padx=20, pady=(10,0))

valor = Entry(frame1, width=30, font = "Verdana 8", borderwidth = 1)
valor.grid(row=1, column=1, padx=20)

quant = Entry(frame1, width=30, font = "Verdana 8", borderwidth = 1)
quant.grid(row=2, column=1, padx=20)

quant_min = Entry(frame1, width=30, font = "Verdana 8", borderwidth = 1)
quant_min.grid(row=3, column=1, padx=20)

id = Entry(frame2, width=15, font = "Verdana 8 bold", borderwidth = 1)
id.grid(row=0, column=1, padx=0)

# CREATE TEXT BOX LABELS
nome_label = Label(frame1, text='Nome do Produto ', bg = '#FFFFF0', font = "Verdana 9 ", fg = 'black')
nome_label.grid(row=0, column=0, pady=(10,0))

valor_label = Label(frame1, text='Valor ', bg = '#FFFFF0', font = "Verdana 9 ", fg = 'black')
valor_label.grid(row=1, column=0)

quant_label = Label(frame1, text='Quantidade ', bg = '#FFFFF0', font = "Verdana 9 ", fg = 'black')
quant_label.grid(row=2, column=0)

quant_min_label = Label(frame1, text='Quantidade Minima ', bg = '#FFFFF0', font = "Verdana 9 ", fg = 'black')
quant_min_label.grid(row=3, column=0)


add_button = Button(frame1, text="Inserir Novo Produto", command = cadastrar_produto, font = "Verdana 8 bold", fg = 'black', bg = '#F5F5F5')
add_button.grid(row=6, column=0, columnspan=2, pady=20, padx=10, ipadx=25, ipady = 3)

show_button = Button(frame2, text="Mostrar Produto", command = mostrar_produto, font = "Verdana 8 bold", fg = 'black', bg = '#F5F5F5')
show_button.grid(row=9, column=0, pady=20, padx=10, ipadx=25, ipady = 3, columnspan= 2)

id_label = Label(frame2, text = 'Numero de I.D', bg = '#FFFFF0', font = "Verdana 10 ", fg = 'black')
id_label.grid(row=0, column = 0)




i = 0
for estoque in resultado:
    if(int(estoque[3]) - int(estoque[4]) < 0.1 * int(estoque[3])):
        list_label = Label(frame5, text= str(estoque[1]), bg='#FFFFF0', font="Verdana 10 ", fg='red')
        list_label.grid(row = i, column = 0)
        i+=1

i = 0
for estoque in resultado:
    if(int(estoque[3]) - int(estoque[4]) < 0.3 * int(estoque[3]) and int(estoque[3]) - int(estoque[4]) > 0.1 * int(estoque[3])):
        list_label = Label(frame6, text= str(estoque[1]), bg='#FFFFF0', font="Verdana 10 ", fg='orange')
        list_label.grid(row = i, column = 0)
        i+=1


delete_button = Button(frame2, text="Retirar Produto", command = retirar_produto, font = "Verdana 8 bold", fg = 'black', bg = '#F5F5F5')
delete_button.grid(row=1, column=1, pady=20, padx=10, ipadx=30, ipady = 3)

mostrar_button = Button(frame3, text="Mostrar Estoque", command = mostrar_estoque, font = "Verdana 8 bold", fg = 'black', bg = '#F5F5F5')
mostrar_button.grid(row=2, column=0, pady=15, padx=15, ipadx=25, ipady = 3)

edit_button = Button(frame2, text="Editar Produto", command = lambda : editar_produto(id.get()), font = "Verdana 8 bold", fg = 'black', bg = '#F5F5F5')
edit_button.grid(row=1, column=0, pady=15, padx=15, ipadx=34, ipady = 3)

sair_button = Button(frame4, text="Sair", command = sair, font = "Verdana 8 bold", fg = 'black', bg = '#F5F5F5', image = imagem)
sair_button.grid(row=0, column=0, pady=5, padx=15, ipadx=40, ipady = 3)

anal_button = Button(frame3, text="Analizar Estoque", command = analizar_estoque, font = "Verdana 8 bold", fg = 'black', bg = '#F5F5F5')
anal_button.grid(row=1, column=0, pady=20, padx=15, ipadx=40, ipady = 3)



root.mainloop()
