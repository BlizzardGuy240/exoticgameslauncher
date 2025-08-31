def run():
    import pygame
    import random
    import csv


    pygame.init()


    def restart():

        # The Screen
        global screen, clock, WIDTH
        WIDTH, HEIGHT = 800, 400
        screen = pygame.display.set_mode((WIDTH, HEIGHT))   
        caption = pygame.display.set_caption("Dino Game")
        clock = pygame.time.Clock()
        dino_img = pygame.image.load("/assets/dino_game/dino_png.png").convert_alpha()
        obs_img = pygame.image.load("/assets/dino_game/cactus.png").convert_alpha()
        cloud_img = pygame.image.load("/assets/dino_game/cloud.png").convert_alpha()
        

        # Colors and constants
        global GREY
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GREY = (50, 50, 50)
        GROUND_Y = HEIGHT - 40

        # Dino properties
        dino_w, dino_h = 100, 80
        dino_x = 50
        dino_y = GROUND_Y - dino_h
        dino_vel_y = 0
        gravity = 0.8
        jump_speed = -18
        is_jumping = False

        # Obstacle properties
        obs_w, obs_h = 50, 80
        obs_x = WIDTH
        obs_y = GROUND_Y - obs_h
        obs_speed = 6

        # Cloud properties
        cloud_w, cloud_h = 100, 60 
        cloud_x = WIDTH
        cloud_y = 50    
        cloud_speed = 0.5

        # Scaling the images
        dino_img = pygame.transform.scale(dino_img, (dino_w, dino_h))
        obs_img = pygame.transform.scale(obs_img, (obs_w, obs_h))
        cloud_img = pygame.transform.scale(cloud_img, (cloud_w, cloud_h)) 

        # Score and Font rendering
        score = 0
        global font
        font = pygame.font.Font("/assets/dino_game/PressStart2P.ttf", 12) # font properties
    
        pygame.display.flip()

        def store_score(list):
            f = open("temp_dino_scores.csv","w", newline='')
            w = csv.writer(f)
            w.writerow(list)
            del l
            f.close()

        l=[]

        global running
        running = True
        while obs_speed == 6:
            dt = clock.tick(60) / 1000  # fps = 60 (time passed in seconds since last frame) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and not is_jumping:
                        dino_vel_y = jump_speed
                        is_jumping = True

            # Update dino
            dino_vel_y += gravity
            dino_y += dino_vel_y
            if dino_y >= GROUND_Y - dino_h:
                dino_y = GROUND_Y - dino_h
                is_jumping = False
                dino_vel_y = 0

            # Update obstacle
            obs_x -= obs_speed
            if obs_x < -obs_w:
                obs_x = WIDTH + random.randint(0, 200)

            # Update cloud
            cloud_x -= cloud_speed
            if cloud_x < -cloud_x:
                cloud_x = WIDTH+10 + random.randint(0, 200)

            # Collision detection
            dino_rect = pygame.Rect(dino_x-10, dino_y-20, dino_w, dino_h)
            obs_rect = pygame.Rect(obs_x-10, obs_y, obs_w, obs_h)
                

            # Drawing
            screen.fill(WHITE)

            pygame.draw.line(screen, BLACK, (0, GROUND_Y), (WIDTH, GROUND_Y), 2)
            screen.blit(dino_img, (dino_x, dino_y))
            screen.blit(obs_img, (obs_x, obs_y))
            screen.blit(cloud_img, (cloud_x, cloud_y)) 

            # Score
            score += dt * 10
            score_surf = font.render(f"HI: {int(score)}", True, GREY)
            screen.blit(score_surf, (WIDTH - 120, 20))

            pygame.display.flip()

            # Game Over 
            if dino_rect.colliderect(obs_rect):
                game_over = False
                end = font.render(f"GAME OVER", True, GREY)
                replay = font.render(f"Press SPACE to RESTART", True, GREY)
                screen.blit(end, (WIDTH - 450, 20))
                screen.blit(replay, (WIDTH - 525, 40))

                #STORING SCORE TEMPORARILY
                l.append(int(score))

                pygame.display.flip()

                break

    restart()

    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    store_score(l)
                    restart()
                    


