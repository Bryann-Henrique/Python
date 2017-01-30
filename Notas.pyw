from tkinter import *
from tkinter import filedialog
import webbrowser

class app:
    def __init__(self, inst):
        self.jan = inst

        self.tela()

    def tela(self):
        self.jan.geometry('700x450')
        self.jan.title('Editor de texto')

        #Vinculos
        self.jan.bind('<Control-o>', self.abrir)
        self.jan.bind('<Control-s>', self.salvar)
        self.jan.bind('<F1>', self.popup)

        #Menu superior
        self.menu = Menu(self.jan)
        self.jan.config(menu = self.menu)

        self.arquivo = Menu(self.menu, tearoff = 0)
        self.arquivo.add_command(label = 'Abrir', command = self.abrir)
        self.arquivo.add_command(label = 'Salvar', command = self.salvar)
        self.arquivo.add_separator()
        self.arquivo.add_command(label = 'Sair', command = self.jan.destroy)

        self.editar = Menu(self.menu, tearoff = 0)
        self.editar.add_command(label = 'Localizar')
        self.editar.add_command(label = 'Substituir')
        self.editar.add_separator()
        self.editar.add_command(label = 'Maiuscula')
        self.editar.add_command(label = 'Minuscula')

        self.sobre = Menu(self.menu, tearoff = 0)
        self.sobre.add_command(label = 'Sobre', command = self.popup)
        self.sobre.add_command(label = 'Site', command = self.site)
        
        self.menu.add_cascade(label = 'Arquivo', menu = self.arquivo)
        self.menu.add_cascade(label = 'Editar', menu = self.editar)
        self.menu.add_cascade(label = 'Sobre', menu = self.sobre)

        #Caixa de texto
        self.caixa = Text(self.jan)
        self.caixa.pack(expand = True, fill=BOTH)

    def abrir(self, event = None):
        try:
            self.arqNome = filedialog.askopenfilename(filetypes=[('Arquivos de Texto', '.txt')])
            self.caixa.delete(1.0, END)
            self.arqTexto = open(self.arqNome ,'r')
            self.caixa.insert(END, self.arqTexto.read())
            self.arqTexto.close()
        except:
            pass

    def salvar(self, event = None):
        try: self.arqNome
        except: self.arqNome = False
        
        if self.arqNome:
            self.salvarTexto = self.caixa.get(1.0, END)

            with open(self.arqNome, 'w') as arq:
                arq.write(self.salvarTexto)

    def popup(self, event = None):
        self.p = Tk()
        self.p.geometry("200x90")
        self.p.title('Sobre')
        self.p.wm_resizable(width=False, height=False)

        self.dados = 'Dev\tBryann Henrique\nVersão\t1.0\nData\t30/01/2017'
        self.info = Label(self.p, text=self.dados, font=20, justify=LEFT)
        self.info.pack(side=LEFT)

        self.p.mainloop()

    def site(self):
        webbrowser.open('www.facebook.com/bryann.henrique')

i = Tk()
app(i)
i.mainloop()


































