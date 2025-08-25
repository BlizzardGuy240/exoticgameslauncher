def run():
    from itertools import cycle
    from random import randrange
    from tkinter import Canvas, Tk, messagebox, font, simpledialog
    import csv

    canvas_width = 800
    canvas_height = 400

    root = Tk()
    root.title("Egg Catcher")
    c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue")
    c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill="sea green", width=0)
    c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
    c.pack()

    color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"])
    catcher_color = "blue"

    # difficulty variables
    egg_width = 0
    egg_speed = 0
    egg_interval = 0
    catcher_width = 0
    score_multiplier = 1
    game_active = True  # Track if the game is active

    # Store after call IDs
    egg_timer_id = None
    move_timer_id = None
    catch_timer_id = None

    # Difficulty settings
    difficulty_levels = {
        1: {"egg_width": 45, "egg_interval": 3000, "egg_speed": 500, "catcher_width": 100, "score_multiplier": 1},
        2: {"egg_width": 40, "egg_interval": 2500, "egg_speed": 450, "catcher_width": 90, "score_multiplier": 1.2},
        3: {"egg_width": 35, "egg_interval": 2000, "egg_speed": 400, "catcher_width": 80, "score_multiplier": 1.5},
        4: {"egg_width": 30, "egg_interval": 1500, "egg_speed": 350, "catcher_width": 70, "score_multiplier": 1.8},
        5: {"egg_width": 25, "egg_interval": 1000, "egg_speed": 300, "catcher_width": 60, "score_multiplier": 2},
    }

    game_font = font.nametofont("TkFixedFont")
    game_font.config(size=18)

    score = 0
    score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: 0")

    lives_remaining = 3
    lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text=f"Lives: {lives_remaining}")

    eggs = []
    catcher = None

    def setup_game(level):
        global egg_width, egg_speed, egg_interval, catcher_width, catcher, score_multiplier
        global egg_timer_id, move_timer_id, catch_timer_id
        
        if level in difficulty_levels:
            settings = difficulty_levels[level]
            egg_width = settings["egg_width"]
            egg_interval = settings["egg_interval"]
            egg_speed = settings["egg_speed"]
            catcher_width = settings["catcher_width"]
            score_multiplier = settings["score_multiplier"]
            
            # catcher
            catcher_startx = canvas_width / 2 - catcher_width / 2
            catcher_starty = canvas_height - 120
            catcher_endx = catcher_startx + catcher_width
            catcher_endy = catcher_starty + 20
            
            if catcher:
                c.delete(catcher)
            catcher = c.create_arc(catcher_startx, catcher_starty, 
                                catcher_endx, catcher_endy, 
                                start=200, extent=140, 
                                style="arc", outline=catcher_color, width=3)
            
            # Start game
            c.focus_set()
            egg_timer_id = root.after(1000, create_egg)
            move_timer_id = root.after(1000, move_eggs)
            catch_timer_id = root.after(1000, check_catch)
        else:
            messagebox.showerror("Error", "Invalid difficulty level")
            root.destroy()

    def create_egg():
        global egg_timer_id
        
        if not game_active:
            return
        
        x = randrange(10, canvas_width - egg_width - 10)
        new_egg = c.create_oval(x, 40, x+egg_width, 40+55, fill=next(color_cycle), width=0)
        eggs.append(new_egg)
        if game_active:
            egg_timer_id = root.after(egg_interval, create_egg)

    def move_eggs():
        global move_timer_id
        
        if not game_active:
            return
        
        for egg in eggs[:]:
            try:
                (eggx, eggy, eggx2, eggy2) = c.coords(egg)
                c.move(egg, 0, 10)
                if eggy2 > canvas_height:
                    egg_dropped(egg)
            except:
                # Canvas might be destroyed, just break out of the loop
                break
        
        if game_active:
            move_timer_id = root.after(egg_speed, move_eggs)

    def egg_dropped(egg):
        global lives_remaining, game_active, egg_timer_id, move_timer_id, catch_timer_id
        
        try:
            eggs.remove(egg)
            c.delete(egg)
            lives_remaining -= 1
            c.itemconfigure(lives_text, text=f"Lives: {lives_remaining}")
            
            if lives_remaining <= 0:
                game_active = False
                # Cancel all scheduled events
                if egg_timer_id:
                    root.after_cancel(egg_timer_id)
                if move_timer_id:
                    root.after_cancel(move_timer_id)
                if catch_timer_id:
                    root.after_cancel(catch_timer_id)
                
                messagebox.showinfo("Game Over!", f"Final Score: {score}")
                
                #STORING SCORES TEMPORARILY
                f = open("temp_egg_scores.csv", "w", newline='')
                w = csv.writer(f)
                w.writerow([score])
                f.close()

                root.destroy()
        except:
            # If canvas is already destroyed, just proceed with cleanup
            game_active = False

    def check_catch():
        global catch_timer_id
        
        if not game_active:
            return
        
        global score
        if catcher:
            try:
                (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
                for egg in eggs[:]:
                    (eggx, eggy, eggx2, eggy2) = c.coords(egg)
                    if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
                        score += int(10 * score_multiplier)
                        c.itemconfigure(score_text, text=f"Score: {score}")
                        eggs.remove(egg)
                        c.delete(egg)
            except:
                # Canvas might be destroyed, don't proceed
                return
        
        if game_active:
            catch_timer_id = root.after(100, check_catch)

    def move_left(event):
        if catcher and game_active:
            try:
                (x1, y1, x2, y2) = c.coords(catcher)
                if x1 > 0:
                    c.move(catcher, -20, 0)
            except:
                pass

    def move_right(event):
        if catcher and game_active:
            try:
                (x1, y1, x2, y2) = c.coords(catcher)
                if x2 < canvas_width:
                    c.move(catcher, 20, 0)
            except:
                pass

    # controls
    c.bind("<Left>", move_left)
    c.bind("<Right>", move_right)
    c.bind("<a>", move_left)
    c.bind("<d>", move_right)

    # difficulty selection
    level = simpledialog.askinteger("Difficulty", 
                                "Choose difficulty (1-5):\n1 = Easy (slow eggs, big basket)\n5 = Hard (fast eggs, small basket)", 
                                minvalue=1, maxvalue=5)
    if level:
        setup_game(level)
    else:
        messagebox.showinfo("Info", "Please select a difficulty to start the game")
        root.destroy()

    root.mainloop()
