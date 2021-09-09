from tkinter import * #importando tudo do tkinter

janela = Tk() #Criando uma variavel para receber a classe Tkinter
janela.title("Minha Primeira Janela") # Coloca o titulo no topo da janela
janela.geometry("500x300")#tamanho da tela, largura por altura
janela.configure(background = "#008") #colocar a cor de fundo em RGB

txt1 = Label(janela,text="Curso de Python",background = "#ff0",foreground = "#000") # Inserindo uma Label e configurando
txt1.place(x=10,y=10,width = 150, height=30) # para que o Lable apareça cplocamos a posição x e Y e width - largura, height - altura





janela.mainloop() #colocando o loop da janela
