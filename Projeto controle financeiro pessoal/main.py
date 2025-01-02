from tkinter import *
from tkinter import Tk, ttk

# importando Pillow
from PIL import Image, ImageTk

# Cores

co0 = "#2e2d2b" # Preta
co1 = "#feffff" #branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # Valor
co4 = "#403d3d" # Letra
co5 = "#e06636" 
co6 = "#038cfc" 
co7 = "#3fbfb9" 
co8 = "#263238" 
co9 = "#e9edf5" 

colors = ["#5588bb", "#66bbbb", "#99bb55", "ee9944", "#444466", "#bb5555"]

# criando janela vazia
janela = Tk()
janela.title()
janela.geometry("900x650")
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style= ttk.Style(janela)
style.theme_use('clam')

# criando frames para divisão da tela
frameCima = Frame(janela, width=1040, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1040, height=361, bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1040, height=300, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)


# trabalhando no frame Cima

# Acessando a imagem
app_img = Image.open("logo.jpg")
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Orçamento Pessoal", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=("verdana 20 bold"), bg=co1, fg=co4)
app_logo.place(x=0, y=0)



janela.mainloop()