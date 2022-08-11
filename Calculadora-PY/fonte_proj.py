from cProfile import label
from cgitb import text
from msilib.schema import Font
from tkinter import *
from tkinter import font

screen = Tk()
screen.title("CALCULADORA")
screen.iconbitmap("void_icone.ico")

#para caracteres especiais


def delet():
    tela.delete(0, END)

def botao_ponto():
    tela.insert(END, ".")

def botao_soma():
    numero1 = tela.get()
    global pri_numero #variavel global
    global calculo
    calculo = "soma"
    pri_numero = float(numero1)
    tela.delete(0, END)


def botao_sub():
    numero1 = tela.get()
    global pri_numero
    global calculo
    calculo = "subtracao"
    pri_numero = float(numero1)
    tela.delete(0, END)

def botao_divisao():
    numero1 = tela.get()
    global pri_numero
    global calculo
    calculo = "divisao"
    pri_numero = float(numero1)
    tela.delete(0, END)

def botao_multi():
    numero1 = tela.get()
    global pri_numero
    global calculo
    calculo = "multiplicacao"
    pri_numero = float(numero1)
    tela.delete(0, END)

def botao_igual():
    numero2 = tela.get()#liberar tudo que esta em tela
    tela.delete(0, END)
    if calculo == "soma":
        tela.insert(0, pri_numero + float(numero2)) #somar na calculadora
    if calculo == "subtracao":
        tela.insert(0, pri_numero - float(numero2))#subtrair na calculadora
    if calculo == "multiplicacao":
        tela.insert(0, pri_numero * float(numero2))#multiplicar na calculadora
    if calculo == "divisao":
        tela.insert(0, pri_numero / float(numero2))#dividir na calculadora





#para os numeros
def clickbotao(num): #funcao para os cliques funcionarem
    click = tela.get()
    tela.delete(0, END)
    tela.insert(END, str(click) + str(num))





label1 = Label(screen, text="CALCULADORA", font=("Arial", 18, "bold"), bg = "black" , padx=14,pady = 10, fg="orange")
label1.pack()

tela = Entry(screen, bg="orange", bd=8, font=("Arial" ,20, "bold"))
tela.pack()

screen["bg"] = "black"

#criando botoes
botao7 = Button(screen, text="7", bg="orange", pady=14, padx=16, bd=0, font=("Arial" ,20, "bold"), command= lambda: clickbotao(7))
botao7.place(x=15,y=120)

botao8 = Button(screen, text="8", bg="orange", pady=14, padx=16, bd=0, font=("Arial" ,20, "bold"), command= lambda: clickbotao(8))
botao8.place(x=100,y=120)

botao9 = Button(screen, text="9", bg="orange", pady=14, padx=16, bd=0, font=("Arial" ,20, "bold"), command= lambda: clickbotao(9))
botao9.place(x=185,y=120)

botaox = Button(screen, text="x", bg="orange", pady=14, padx=16, bd=0, font=("Arial" ,20, "bold"), command=botao_multi)
botaox.place(x=270,y=120)

botao4 = Button(screen, text="4", bg="orange", pady=14, padx=16, bd=0, font=("Arial" ,20, "bold"), command= lambda: clickbotao(4))
botao4.place(x=15,y=210)

botao5 = Button(screen, text="5", bg="orange", pady=14, padx=16, bd=0, font=("Arial" ,20, "bold"), command= lambda: clickbotao(5))
botao5.place(x=100,y=210)

botao6 = Button(screen, text="6", bg="orange", pady=14, padx=16, bd=0, font=("Arial" ,20, "bold"), command= lambda: clickbotao(6))
botao6.place(x=185,y=210)

botaod = Button(screen, text="/", bg="orange", pady=14, padx=19, bd=0, font=("Arial" ,20, "bold"), command=botao_divisao)
botaod.place(x=270,y=210)

botao1 = Button(screen, text="1", bg="orange", pady=14, padx=16, bd=0, font=("Arial" ,20, "bold"), command= lambda: clickbotao(1))
botao1.place(x=15,y=300)

botao2 = Button(screen, text="2", bg="orange", pady=14, padx=16, bd=0, font=("Arial" ,20, "bold"), command= lambda: clickbotao(2))
botao2.place(x=100,y=300)

botao3 = Button(screen, text="3", bg="orange", pady=14, padx=16, bd=0, font=("Arial" ,20, "bold"), command= lambda: clickbotao(3))
botao3.place(x=185,y=300)

botaos = Button(screen, text="+", bg="orange", pady=14, padx=15, bd=0, font=("Arial" ,20, "bold"), command=botao_soma)
botaos.place(x=270,y=300)

botaoi = Button(screen, text="=", bg="orange", pady=3, padx=15, bd=0, font=("Arial" ,20, "bold"), command=botao_igual)
botaoi.place(x=270,y=390)

botao0 = Button(screen, text="0", bg="orange", pady=3, padx=16, bd=0, font=("Arial" ,20, "bold"), command= lambda: clickbotao(0))
botao0.place(x=15,y=390)

botaop = Button(screen, text=".", bg="orange", pady=3, padx=19, bd=0, font=("Arial" ,20, "bold"), command=botao_ponto)
botaop.place(x=100,y=390)

botaom = Button(screen, text="-", bg="orange", pady=3, padx=19, bd=0, font=("Arial" ,20, "bold"), command=botao_sub)
botaom.place(x=185,y=390)

botaoac = Button(screen, text="AC", bg="orange", pady=138, padx=4, bd=0, font=("Arial" ,20, "bold"), command=delet)
botaoac.place(x=347,y=120)



screen.resizable(False, False) #usuario nao interfere na janela
screen.geometry("420x450")
screen.mainloop()



