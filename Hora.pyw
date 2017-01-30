from tkinter import *
import time

class app:
    def __init__(self, inst):
        self.jan = inst

        self.tela()

    def tela(self):
        self.jan.geometry('605x150+900+650')
        self.jan.title('Relógio')
        self.jan.wm_resizable(width=False, height=False)

        #Texto
        self.texto = Label(self.jan, text='00:00:00', font=('Ebrima', 120))
        self.texto.pack()

        #Menu superior
        self.menu = Menu(self.jan)
        self.jan.config(menu=self.menu)

        self.sobre = Menu(self.menu, tearoff = 0)
        self.sobre.add_command(label = 'Sobre', command=self.popup)
		
        self.posic = Menu(self.menu, tearoff = 0)
        self.posic.add_command(label='Superior direito', command = self.supD)
        self.posic.add_command(label='Superior esquerdo', command = self.supE)
        self.posic.add_command(label='Inferior direito', command = self.infD)
        self.posic.add_command(label='Inferior esquerdo', command = self.infE)
        self.posic.add_command(label='Centro', command = self.centro)

        self.menu.add_cascade(label='Posição', menu=self.posic)
        self.menu.add_cascade(label='Sobre', menu=self.sobre)

        #Função hora
        self.hora()

    def supD(self): self.jan.geometry('605x150+900+50')
    def supE(self): self.jan.geometry('605x150+50+50')
    def infD(self): self.jan.geometry('605x150+900+650')
    def infE(self): self.jan.geometry('605x150+50+650')
    def centro(self):
        #Obtendo altura e largura do monitor
        self.larguraTela = self.jan.winfo_screenwidth()
        self.alturaTela = self.jan.winfo_screenheight()

        #Calculando cordenadas x e y
        self.largura = (self.larguraTela/2) - (605/2)
        self.altura = (self.alturaTela/2) - (150/2)

        self.jan.geometry('605x150+%i+%i' %(self.largura, self.altura))
        
    def hora(self):
        self.horario = time.strftime('%H:%M:%S')
        self.texto['text'] = self.horario

        self.jan.after(1000, self.hora)

    def popup(self):
        self.p = Tk()
        self.p.geometry("200x90+900+520")
        self.p.title('Sobre')
        self.p.wm_resizable(width=False, height=False)

        self.dados = 'Dev\tBryann Henrique\nVersão\t1.0\nData\t23/01/2017'
        self.info = Label(self.p, text=self.dados, font=20, justify=LEFT)
        self.info.pack(side=LEFT)

        self.p.mainloop()
            
i = Tk()
app(i)
i.mainloop()





















