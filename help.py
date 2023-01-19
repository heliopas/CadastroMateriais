import tkinter as tk
import tkinter.scrolledtext as stTxt
import loadParameters

def drawHelp():
    loadParameters.loadConfigFile()
    root = tk.Tk()
    root.wm_attributes("-topmost", True)
    root.title('Menu')

    tk.Label(root,
             text='(M)e(n)u',
             font= ("Times New Roman", 15)).grid(column=0, row=0)

    textArea = stTxt.ScrolledText(root, width= 100, height=25,
                                  font= ("Times New Roman", 15))

    textArea.grid(column=0, padx=10, pady=10)

    textArea.insert(tk.INSERT, loadParameters.loadHelptFile())

    textArea.configure(state='disabled')
    root.mainloop()