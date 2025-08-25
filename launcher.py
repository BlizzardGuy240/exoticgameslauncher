import sys
import os
import csv
import tkinter as tk
from tkinter import messagebox as msb
import pickle
import subprocess as sp
from tkinter import font
from PIL import ImageTk, Image
import pyglet

from game.dino_game import run
from game.egg_catcher import run
from game.hangman import run
from game.reaction_test import run

try:
    with open("sensitive.dat", 'rb'):
        pass
except FileNotFoundError:
    sp.run(['python', 'defaulter.py'])


if __name__ == "__main__":
    def launcher():
        launcher = tk.Tk()
        launcher.title("Exotic Games Launcher")
        launcher.geometry("800x400")
        launcher.configure(bg = "#321321")

        label = tk.Label(launcher, text = f"Welcome to Exotic Games, {user}", font = ("Comic Sans MS", 18), fg = "white", bg="#321321")
        label.pack()

        # test = ImageTk.PhotoImage(Image.open("start.png").resize((150, 150)))
        # b = tk.Button(side, image=test)
        # b.pack()

        my_title_font = font.Font(family="Comic Sans MS", size = 29)
        my_font = font.Font(family="TT Rounds Neue Trial Condensed Regular", size=9)
        my_font = pyglet.font.add_file("TT Rounds Neue Trial Condensed Regular.ttf")
        def resize_font(event):
            new_size = max(9, int(event.width / 50))
            new_title_size = max(29, int(event.width / 50))
            my_title_font.configure(size=new_title_size)
        
        side = tk.Frame(launcher, bg="#1d106c")
        side.place(x=0,y=35, relwidth=0.4375, relheight=1, bordermode="outside") #width = 350
        side.pack_propagate(False)

        main = tk.Frame(launcher, bg="#3F5F68")
        main.place(relx=0.4375, y=35, relwidth=0.5625, relheight=1)
        main.pack_propagate(False)

        filler=tk.Label(main, text='\n\n', bg="#3F5F68").pack()
        text = tk.Label(main, text="Click on a game to get started...!", font=font.Font(family="Consolas 20 bold", size=50, slant='italic'), bg="#3F5F68", fg="#FFFFFF", wraplength=400)
        text.pack(expand=True, anchor='n')

        def egg_click():
            global frame1
            frame1 = tk.Frame(main, bg="#3F5F68")
            frame1.place(x=0, y=0, relwidth=1, relheight=1)
            frame1.pack_propagate(False)

            def store_score():
                f = open("./egg_catcher/egg_catcher_scores.csv", "a", newline='')
                g = open("temp_egg_scores.csv", "r")
                w = csv.writer(f)
                for i in csv.reader(g):
                    w.writerow([user, i])
                f.close()
                g.close()
                os.remove(".temp_egg_scores.csv")

            def play():
                game.egg_catcher.run()
                store_score()

            title = tk.Label(frame1, text="EGG CATCHER", font=my_title_font, bg="#3F5F68", fg="#FFFFFF")
            text = tk.Label(frame1, text="""Eggs are falling from the sky! Can you catch them all? Showcase your determination to save them all while racking up unimaginable scores with the score multiplier in different difficulties. Press play to relieve stress!""",
                            wraplength=400, font=my_font, bg="#3F5F68", fg="#FFFFFF")
            play_btn = tk.Button(frame1, text="PLAY", command=play)

            image_open = Image.open("/assets/launcher/dino_game3.png")
            image = ImageTk.PhotoImage(image_open)
            image_label = tk.Label(frame1, image=image)

            title.pack(expand=False, fill="both")
            text.pack(expand=False, fill="both")
            image_label.pack(expand=False, fill="none")
            play_btn.pack(expand=False, pady=5, fill="none")

        def dino_click():
            global frame2
            frame2 = tk.Frame(main, bg="#3F5F68")
            frame2.place(x=0, y=0, relwidth=1, relheight=1)
            frame2.pack_propagate(False)

            def store_score():
                f = open("./dino_game/dino_scores.csv", "a", newline='')
                g = open("./dino_game/temp_dino_scores.csv", "r")
                w = csv.writer(f)
                for i in csv.reader(g):
                    w.writerow([user, i])
                f.close()
                g.close()
                os.remove("./dino_game/temp_dino_scores.csv")

            def play():
                game.dino_game.run()
                store_score()

            title = tk.Label(frame2, text="DINO GAME", font=my_title_font, bg="#3F5F68", fg="#FFFFFF")
            text = tk.Label(frame2, text="""Give your spacebar a test today by joining the competition to get the highest score in this endless runner game, called DINO. Press play to demonstrate your precise timing, and ambition!""",
                            wraplength=400, font=my_font, bg="#3F5F68", fg="#FFFFFF")
            play_btn = tk.Button(frame2, text="PLAY", command=play)

            image_open = Image.open("/assets/launcher/dino_game3.png")
            image = ImageTk.PhotoImage(image_open)
            image_label = tk.Label(frame2, image=image)

            title.pack(expand=False, fill="both")
            text.pack(expand=False, fill="both")
            image_label.pack(expand=False, fill="none")
            play_btn.pack(expand=False, pady=5, fill="none")           
            
            # title.place(relx=0, rely=0, relwidth=1, relheight=0.2)
            # text.place(relx=0, rely=0.15, relwidth=1, relheight=0.24)
            # play_btn.place(relx)
            
        def hangman_click():
            global frame3
            frame3 = tk.Frame(main, bg="#3F5F68")
            frame3.place(x=0, y=0, relwidth=1, relheight=1)
            frame3.pack_propagate(False)

            def play():
                sp.run(["python", "./hangman/hangman.py"])

            title = tk.Label(frame3, text="HANGMAN", font=my_title_font, bg="#3F5F68", fg="#FFFFFF")
            text = tk.Label(frame3, text="""The best productive game to test your vernacular and deductive skills with a simple GUI, and a not-so-simple library of words that range from easy to hard. Press play to destroy OR get destroyed!""",
                            wraplength=400, font=my_font, bg="#3F5F68", fg="#FFFFFF")
            play_btn = tk.Button(frame3, text="PLAY", command=play)

            image_open = Image.open("/assets/launcher/hangman_image.png")
            image = ImageTk.PhotoImage(image_open.resize((300,200)))
            image_label = tk.Label(frame3, image=image)

            title.pack(expand=False, fill="both")
            text.pack(expand=False, fill="both")
            image_label.pack(expand=False, fill="none")
            play_btn.pack(expand=False, pady=5, fill="none")
            
        def reaction_click():
            global frame4
            frame4 = tk.Frame(main, bg="#3F5F68")
            frame4.place(x=0, y=0, relwidth=1, relheight=1)
            frame4.pack_propagate(False)

            def store_score():
                f = open("./reaction_test/reaction_test_scores.csv", "a", newline='')
                g = open("./reaction_test/temp_reaction_scores_FINAL.csv", "r")
                w = csv.writer(f)
                for i in csv.reader(g):
                    w.writerow([user, i])
                f.close()
                g.close()
                os.remove("./reaction_test/temp_reaction_scores_FINAL.csv")

            def play():
                sp.run(["python", "./reaction_test/reaction_test.py"])
                store_score()

            title = tk.Label(frame4, text="REACTION TEST", font=my_title_font, bg="#3F5F68", fg="#FFFFFF")
            text = tk.Label(frame4, text="""READY? SET! GO!! A fun game with the premise of being a lights-out reaction test for the player to train their speeds. Press play and let's see what you can do!""",
                            wraplength=400, font=my_font, bg="#3F5F68", fg="#FFFFFF")
            play_btn = tk.Button(frame4, text="PLAY", command=play)

            image_open = Image.open("/assets/launcher/hangman_image.png")
            image = ImageTk.PhotoImage(image_open.resize((300,200)))
            image_label = tk.Label(frame4, image=image)

            title.pack(expand=False, fill="both")
            text.pack(expand=False, fill="both")
            image_label.pack(expand=False, fill="none")
            play_btn.pack(expand=False, pady=5, fill="none")

        egg_img = ImageTk.PhotoImage(Image.open("/assets/launcher/egg_catcher.png").resize((110, 120)))
        egg_btn = tk.Button(side, image=egg_img, bg = "#61451A", borderwidth=5, command=egg_click)
        egg_btn.place(relx=0.035, rely=0.015, relwidth=0.4, relheight=0.4)

        dino_img = ImageTk.PhotoImage(Image.open("/assets/launcher/dino2.png").resize((110, 120)))
        dino_btn = tk.Button(side, image=dino_img, bg = "#623456", borderwidth=5, command=dino_click)
        dino_btn.place(relx=0.56, rely=0.015, relwidth=0.4, relheight=0.4)

        han_img = ImageTk.PhotoImage(Image.open("/assets/launcher/hangman.png").resize((110, 120)))
        han_btn = tk.Button(side, image=han_img, bg = "#EFDECD", borderwidth=5, command=hangman_click)
        han_btn.place(relx=0.035, rely=0.48, relwidth=0.4, relheight=0.4)

        reat_img = ImageTk.PhotoImage(Image.open("/assets/launcher/react.png").resize((110, 120)))
        reat_btn = tk.Button(side, image=reat_img, bg = "#FFFF4D", borderwidth=5, command=reaction_click)
        reat_btn.place(relx=.56, rely=0.48, relwidth=0.4, relheight=0.4)
        
        def settings():
            pass
        
        settings_img = ImageTk.PhotoImage(Image.open("/assets/launcher/settings.png"))

        settings = tk.Button(launcher, image=settings_img)
        settings.place(relx=0.96, rely=0.0075)
        
        launcher.bind("<Configure>", resize_font)

        launcher.mainloop()

    #Initializing the Window
    window = tk.Tk()
    window.geometry("300x250")
    window.configure(bg = "#333333")

    def main():
        window.title("Exotic Games")
        window.geometry("300x225")
        global frame1
        frame1 = tk.Frame(window, width=300, height=225)
        frame1.configure(bg = "#333333")
        frame1.pack()
        frame1.pack_propagate(False)

        msg = tk.Label(frame1, text = "  Welcome,\nTo Exotic Games!", font = font.Font(family="Arial", size=25, slant="roman"), fg = "white", bg = "#333333")
        msg2 = tk.Label(frame1, text = "Please login or signup\nto proceed to the launcher", font = font.Font(family="Arial", size=10, slant="italic"), fg = "white", bg = "#333333")

        log_btn = tk.Button(frame1, text = "Login", font = ("Arial", 18), command = login, fg = "white", bg = "#333333")
        sign_btn = tk.Button(frame1, text = "Signup", font = ("Arial", 18), command = signup, fg = "white", bg = "#333333")

        msg3 = tk.Label(frame1, text = "to a pre-existing account", fg = "white", bg = "#333333")
        msg4 = tk.Label(frame1, text = "using a new account", fg = "white", bg = "#333333")
        msg5 = tk.Label(frame1, text = "OR", fg = "white", bg = "#333333")

        msg.grid(row = 1, column = 1, columnspan= 2, sticky = "news")
        msg2.grid(row = 4, column = 1, columnspan = 2)
        log_btn.grid(row = 7, column = 1, pady = 10)
        sign_btn.grid(row = 7, column = 2)
        msg3.grid(row = 8, column = 1, sticky = "w")
        msg4.grid(row = 8, column  = 2)
        msg5.grid(row = 7, column = 1, sticky = "e")


    def login():
        window.title("Login Page")
        window.geometry("300x250")
        global frame2
        frame1.destroy()
        frame2 = tk.Frame(window, width=300, height=250)
        frame2.configure(bg = "#333333")
        frame2.pack()
        frame2.pack_propagate(False)
        
        def validate():
            global user
            user = username_enter.get()
            passw = password_enter.get()
            f = open("sensitive.dat", "rb")
            data = pickle.load(f)
            f.close()
            if passw != "" and user != "":
                if user in data:
                    if data[user] == passw:
                        window.destroy()
                        launcher()                
                    else:
                        incorrect = msb.showerror("Error", "Incorrect Password or Username")
                        password_enter.delete(0, tk.END)
                        pass 
                else:
                    msb.showerror("Error", "Username does not exist, please sign up")
                    signup()
            else:
                msb.showerror("Error", "Please enter valid credentials")     
                
        def back():
            frame2.destroy()
            main()
            back_btn.destroy()

        msg = tk.Label(frame2, text = "Login to Exotic Games", font = ("Arial", 18), fg = "white", bg = "#333333")
        msg2 = tk.Label(frame2, text = "using your username and password", font = font.Font(family="Arial", size=10, slant="italic"), fg = "white", bg = "#333333")
        blank = tk.Label(frame2, text = "", font = ("Arial", 10), fg = "white", bg = "#333333")
        blank2 = tk.Label(frame2, text = "", font = ("Arial", 5), fg = "white", bg = "#333333")
        blank3 = tk.Label(frame2, text = "", font = ("Arial", 10), fg = "white", bg = "#333333")
        blank4 = tk.Label(frame2, text = "", font = ("Arial", 10), fg = "white", bg = "#333333")
        txt = tk.Label(frame2, text = "   Username", fg = "white", bg = "#333333", font = ("Arial", "16"))
        username_enter = tk.Entry(frame2)
        txt2 = tk.Label(frame2, text = "   Password", fg = "white", bg = "#333333", font = ("Arial", "16"))
        password_enter = tk.Entry(frame2, show = "*")
        confirm_btn = tk.Button(frame2, text = "Confirm", command = validate, fg = "white", bg = "#333333")
        back_btn = tk.Button(frame2, text = "Back", command = back, fg = "white", bg = "#333333")

        blank4.grid(row = 0, column = 1)
        msg.grid(row = 1, column = 1, sticky = "news")
        msg2.grid(row = 2, column = 1, sticky = "n")
        blank.grid(row = 3)
        txt.grid(row = 5, column = 1, sticky = "w")
        username_enter.grid(row = 5, column = 1, sticky = "e")
        blank2.grid(row = 6)
        txt2.grid(row = 7, column = 1, sticky = "w")
        password_enter.grid(row = 7, column = 1, sticky = "e")
        blank3.grid(row = 8, column = 1)
        confirm_btn.grid(row = 9, column = 1, sticky = "se")
        back_btn.grid(row = 9, column = 1, sticky = "sw")

    def signup():
        window.title("Signup Page")
        global frame3
        frame1.destroy()
        window.geometry("300x310")
        frame3 = tk.Frame(window, width=300, height=310)
        frame3.configure(bg = "#333333")
        frame3.pack()
        frame3.pack_propagate(False)

        def back():
            frame3.destroy()
            main()
            back_btn.destroy()
        
        def correctLength():
            if len(pass_entry1.get()) < 8 or len(user_entry.get()) < 8:
                return False
            else:
                return True
        
        def validUsername():
            for char in r"!@#$%^&*()-_=+[]{}|;:'\",.<>?/\`~":
                if char in user_entry.get():
                    return False
            else:
                return True
        
        def validPassword():
            count = 0
            for char in r"!@#$%^&*()-_=+[]{}|;:'\",.<>?/\`~":
                if char in pass_entry1.get():
                    count += 1
            if count >= 1:
                return True
            else:
                return False
        
        def matchPasswords():
            if pass_entry1.get() == pass_entry2.get():
                return True
            else:
                return False
        
        def createacc():
            if not correctLength():
                return msb.showerror("Error", "Password & username must be greater than 8 characters")
            elif not validUsername():
                return msb.showerror("Error", "Username must not contain special character(s)")
            elif not validPassword():
                return msb.showwarning("Warning", "Password does not contain special character(s)")
            elif not matchPasswords():
                for i in (pass_entry1, pass_entry2):
                    i.delete(0, tk.END)
                return msb.showerror("Error", "Passwords entered do not match")
            else:
            
                with open("sensitive.dat", "rb") as f:
                        data = pickle.load(f)
                if user_entry.get() not in data:

                    g = open("sensitive.dat", "wb")
                    data.update({user_entry.get(): pass_entry1.get()})
                    pickle.dump(data, g)

                    global msg
                    msg = msb.showinfo("Success!", "Account successfully created, please log in through our portal")
                    back()
                
                else:
                    return msb.showerror("Error", "Username already exists")


        blank = tk.Label(frame3, text = "", font = ("Arial", 10), fg = "white", bg = "#333333")
        txt = tk.Label(frame3, text = "Sign Up to Exotic Games", font = ("Arial", 18), fg = "white", bg = "#333333")
        txt2 = tk.Label(frame3, text = "Enter a username", fg = "white", bg = "#333333")
        user_entry = tk.Entry(frame3)
        txt3 = tk.Label(frame3, text = "Enter a password", fg = "white", bg = "#333333")
        txt4 = tk.Label(frame3, text = "Confirm your password", fg = "white", bg = "#333333")
        pass_entry1 = tk.Entry(frame3, show = "*")
        pass_entry2 = tk.Entry(frame3, show = "*")
        confirm_btn = tk.Button(frame3, text = "Confirm", command = createacc, fg = "white", bg = "#333333")
        back_btn = tk.Button(frame3, text = "Back", command = back, fg = "white", bg = "#333333")
        inst = tk.Label(frame3, text = "INSTRUCTIONS:\n1. Username and password must be greater or equal to 8 characters\n2. Username must not contain any special characters\n3. Password must contain ATLEAST one special character\n4. Username must be unique"
                        , font = font.Font(family="Arial", size=7, slant="italic"), bg = "#333333", fg = "#FFFFFF", justify="left")

        blank.pack()
        txt.pack()
        txt2.pack()
        user_entry.pack()
        txt3.pack()
        pass_entry1.pack()
        txt4.pack()
        pass_entry2.pack()
        confirm_btn.pack(pady = 5)
        back_btn.pack()
        inst.pack()




    main()

    window.mainloop()

