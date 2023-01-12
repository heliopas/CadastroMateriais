import tkinter as tk
import cadastroSkinApp
import datetime

from PIL import Image, ImageTk

def deletar():
    return 1

def alterar():
    return 1

def helpmenu():
    return 1

def emprestimo():
    return 1

def exitsw(root):
    root.destroy()


def drawApp():
    root = tk.Tk()
    root.wm_attributes("-topmost", True)
    root.title('WareHouse HQA V:1.00')

    window_width = 310
    window_height = 500

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # set windows size
    global draWindow
    draWindow = tk.Canvas(root)
    draWindow.grid(columnspan=1, rowspan=1)

    # set backgroung logo
    logo = Image.open('files/logo/landisLogo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, columnspan=2, row=1, rowspan=5, padx=0, pady=0)

    # software instructions
    instructions = tk.Label(draWindow, text="HQA WAREHOUSE CONTROL", font="Raleway")
    instructions.grid(columnspan=1, row=10, column=0, padx=10, pady=10)

    # Button cadastro material
    cadastrobtnTXT = tk.StringVar()
    cadastrobtn = tk.Button(draWindow, textvariable=cadastrobtnTXT, command=lambda: cadastroSkinApp.cadastro(), font="Raleway",
                         background="#8b9484", foreground="White", height=1, width=20)
    cadastrobtnTXT.set("Cadastro de material")
    cadastrobtn.grid(column=0, row=0)

    # Button buscar material
    buscarbtnTXT = tk.StringVar()
    buscarbtn = tk.Button(draWindow, textvariable=buscarbtnTXT, command=lambda: cadastroSkinApp.buscar(), font="Raleway",
                        background="#8b9484", foreground="White", height=1, width=20)
    buscarbtnTXT.set("Buscar material")
    buscarbtn.grid(column=0, row=1)

    # Button deletar material
    deletarbtnTXT = tk.StringVar()
    deletarbtn = tk.Button(draWindow, textvariable=deletarbtnTXT, command=lambda: deletar(), font="Raleway",
                           background="#8b9484", foreground="White", height=1, width=20)
    deletarbtnTXT.set("Deletar material")
    deletarbtn.grid(column=0, row=2)

    # Button alterar material
    alterarbtnTXT = tk.StringVar()
    alterarbtn = tk.Button(draWindow, textvariable=alterarbtnTXT, command=lambda: alterar(), font="Raleway",
                        background="#8b9484", foreground="White", height=1, width=20)
    alterarbtnTXT.set("Alterar material")
    alterarbtn.grid(column=0, row=3)

    # Button help
    helpbtnTXT = tk.StringVar()
    helpbtn = tk.Button(draWindow, textvariable=helpbtnTXT, command=lambda: helpmenu(), font="Raleway",
                         background="#8b9484", foreground="White", height=1, width=20)
    helpbtnTXT.set("Help")
    helpbtn.grid(column=0, row=4)

    # Button Emprestimos
    emprestimobtnTXT = tk.StringVar()
    emprestimobtn = tk.Button(draWindow, textvariable=emprestimobtnTXT, command=lambda: emprestimo(), font="Raleway",
                         background="#8b9484", foreground="White", height=1, width=20)
    emprestimobtnTXT.set("Emprestimos")
    emprestimobtn.grid(column=0, row=6)

    # Button Close
    closebtnTXT = tk.StringVar()
    closebtn = tk.Button(draWindow, textvariable=closebtnTXT, command=lambda: exitsw(root), font="Raleway",
                         background="#8b9484", foreground="White", height=1, width=20)
    closebtnTXT.set("Close App")
    closebtn.grid(column=0, row=6)

    root.mainloop()