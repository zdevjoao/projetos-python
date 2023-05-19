from tkinter import *

# Criando janela
root = Tk()
root.title('Sua calculadora')
# Tamanho janela
root.geometry('409x355')
root.minsize(400,355)
root.maxsize(400,355)

numero1 = ''
divisao = FALSE
multiplica = FALSE
adicao = FALSE
subtracao = FALSE
# Cor Background
root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg="#a7a28f", font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row = 0,
    column= 0,
    columnspan= 4,
    pady= 2
)
# Funçoes operadores
def botao_click(num):
    e.insert(END, num)
    return
def botao_divisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_multiplica():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = e.get()
    e.delete(0, END)
    return
def botao_subtracao():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)
    return
def botao_adicao():
    global numero1
    global adicao
    adicao = TRUE
    numero1 = e.get()
    e.delete(0, END)
    return
def botao_igual():
    global subtracao
    global adicao
    global multiplica
    global divisao
    numero2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        adicao = FALSE
    if multiplica == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplica = FALSE
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero1) // int(numero2))
        divisao = FALSE
    return
def botao_limpar():
    e.delete(0, END)
    return

divisao = Button(root,
                text='÷',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold'),
                
)
divisao.grid(row=0, column=4)
# Primeira fileira
um = Button(root,
                text='1',
                padx=40,
                pady=20,
                command=lambda: botao_click(1),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
# Primeira Fileira
um.grid(row=1, column=1)
dois = Button(root,
                text='2',
                padx=40,
                pady=20,
                command=lambda: botao_click(2),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
dois.grid(row=1, column=2)
tres = Button(root,
                text='3',
                padx=40,
                pady=20,
                command=lambda: botao_click(3),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
tres.grid(row=1, column=3)
multiplica = Button(root,
                text='×',
                padx=41,
                pady=20,
                command=botao_multiplica,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
multiplica.grid(row=1, column=4)
quatro = Button(root,
                text='4',
                padx=40,
                pady=20,
                command=lambda: botao_click(4),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
# Segunda Primeira
quatro.grid(row=2, column=1)
cinco = Button(root,
                text='5',
                padx=40,
                pady=20,
                command=lambda: botao_click(5),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
cinco.grid(row=2, column=2)
seis = Button(root,
                text='6',
                padx=40,
                pady=20,
                command=lambda: botao_click(6),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
seis.grid(row=2, column=3)
subtracao = Button(root,
                text='-',
                padx=43,
                pady=20,
                command=botao_subtracao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
subtracao.grid(row=2, column=4)
sete = Button(root,
                text='7',
                padx=40,
                pady=20,
                command=lambda: botao_click(7),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
sete.grid(row=3, column=1)
oito = Button(root,
                text='8',
                padx=40,
                pady=20,
                command=lambda: botao_click(8),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
oito.grid(row=3, column=2)
nove = Button(root,
                text='9',
                padx=40,
                pady=20,
                command=lambda: botao_click(9),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
nove.grid(row=3, column=3)
mais = Button(root,
                text='+',
                padx=41,
                pady=20,
                command=botao_adicao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
mais.grid(row=3, column=4)


# Quarta Fileira
zero = Button(root,
                text='0',
                padx=91,
                pady=20,
                command=lambda: botao_click(0),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
zero.grid(row=4, column=1, columnspan=2)
limpa = Button(root,
                text='C',
                padx=40,
                pady=20,
                command=botao_limpar,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
limpa.grid(row=4, column=4)
igual = Button(root,
                text='=',
                padx=40,
                pady=20,
                command=botao_igual,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
                
)
igual.grid(row=4, column=3)

# Mantem a janela em loop
root.mainloop()