import tkinter as tk
import datetime
from tkinter import ttk
import random

from files import globalVar
import bdFunctions
import messagePipe


def inserirBD(desc, ns, qtda, price, prodType):
    def __init__(desc: str | None = ...,  ns: str = ..., qtda: str | None = ..., price: str | None = ...,
                 prodType: str | None = ...) -> None: ...

    val = [('Medidor E223', '4N234514', '5', '17.895', '27/12/2025 - 12:45 AM', 'Cabo', '3', '2', '1', '3', '2', '1',
            '2231422')]

    data = datetime.datetime.utcnow().strftime('%c')
    ID = datetime.datetime.utcnow().strftime('%Y') + datetime.datetime.utcnow().strftime('%d') + str(random.randint(1, 1000))

    dataVector = [( str(desc), str(ns), str(qtda), str(price), str(data), str(prodType), str('-'), str('-'),
                    str('0'), str('0'), str('0'), str('0') , str(ID))]

    if (desc or ns) != '':
        bdFunctions.dbInsert(dataVector)
    else:
        messagePipe.messageError('Falta parametros -> Descrição ou NS!!!')

def ConsultarBD(ns, prodType):
    def __init__(ns: str | None = ...,  prodType: str | None = ...) -> None: ...

    if (ns or prodType) == '':
        # montar função para trazer todos os dados cadastrados
        messagePipe.messageError('Insira um valor!')
    else:
        bdFunctions.dbGetData(str(ns), str(prodType))

def sair(root):
    root.destroy()

def buscar():
    root = tk.Tk()
    root.wm_attributes("-topmost", True)
    root.title('Busca de Material')

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = screen_width - 1030
    window_height = screen_height - 750

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    midFrame = tk.Frame(root)
    midFrame.grid(column=1, row=3, sticky='new')
    midFrame.grid_columnconfigure(0, weight=3, uniform='middle')

    # numero de série
    nsLbl = tk.Label(root, text="Numero de série:", font="Raleway 12", anchor='w')
    nsLbl.grid(column=0, row=0)
    ns = tk.Entry(root, font='Raleway', width=25)
    ns.grid(column=1, row=0)

    # comboBox seleção de tipo de material
    tipoProdutoLbl = tk.Label(root, text="Tipo produto:", font="Raleway 12")
    tipoProdutoLbl.grid(column=0, row=2)
    tipoProduto = ttk.Combobox(root, font='Raleway 12', width=27)
    tipoProduto['values'] = globalVar.tipoProduto
    tipoProduto['state'] = 'readonly'
    tipoProduto.grid(column=1, row=2, sticky='w')

    # Consultar
    ConsultarbtnTXT = tk.StringVar()
    Consultarbtn = tk.Button(midFrame, textvariable=ConsultarbtnTXT, command=lambda:ConsultarBD(ns.get(), tipoProduto.get()),font="Raleway 14", background="#8b9484", foreground="White", height=1, width=15, text='Consultar')
    Consultarbtn.grid(column=0, row=3, sticky='new')

    # Sair
    sairbtnTXT = tk.StringVar()
    sairbtn = tk.Button(midFrame, textvariable=sairbtnTXT, command=lambda:sair(root),font="Raleway 14", background="#8b9484", foreground="White", height=1, width=15, text='Sair')
    sairbtn.grid(column=1, row=3, sticky='new')

    root.mainloop

def cadastro():
    root = tk.Tk()
    root.wm_attributes("-topmost", True)
    root.title('Cadastro de materiais')

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = screen_width - 750
    window_height = screen_height - 500

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    midFrame = tk.Frame(root)
    midFrame.grid(column=1, row=9, sticky='new')
    midFrame.grid_columnconfigure(0, weight=3, uniform='middle')

    #cadastra nome produto
    produtoLbl = tk.Label(root, text="Descrição produto:", font="Raleway 12", anchor='w')
    produtoLbl.grid(column=0, row=1)
    produto = tk.Entry(root, font='Raleway', width=50)
    produto.grid(column=1, row=1)
    # cadastra numero de série
    nsLbl = tk.Label(root, text="Numero de série:", font="Raleway 12", anchor='w')
    nsLbl.grid(column=0, row=2)
    ns = tk.Entry(root, font='Raleway', width=50)
    ns.grid(column=1, row=2)
    #cadastra quantidade
    qtdaLbl = tk.Label(root, text="Quantidade:", font="Raleway 12", anchor='w')
    qtdaLbl.grid(column=0, row=3)
    qtda = tk.Entry(root, font='Raleway', width=50)
    qtda.grid(column=1, row=3)
    # cadastra valor produto
    valorLbl = tk.Label(root, text="Valor:", font="Raleway 12", anchor='w')
    valorLbl.grid(column=0, row=4)
    valor = tk.Entry(root, font='Raleway', width=50)
    valor.grid(column=1, row=4)
    # cadastra data hora atual
    data = datetime.datetime.utcnow().strftime('%c')
    dateHrLbl = tk.Label(root, text="Data / hora:", font="Raleway 12", anchor='w')
    dateHrLbl.grid(column=0, row=5)
    dateHr = tk.Entry(root, font='Raleway', width=50)
    dateHr.insert(0,string=data)
    dateHr.grid(column=1, row=5)
    # comboBox seleção de tipo de material
    tipoProdutoLbl = tk.Label(root, text="Tipo produto:", font="Raleway 12")
    tipoProdutoLbl.grid(column=0, row=6)
    tipoProduto = ttk.Combobox(root, font='Raleway 12')
    tipoProduto['values'] = globalVar.tipoProduto
    tipoProduto['state'] = 'readonly'
    tipoProduto.grid(column=1, row=6, sticky='w')

    # Inserir material
    inserirbtnTXT = tk.StringVar()
    inserirbtn = tk.Button(midFrame, textvariable=inserirbtnTXT, command=lambda:inserirBD(produto.get(), ns.get(), qtda.get(), valor.get(),tipoProduto.get()),font="Raleway 14", background="#8b9484", foreground="White", height=1, width=15, text='Inserir')
    inserirbtn.grid(column=0, row=7, sticky='new')

    # Consultar
    ConsultarbtnTXT = tk.StringVar()
    Consultarbtn = tk.Button(midFrame, textvariable=ConsultarbtnTXT, command=lambda:ConsultarBD(),font="Raleway 14", background="#8b9484", foreground="White", height=1, width=15, text='Consultar')
    Consultarbtn.grid(column=1, row=7, sticky='new')

    # Sair
    sairbtnTXT = tk.StringVar()
    sairbtn = tk.Button(midFrame, textvariable=sairbtnTXT, command=lambda:sair(root),font="Raleway 14", background="#8b9484", foreground="White", height=1, width=15, text='Sair')
    sairbtn.grid(column=2, row=7, sticky='new')

    root.mainloop