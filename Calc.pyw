from tkinter import *
import webbrowser

class app:
    def __init__(self, inst):
        self.janela = inst

        self.tela()

    def tela(self):
        self.validade = 0
        self.calc = False

        #Janela
        self.janela.geometry("250x280")
        self.janela.title("Calculadora")
        self.janela.wm_iconbitmap(None)
        self.janela.wm_resizable(width=False, height=False)

        #Menubar
        menuBar = Menu(self.janela)
        self.janela.config(menu=menuBar)

        editar = Menu(menuBar, tearoff = 0)
        editar.add_command(label='Limpar', command=self.limpa)
        editar.add_separator()
        editar.add_command(label='Sair', command=self.sair)
        
        site = Menu(menuBar, tearoff = 0)
        site.add_command(label='Sobre', command=self.popup)

        menuBar.add_cascade(label='Editar', menu=editar)
        menuBar.add_cascade(label='Ajuda', menu=site)

        #Frames
        frame1 = Frame(self.janela); frame1.pack()
        frame2 = Frame(self.janela); frame2.pack()
        frame3 = Frame(self.janela); frame3.pack()
        frame4 = Frame(self.janela); frame4.pack()
        frame5 = Frame(self.janela); frame5.pack()

        #Texto
        self.texto = Label(frame1, text='0', font=('Consolas', 24), width = 12)
        self.texto.pack(pady = 20)
        
        #Botões
        bt01 = Button(frame2, text = "+", width=4, font=('Consolas', 14), command = self.funcAdi).pack(pady=4, padx=4, side = LEFT)
        bt02 = Button(frame2, text = "-", width=4, font=('Consolas', 14), command = self.funcSub).pack(pady=4, padx=4, side = LEFT)
        bt03 = Button(frame2, text = "*", width=4, font=('Consolas', 14), command = self.funcMul).pack(pady=4, padx=4, side = LEFT)
        bt04 = Button(frame2, text = "/", width=4, font=('Consolas', 14), command = self.funcDiv).pack(pady=4, padx=4, side = LEFT)
        bt05 = Button(frame3, text = "1", width=4, font=('Consolas', 14), command = self.funcUm_).pack(pady=4, padx=4, side = LEFT)
        bt06 = Button(frame3, text = "2", width=4, font=('Consolas', 14), command = self.funcDoi).pack(pady=4, padx=4, side = LEFT)
        bt07 = Button(frame3, text = "3", width=4, font=('Consolas', 14), command = self.funcTre).pack(pady=4, padx=4, side = LEFT)
        bt08 = Button(frame3, text = "4", width=4, font=('Consolas', 14), command = self.funcQua).pack(pady=4, padx=4, side = LEFT)
        bt09 = Button(frame4, text = "5", width=4, font=('Consolas', 14), command = self.funcCin).pack(pady=4, padx=4, side = LEFT)
        bt10 = Button(frame4, text = "6", width=4, font=('Consolas', 14), command = self.funcSex).pack(pady=4, padx=4, side = LEFT)
        bt11 = Button(frame4, text = "7", width=4, font=('Consolas', 14), command = self.funcSet).pack(pady=4, padx=4, side = LEFT)
        bt14 = Button(frame4, text = "8", width=4, font=('Consolas', 14), command = self.funcOit).pack(pady=4, padx=4, side = LEFT)
        bt13 = Button(frame5, text = "9", width=4, font=('Consolas', 14), command = self.funcNov).pack(pady=4, padx=4, side = LEFT)
        bt14 = Button(frame5, text = "0", width=4, font=('Consolas', 14), command = self.funcZer).pack(pady=4, padx=4, side = LEFT)
        bt15 = Button(frame5, text = "=", width=10, font=('Consolas', 14), command = self.funcCalc).pack(pady=4, padx=4, side = LEFT)

    def funcAdi(self): self.valida(); self.texto['text'] += '+'
    def funcSub(self): self.valida(); self.texto['text'] += '-'
    def funcMul(self): self.valida(); self.texto['text'] += '*'
    def funcDiv(self): self.valida(); self.texto['text'] += '/'
    def funcUm_(self): self.valida(); self.texto['text'] += '1'
    def funcDoi(self): self.valida(); self.texto['text'] += '2'
    def funcTre(self): self.valida(); self.texto['text'] += '3'
    def funcQua(self): self.valida(); self.texto['text'] += '4'
    def funcCin(self): self.valida(); self.texto['text'] += '5'
    def funcSex(self): self.valida(); self.texto['text'] += '6'
    def funcSet(self): self.valida(); self.texto['text'] += '7'
    def funcOit(self): self.valida(); self.texto['text'] += '8'
    def funcNov(self): self.valida(); self.texto['text'] += '9'
    def funcZer(self): self.valida(); self.texto['text'] += '0'

    def funcCalc(self):
        try:
            self.texto['text'] = int(eval(self.texto['text']))
        except:
            self.texto['text'] = 'op invalida'
        finally:
            self.calc = True

    def limpa(self):
        self.texto['text'] = '0'
        self.validade = 0

    def valida(self):
        #Retira o '0' inicial da calculado
        if (self.validade == 0) and (int(self.texto['text']) == 0):
            self.texto['text'] = ''
            self.validade = 1
        #Limpa a calculadora sempre que um botão é pressionado após a realização de um cálculo
        if self.calc == True:
            self.texto['text'] = str(self.texto['text'])
            self.calc = False

    def popup(self):
        self.p = Tk()
        self.p.geometry("200x90")
        self.p.title('Sobre')
        self.p.wm_resizable(width=False, height=False)

        self.dados = 'Dev\tBryann Henrique\nVersão\t1.0\nData\t23/01/2017'
        self.info = Label(self.p, text=self.dados, font=20, justify=LEFT)
        self.info.pack(side=LEFT)

        self.p.mainloop()

    def sair(self): quit()

i = Tk()
app(i)
i.mainloop()
