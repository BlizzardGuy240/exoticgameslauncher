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

try:
    with open("sensitive.dat", 'rb'):
        pass
except FileNotFoundError:
    sp.run(['python', 'defaulter.py'])

if __name__ == "__main__":
    def delcurrentUser(event):
        try:
            os.remove("current_user.dat")
            sys.exit()
        except:
            pass
    
    def launcher():
        with open("current_user.dat", "wb") as f:
            pickle.dump(user, f)
        launcher = tk.Tk()
        launcher.title("Exotic Games Launcher")
        launcher.geometry("800x400")
        launcher.resizable(False, False)
        launcher.configure(bg = "#321321")

        label = tk.Label(launcher, text = f"Welcome to Exotic Games, {user}", font = ("Comic Sans MS", 18), fg = "white", bg="#321321")
        label.pack()

        # test = ImageTk.PhotoImage(Image.open("start.png").resize((150, 150)))
        # b = tk.Button(side, image=test)
        # b.pack()

        my_title_font = font.Font(family="Comic Sans MS", size = 29)
        my_font = font.Font(family=r"/assets/launcher/TT Rounds Neue Trial Condensed Regular", size=9)
        my_font = pyglet.font.add_file(r"assets\launcher\TT Rounds Neue Trial Condensed Regular.ttf")
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

        filler = tk.Label(main, text='\n\n ', bg="#3F5F68").pack()
        text = tk.Label(main, text="Click on a game to get started...!", font=font.Font(family="Consolas 20 bold", size=50, slant='italic'), bg="#3F5F68", fg="#FFFFFF", wraplength=400)
        text.pack(expand=True, anchor='n')

        def egg_click():
            global frame1
            frame1 = tk.Frame(main, bg="#3F5F68")
            frame1.place(x=0, y=0, relwidth=1, relheight=1)
            frame1.pack_propagate(False)

            def play():
                sp.run(['python', 'games\egg_catcher.py'])

            title = tk.Label(frame1, text="EGG CATCHER", font=my_title_font, bg="#3F5F68", fg="#FFFFFF")
            text = tk.Label(frame1, text="""Eggs are falling from the sky! Can you catch them all? Showcase your determination to save them all while racking up unimaginable scores with the score multiplier in different difficulties. Press play to relieve stress!""",
                            wraplength=400, font=my_font, bg="#3F5F68", fg="#FFFFFF")
            play_btn = tk.Button(frame1, text="PLAY", command=play)

            egg_open = Image.open(r"assets\launcher\egg_game.png").resize((300, 200), Image.Resampling.LANCZOS)
            image_e = ImageTk.PhotoImage(egg_open)
            image_label = tk.Label(frame1, image=image_e, borderwidth=5, relief="sunken")
            image_label.image = image_e

            title.pack(expand=False, fill="both")
            text.pack(expand=False, fill="both")
            image_label.pack(expand=False, fill="none")
            play_btn.pack(expand=False, pady=5, fill="none")

        def dino_click():
            global frame2
            frame2 = tk.Frame(main, bg="#3F5F68")
            frame2.place(x=0, y=0, relwidth=1, relheight=1)
            frame2.pack_propagate(False)

            def play():
                sp.run(['python', 'games\dino_game.py'])

            title = tk.Label(frame2, text="DINO GAME", font=my_title_font, bg="#3F5F68", fg="#FFFFFF")
            text = tk.Label(frame2, text="""Give your spacebar a test today by joining the competition to get the highest score in this endless runner game, called DINO. Press play to demonstrate your precise timing, and ambition!""",
                            wraplength=400, font=my_font, bg="#3F5F68", fg="#FFFFFF")
            play_btn = tk.Button(frame2, text="PLAY", command=play)

            dino_open = Image.open(r"assets\launcher\dino_game.png").resize((300, 200), Image.Resampling.LANCZOS)
            image_d = ImageTk.PhotoImage(dino_open)
            image_label = tk.Label(frame2, image=image_d, borderwidth=5, relief="sunken")
            image_label.image = image_d

            title.pack(expand=False, fill="both")
            text.pack(expand=False, fill="both")
            image_label.pack(expand=False, fill="none")
            play_btn.pack(expand=False, pady=5, fill="none")           

        def hangman_click():
            global frame3
            frame3 = tk.Frame(main, bg="#3F5F68")
            frame3.place(x=0, y=0, relwidth=1, relheight=1)
            frame3.pack_propagate(False)

            def play():
                sp.run(['python', r'games\hangman.py'])

            title = tk.Label(frame3, text="HANGMAN", font=my_title_font, bg="#3F5F68", fg="#FFFFFF")
            text = tk.Label(frame3, text="""The best productive game to test your vernacular and deductive skills with a simple GUI, and a not-so-simple library of words that range from easy to hard. Press play to destroy OR get destroyed!""",
                            wraplength=400, font=my_font, bg="#3F5F68", fg="#FFFFFF")
            play_btn = tk.Button(frame3, text="PLAY", command=play)

            hang_open = Image.open(r"assets\launcher\hangman_image.png").resize((300, 200), Image.Resampling.LANCZOS)
            image_h = ImageTk.PhotoImage(hang_open)
            image_label = tk.Label(frame3, image=image_h, borderwidth=5, relief="sunken")
            image_label.image = image_h

            title.pack(expand=False, fill="both")
            text.pack(expand=False, fill="both")
            image_label.pack(expand=False, fill="none")
            play_btn.pack(expand=False, pady=5, fill="none")
            
        def reaction_click():
            global frame4
            frame4 = tk.Frame(main, bg="#3F5F68")
            frame4.place(x=0, y=0, relwidth=1, relheight=1)
            frame4.pack_propagate(False)

            def play():
                sp.run(['python', r'games\reaction_test.py'])

            title = tk.Label(frame4, text="REACTION TEST", font=my_title_font, bg="#3F5F68", fg="#FFFFFF")
            text = tk.Label(frame4, text="""READY? SET! GO!! A fun game with the premise of being a lights-out reaction test for the player to train their speeds. Press play and let's see what you can do!""",
                            wraplength=400, font=my_font, bg="#3F5F68", fg="#FFFFFF")
            play_btn = tk.Button(frame4, text="PLAY", command=play)

            reaction_open = Image.open(r"assets\launcher\reaction_game.png").resize((300, 200), Image.Resampling.LANCZOS)
            image_r = ImageTk.PhotoImage(reaction_open)
            image_label = tk.Label(frame4, image=image_r, borderwidth=5, relief="sunken")
            image_label.image = image_r

            title.pack(expand=False, fill="both")
            text.pack(expand=False, fill="both")
            image_label.pack(expand=False, fill="none")
            play_btn.pack(expand=False, pady=5, fill="none")

        egg_img = ImageTk.PhotoImage(Image.open(r"assets\launcher\egg_catcher.png").resize((110, 120)))
        egg_btn = tk.Button(side, image=egg_img, bg = "#61451A", borderwidth=5, command=egg_click)
        egg_btn.place(relx=0.035, rely=0.015, relwidth=0.4, relheight=0.4)

        dino_img = ImageTk.PhotoImage(Image.open(r"assets\launcher\dino.png").resize((110, 120)))
        dino_btn = tk.Button(side, image=dino_img, bg = "#623456", borderwidth=5, command=dino_click)
        dino_btn.place(relx=0.56, rely=0.015, relwidth=0.4, relheight=0.4)

        han_img = ImageTk.PhotoImage(Image.open(r"assets\launcher\hangman.png").resize((110, 120)))
        han_btn = tk.Button(side, image=han_img, bg = "#EFDECD", borderwidth=5, command=hangman_click)
        han_btn.place(relx=0.035, rely=0.48, relwidth=0.4, relheight=0.4)

        reat_img = ImageTk.PhotoImage(Image.open(r"assets\launcher\react.png").resize((110, 120)))
        reat_btn = tk.Button(side, image=reat_img, bg = "#FFFF4D", borderwidth=5, command=reaction_click)
        reat_btn.place(relx=.56, rely=0.48, relwidth=0.4, relheight=0.4)
        
        def settings():
            # settings = tk.Tk()
            # settings.title("Settings")
            # settings.geometry("300x200")
            # settings.resizable(False, False)

            # global settings_1
            # settings_1 = tk.Frame(settings, width=300, height=200)
            # settings_1.configure(bg = "#333333")
            # settings_1.pack_propagate(False)

            # def changePassword():
                
            #     def validPassword(entry):
            #         count = 0
            #         for char in r"!@#$%^&*()-_=+[]{}|;:'\",.<>?/\`~":
            #             if char in entry.get():
            #                 count += 1
            #         if count >= 1:
            #             return True
            #         else:
            #             return False

            #     def validate():
            #         with open("sensitive.dat", "rb") as f:
            #             data = pickle.load(f)
            #             if old_p.get() == '':
            #                 if len(new_p.get()) >= 8:
            #                     if validPassword(new_p):
            #                         if data[user] == old_p.get():
            #                             data[user] == new_p.get()
            #                             msb.showinfo("Succesful", "Password successfully changed")
            #                             settings.destroy()
            #                         else:
            #                             msb.showerror("Error", "Incorrect password")
            #                             for i in (old_p, new_p):
            #                                 i.delete(0, tk.END)
            #                     else:
            #                         msb.showwarning("Warning", "Password does not contain special character(s)")
            #                         for i in (old_p, new_p):
            #                             i.delete(0, tk.END)
            #                 else:
            #                     msb.showerror("Error", "New password must be greater than 8 characters")
            #                     for i in (old_p, new_p):
            #                         i.delete(0, tk.END)
            #             else:
            #                 msb.showerror("Error", "All entries are mandatory")
                
            #         with open("sensitive.dat", "wb") as g:
            #             pickle.dump(data, g)

            #     settings_2 = tk.Frame(settings, width=300, height=200)
            #     settings_2.configure(bg = "#333333")
            #     settings_2.pack_propagate(False)
            #     settings_1.destroy()
            #     settings_2.pack()
            #     l = []
            #     old_password = tk.Label(settings_2, text = "Old Password")
            #     old_p = tk.Entry(settings_2)
            #     new_password = tk.Label(settings_2, text = "New Password")
            #     new_p = tk.Entry(settings_2)
            #     ok_btn = tk.Button(settings_2, text = "Confirm", command = validate)
            #     l.extend([old_password, old_p, new_password, new_p, ok_btn])
                      
            #     for i in l:
            #         i.pack()
            
            # def exit():
            #     ans = msb.askyesno("Logging Out", "Are you sure you want to exit?")
            #     if ans:
            #         delcurrentUser("event")
            #         launcher.destroy()
            #         settings.destroy()
            #     else:
            #         settings.destroy()
            
            # settings_1.pack()            
            # change_pass = tk.Button(settings_1, text = "Change Password", command = changePassword).pack()
            # logout_btn = tk.Button(settings_1, text = "Log Out", command = exit).pack()
            
            # settings.mainloop()
        
            settings_win = tk.Tk()
            settings_win.title("Settings")
            settings_win.geometry("300x200")
            settings_win.resizable(False, False)

            global settings_1
            settings_1 = tk.Frame(settings_win, width=300, height=200, bg="#333333")
            settings_1.pack_propagate(False)

            def changePassword():
                def validPassword(entry):
                    specials = r"!@#$%^&*()-_=+[]{}|;:'\",.<>?/\`~"
                    return any(char in specials for char in entry.get())

                def validate():
                    with open("sensitive.dat", "rb") as f:
                        data = pickle.load(f)

                    # Check all fields filled
                    if not old_p.get() or not new_p.get():
                        msb.showerror("Error", "All entries are mandatory")
                        return

                    # Check old password matches
                    if data.get(user) != old_p.get():
                        msb.showerror("Error", "Incorrect old password")
                        old_p.delete(0, tk.END)
                        new_p.delete(0, tk.END)
                        return

                    # Check new password length
                    if len(new_p.get()) < 8:
                        msb.showerror("Error", "New password must be at least 8 characters")
                        new_p.delete(0, tk.END)
                        return

                    # Check special character
                    if not validPassword(new_p):
                        msb.showwarning("Warning", "Password must contain at least one special character")
                        new_p.delete(0, tk.END)
                        return

                    # Update password
                    data[user] = new_p.get()
                    with open("sensitive.dat", "wb") as g:
                        pickle.dump(data, g)

                    msb.showinfo("Successful", "Password successfully changed")
                    settings_win.destroy()

                settings_2 = tk.Frame(settings_win, width=300, height=250, bg="#333333")
                settings_win.geometry("300x250")
                settings_2.pack_propagate(False)
                settings_1.destroy()
                settings_2.pack()

                txt1 = tk.Label(settings_2, text=f"Password change for,", font = font.Font(family="Arial", size=7, slant='roman'), fg = "white", bg = "#333333").pack()
                txt = tk.Label(settings_2, text=f"{user}", font = font.Font(family="Arial", size=7, slant="italic"), fg = "white", bg = "#333333").pack()
                old_password = tk.Label(settings_2, text="Old Password", bg="#333333", fg="white")
                old_p = tk.Entry(settings_2, show="*")
                new_password = tk.Label(settings_2, text="New Password", bg="#333333", fg="white")
                new_p = tk.Entry(settings_2, show="*")
                ok_btn = tk.Button(settings_2, text="Confirm", command=validate, fg = "white", bg = "#333333")

                for widget in (old_password, old_p, new_password, new_p, ok_btn):
                    widget.pack(pady=5)

            def exit_settings():
                ans = msb.askyesno("Logging Out", "Are you sure you want to exit?")
                if ans:
                    delcurrentUser("event")
                    launcher.destroy()
                    settings_win.destroy()
                else:
                    settings_win.destroy()

            settings_1.pack()
            tk.Label(settings_1, text = "Settings", font = ("Arial", 30), fg = "white", bg = "#333333").pack(pady=5)
            tk.Button(settings_1, text="Change Password", command=changePassword, fg = "white", bg = "#333333").pack(pady=10)
            tk.Button(settings_1, text="Log Out", command=exit_settings, fg = "white", bg = "#333333").pack(pady=10)

            settings_win.mainloop()
        
        settings_img = ImageTk.PhotoImage(Image.open(r"assets\launcher\settings.png"))

        settings = tk.Button(launcher, image=settings_img, command = settings)
        settings.image = settings_img
        settings.place(relx=0.959, y=2)


        def highscores():
            GAMES = {"Dino Game": "dino_scores", "Egg Catcher": "egg_scores", "Reaction Test": "reaction_test_scores"}

            def show_scores(game_file, game_name):
                file_path = os.path.join("data", game_file + ".csv")

                if not os.path.exists(file_path):
                    msb.showerror("No Data", f"No scores found for '{game_name}', please play the game to register scores")
                    return

                scores_by_user = {}

                with open(file_path, newline="\r\n") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if len(row) == 2:
                            username = row[0]
                            if game_name != "Reaction Test":
                                score = int(row[1])
                            else:
                                score = float(row[1])

                            if username not in scores_by_user:
                                scores_by_user[username] = []
                            
                            scores_by_user[username].append(score)

                for user in scores_by_user:
                    if game_name != "Reaction Test":
                        scores_by_user[user].sort(reverse=True)
                    else:
                        scores_by_user[user].sort(reverse=False)

                score_win = tk.Toplevel(root)
                score_win.title(f"Scores - {game_name}")
                score_win.geometry("350x400")
                score_win.resizable(False, False)

                tk.Label(score_win, text=f"All Scores - {game_name}", font=("Arial", 14, "bold")).pack(pady=10)

                # Display scores grouped by user
                for user in sorted(scores_by_user.keys()):
                    tk.Label(score_win, text=user, font=("Arial", 12, "bold")).pack(anchor="w", padx=20, pady=(5, 0))
                    for score in scores_by_user[user]:
                        tk.Label(score_win, text=f"   {score}", font=("Arial", 11)).pack(anchor="w", padx=40)

            root = tk.Tk()
            root.title("Game Scores Viewer")
            root.geometry("300x200")
            root.resizable(False, False)

            tk.Label(root, text="Select a game to view scores:", font=("Arial", 12, "bold")).pack(pady=10)

            for game_name, game_file in GAMES.items():
                btn = tk.Button(root, text=game_name, font=("Arial", 12),
                                command=lambda f=game_file, n=game_name: show_scores(f, n))
                btn.pack(pady=5, fill="x", padx=40)

            root.mainloop()

        high_img = ImageTk.PhotoImage(Image.open(r"assets\launcher\trophy.png"))

        high_scores = tk.Button(launcher, image=high_img, command = highscores)
        high_scores.image = high_img
        high_scores.place(relx=0.915, y=2)
        
        launcher.bind("<Configure>", resize_font)

        def on_close():
            delcurrentUser("event")
            launcher.destroy()

        launcher.protocol("WM_DELETE_WINDOW", on_close)

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
                        incorrect = msb.showerror("Error", "Incorrect password or username")
                        password_enter.delete(0, tk.END)
                        pass 
                else:
                    msb.showerror("Error", "Username does not exist, please sign up")
                    back()
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

