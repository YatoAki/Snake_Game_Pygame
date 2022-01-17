import pygame
import random

pygame.init()

blue = (0,0,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

dis_width = 400
dis_height = 300

snake_size = 10


clock = pygame.time.Clock()

dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake game by Yato')

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Your Score: " + str(score),True, green)
    dis.blit(value, [0,0])

def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,blue, [x[0],x[1],snake_size,snake_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width // 6, dis_height // 3])

def gameLoop():
    game_over = False
    game_close = False

    x = dis_width // 2
    y = dis_height // 2

    x_change = 0
    y_change = 0

    snake_List = []
    Length_of_snake = 1
    snake_speed = 10

    foodx = round(random.randrange(0, dis_width-snake_size) / 10.0) *10
    foody = round(random.randrange(0, dis_height-snake_size) / 10.0) *10
    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_size
                if event.key == pygame.K_SPACE:
                    snake_speed = 30
            if event.type == pygame.KEYUP:
                snake_speed = 10

        if x >= dis_width or x < 0 or y >= dis_height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        dis.fill(black)
        pygame.draw.rect(dis,green,[foodx,foody,snake_size,snake_size])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for pos in snake_List[:-1]:
            if pos == snake_Head:
                game_close = True
        our_snake(snake_size, snake_List)
        your_score(Length_of_snake - 1)
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, dis_width-snake_size) / 10.0) *10
            foody = round(random.randrange(0, dis_height-snake_size) / 10.0) *10
            Length_of_snake += 1
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()


gameLoop()
