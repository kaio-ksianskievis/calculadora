from cProfile import label
from cgitb import text
from heapq import heappush
from pickle import FRAME
from tkinter import *
from tkinter import ttk
from turtle import right, width


color1 = '#000000'#preta
color2= '#ECEFF1'#cinza
color3='#FFAB40'#laranja
color4='#feffff'#branca
janela = Tk()
janela.title('ksianskievis')
janela.geometry('235x300')
frame_tela = Frame(janela,width=235, height=50,bg=color1)
frame_tela.grid(row=0,column=0)
frama_corpo = Frame(janela,width=235,height=250)
frama_corpo.grid(row=1,column=0)

espessão=''
def printar(valor):
    global espessão
    espessão = espessão+str(valor)
    valor_texto.set(espessão)
def apagar():
    global espessão
    espessão = ""
    valor_texto.set("")

def calcular():
    global espessão
    resultado=eval(espessão)
    espessão=""
    valor_texto.set(resultado)


valor_texto = StringVar()


lb = Label(frame_tela,textvariable=valor_texto,width=16,height=2,padx=7,relief=FLAT,anchor='e',justify=RIGHT,font=('ivy 18'))
lb.place(x=0,y=0)
#botões
b_1= Button(frama_corpo,command=lambda:apagar() ,text='C',width=11,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_1.place(x=0,y=0)
b_2 = Button(frama_corpo,command=lambda:printar('%'),text='%',width=5,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_2.place(x=118,y=0)
b_3 = Button(frama_corpo,command=lambda:printar('/'),text='/',width=5,height=2,bg=color3,fg=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_3.place(x=177,y=0)
b_4 = Button(frama_corpo,command=lambda:printar('7'),text='7',width=5,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_4.place(x=0,y=50)
b_5 = Button(frama_corpo,command=lambda:printar('8'),text='8',width=5,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_5.place(x=60,y=50)
b_6 = Button(frama_corpo,command=lambda:printar('9'),text='9',width=5,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_6.place(x=118,y=50)
b_7 = Button(frama_corpo,command=lambda:printar('*'),text='*',width=5,height=2,bg=color3,fg=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_7.place(x=177,y=50)
b_8 = Button(frama_corpo,command=lambda:printar('4'),text='4',width=5,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_8.place(x=0,y=100)
b_9 = Button(frama_corpo,command=lambda:printar('5'),text='5',width=5,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_9.place(x=60,y=100)
b_10 = Button(frama_corpo,command=lambda:printar('6'),text='6',width=5,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_10.place(x=118,y=100)
b_11 = Button(frama_corpo,command=lambda:printar('-'),text='-',width=5,height=2,bg=color3,fg=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_11.place(x=177,y=100)
b_12 = Button(frama_corpo,command=lambda:printar('1'),text='1',width=5,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_12.place(x=0,y=150)
b_13 = Button(frama_corpo,command=lambda:printar('2'),text='2',width=5,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_13.place(x=60,y=150)
b_14 = Button(frama_corpo,command=lambda:printar('3'),text='3',width=5,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_14.place(x=118,y=150)
b_15 = Button(frama_corpo,command=lambda:printar('+'),text='+',width=5,height=2,bg=color3,fg=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_15.place(x=177,y=150)
b_16 = Button(frama_corpo,command=lambda:printar('0'),text='0',width=11,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_16.place(x=0,y=200)
b_17 = Button(frama_corpo,command=lambda:printar('.'),text='.',width=5,height=2,bg=color2,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_17.place(x=118,y=200)
b_18 = Button(frama_corpo,command=lambda:calcular(),text='=',width=5,height=2,bg=color3,fg=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b_18.place(x=177,y=200)






janela.mainloop()