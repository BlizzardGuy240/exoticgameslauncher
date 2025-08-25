import random
import tkinter as tk

path = "/assets/hangman"

root = tk.Tk()
root.title("Hangman")
root.geometry('615x365')
ez = [f"{path}0.png",f"{path}1.png",f"{path}2.png",f"{path}3.png",f"{path}4.png",f"{path}5.png",f"{path}6.png",f"{path}7.png",f"{path}8.png",f"{path}9.png",f"{path}10.png",f"{path}11.png",f"{path}12.png"]
mid = [f"{path}0.png",f"{path}2.png",f"{path}4.png",f"{path}5.png",f"{path}6.png",f"{path}8.png",f"{path}10.png",f"{path}12.png"]
har = [f"{path}0.png",f"{path}4.png",f"{path}6.png",f"{path}10.png",f"{path}12.png"]
pics = [f'{path}0.png']
words=["COFFEE","LABURNUM","RHYTHM","CATALYST","LYNX"]
word = list(words[random.randrange(0,len(words))])
display = list(len(word)*'_')
mis = 0

def disp():
    s = ''
    for i in display:
        s += i
    return(s)
def wor():
    s = ''
    for i in word:
        s += i
    return s

def del_inp():
    inp.delete(0,tk.END)

def first():
    global pics
    pics = ez
    game_screen()
    select.place(x=-200,y=0)
    easy.place(x=-200,y=50)
    med.place(x=-200,y=100)
    hard.place(x=-200,y =150)
    Hangman.place(x=-300,y=0)
def second():
    global pics
    pics = mid
    game_screen()
    select.place(x=-200,y=0)
    easy.place(x=-200,y=50)
    med.place(x=-200,y=100)
    hard.place(x=-200,y =150)
    Hangman.place(x=-300,y=0)
def third():
    global pics
    pics = har
    game_screen()
    select.place(x=-200,y=0)
    easy.place(x=-200,y=50)
    med.place(x=-200,y=100)
    hard.place(x=-200,y =150)
    Hangman.place(x=-300,y=0)


def press():
    game_screen()
    global ch
    global mis
    global dis
    global image
    global im
    
    if len(ch)!=1:
        err = tk.Label(root, text='Input 1 Letter', font=("Arial",17))
        err.place(x=10,y=10)
    else:
        err = tk.Label(root, text='                                       ',font=('Arial',17))
        err.place(x=10,y=10)
        if ch in word:
            for i in range(0,len(word)):
                if ch == word[i]:
                    display[i] = word[i]
                    dis = tk.Label(root, text=disp(), font = ("Arial", 24))
                    dis.place(x=30,y=50)
        else:
            mis += 1

    image = tk.PhotoImage(file = pics[mis])
    im = tk.Label(root, image=image )
    im.place(x=250,y=0)

    del_inp()

    if pics[mis]== f'{path}12.png':
        lose = tk.Label(root, text = f'You lose :( \n The word was {wor()}', font=('Arial',17))
        lose.place(x=25,y=200)
        inp.config(state='disabled')
    if display == word:
        win = tk.Label(root, text = 'You win!!!', font=('Arial',17))
        win.place(x=25,y=200)
        inp.config(state='disabled')
        image = tk.PhotoImage(file = f'{path}win.png')
        im = tk.Label(root, image=image )
        im.place(x=250,y=0)

Hangman = tk.Label(root, text = "HANGMAN", font=("Times New Roman",36))
select = tk.Label(root,text="Select Mode:",font = ('Arial',21))
easy = tk.Button(root, text='Easy', command=first)
med = tk.Button(root, text="Medium",command=second)
hard = tk.Button(root, text='Hard',command=third)    
Hangman.place(x=165, y=25)
select.place(x=206,y=100)
easy.place(x=275,y=150)
med.place(x=263,y=200)
hard.place(x=275,y = 250)

image = tk.PhotoImage(file = pics[mis])
im = tk.Label(root, image=image )
dis = tk.Label(root, text=disp(), font = ("Arial", 24))
Gu = tk.Label(root, text="Guess:", font = ('Arial',24))
inp = tk.Entry(root, font=('Arial',24),width = 2)
Button = tk.Button(root, text='Guess', command=press)


def game_screen():
    global ch
    im.place(x=250,y=0)
    dis.place(x=30,y=50)
    Gu.place(x=25,y=100)
    inp.place(x=140,y=100)
    Button.place(x=75,y=150)
    ch = inp.get()
tk.mainloop()