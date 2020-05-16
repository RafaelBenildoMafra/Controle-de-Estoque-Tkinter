import pymysql.cursors
from tkinter import *
from tkinter import messagebox

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
        listbox.insert(END,' Quantidade em estoque: ' + str( resultado[i][3]))
        listbox.insert(END,' Quantidade mínima: ' + str( resultado[i][4]))
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
    conexao = pymysql.connect(
        host='den1.mysql4.gear.host',
        user='integredb1',
        password='Ao89Qen9i!A?',
        database='integredb1',
    )

    cursor = conexao.cursor()
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
root.geometry('450x400')
root.title('Sistema de Controle de Estoque')
root.resizable(0, 0)

root.configure(bg = '#FFFFF0')

# CREATE TEXT BOXES
name = Entry(root, width=30, font = "Verdana 8", borderwidth = 1)
name.grid(row=0, column=1, padx=20, pady=(10,0))

valor = Entry(root, width=30, font = "Verdana 8", borderwidth = 1)
valor.grid(row=1, column=1, padx=20)

quant = Entry(root, width=30, font = "Verdana 8", borderwidth = 1)
quant.grid(row=2, column=1, padx=20)

quant_min = Entry(root, width=30, font = "Verdana 8", borderwidth = 1)
quant_min.grid(row=3, column=1, padx=20)

id = Entry(root, width=15, font = "Verdana 8 bold", borderwidth = 1)
id.grid(row=8, column=1, padx=0)

# CREATE TEXT BOX LABELS
nome_label = Label(root, text='Nome do Produto ', bg = '#FFFFF0', font = "Verdana 9 ", fg = 'black')
nome_label.grid(row=0, column=0, pady=(10,0))

valor_label = Label(root, text='Valor ', bg = '#FFFFF0', font = "Verdana 9 ", fg = 'black')
valor_label.grid(row=1, column=0)

quant_label = Label(root, text='Quantidade ', bg = '#FFFFF0', font = "Verdana 9 ", fg = 'black')
quant_label.grid(row=2, column=0)

quant_min_label = Label(root, text='Quantidade Minima ', bg = '#FFFFF0', font = "Verdana 9 ", fg = 'black')
quant_min_label.grid(row=3, column=0)


add_button = Button(root, text="Adicionar Produto Ao Estoque", command = cadastrar_produto, font = "Verdana 8 bold", fg = 'black', bg = '#F5F5F5')
add_button.grid(row=6, column=0, columnspan=2, pady=20, padx=10, ipadx=25, ipady = 3)

show_button = Button(root, text="Mostrar Produto", command = mostrar_produto, font = "Verdana 8 bold", fg = 'black', bg = '#F5F5F5')
show_button.grid(row=9, column=0, pady=20, padx=10, ipadx=25, ipady = 3)

id_label = Label(root, text = 'Numero de I.D', bg = '#FFFFF0', font = "Verdana 10 ", fg = 'black')
id_label.grid(row=8, column = 0)

delete_button = Button(root, text="Retirar Produto", command = retirar_produto, font = "Verdana 8 bold", fg = 'black', bg = '#F5F5F5')
delete_button.grid(row=9, column=1, pady=20, padx=10, ipadx=30, ipady = 3)

delete_button = Button(root, text="Mostrar Estoque", command = mostrar_estoque, font = "Verdana 8 bold", fg = 'black', bg = '#F5F5F5')
delete_button.grid(row=11, column=0, pady=20, padx=15, ipadx=40, ipady = 3, columnspan = 2)


root.mainloop()
