def run():
    import time as t
    import pygame
    import random
    import sys
    import csv
    import os

    l = []

    pygame.init()
    screen = pygame.display.set_mode((650, 700))

    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 650, 700))
    pygame.display.update()
    pygame.display.set_caption("Reaction Test")

    for k in range(100, 500):
        l += [k/100]



    def lights():
        draw_board()
        for i in range(0, 600, 200):
            pygame.draw.circle(screen, (255, 0, 0), (125+i, 150), 70)
            pygame.draw.circle(screen, (255, 0, 0), (125+i, 300), 70)
            pygame.draw.circle(screen, (255, 0, 0), (125+i, 450), 70)
            if i != 0:
                t.sleep(1)
            pygame.display.update()
        t.sleep(random.choice(l))
        draw_board()
        global start
        start = t.perf_counter()
        global turn
        turn += 1   

        
    def draw_board():
        for i in range(0, 600, 200):
            pygame.draw.rect(screen, (128, 128, 128), (50+i, 50, 150, 500))
            pygame.draw.rect(screen, (0, 0, 0), (50+i, 50, 150, 500), 3)
            for j in range(150, 600, 150):
                pygame.draw.circle(screen, (0, 0, 0), (125+i, j), 70)
        pygame.display.update()

    def score(list):
        g = open("temp_reaction_scores_FINAL.csv", "w")
        g.close()
        os.remove("temp_reaction_scores_FINAL.csv")
        f = open("temp_reaction_scores.csv", "a", newline='')
        w = csv.writer(f)
        w.writerow(l2)
        f.close()
        list.clear()

    draw_board()
    l1 = []
    l2 = []
    turn = 0

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                os.rename('temp_reaction_scores.csv', 'temp_reaction_scores_FINAL.csv')
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN and turn == 0 and len(l1) == 0:
                pygame.draw.rect(screen, (255, 255, 255), (0, 500, 1000, 1000))
                lights()
                pygame.event.clear()
                l1 += [1]         
                
            elif event.type == pygame.MOUSEBUTTONDOWN and turn == 1 and len(l1) == 1:
                del l1[0]
                global end
                end = t.perf_counter()
                a = (end - start)
                time = pygame.font.SysFont("freesansbold.ttf", 100).render(str("{:.2f}".format(a*1000)) + 'ms', 1, (0, 0, 0))
                screen.blit(time, (175, 580))
                pygame.display.update()
                turn -= 1
                l2 += ["{:.2f}".format(a*1000)]
                score(l2)
