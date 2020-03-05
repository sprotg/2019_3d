import pygame
from game import Connect_four_game
from connec_four_ai import Connect_four_ai

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((1000, 600))#, pygame.FULLSCREEN)
myfont = pygame.font.SysFont("monospace", 12)
clock = pygame.time.Clock()

# Initialize game variables
done = False
game = Connect_four_game()
ai = Connect_four_ai()

x_off = 130
y_off = 130
size = 70
players = 1

# tile vars
player_colors = [(100,100,100), (255,30,30), (255,255,30)]


def draw_game():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,1000,800))
    screen.blit(myfont.render("state: {}".format(game.state), 0, (255,255,255)), (30,30))

    if 0 < game.state <= 4:
        #Draw the board
        for x in range(len(game.grid[0])):
            for y in range(len(game.grid)):
                pygame.draw.rect(screen, player_colors[game.grid[x][y]], pygame.Rect(x_off + size * x * 1.1, y_off + size * y * 1.1, size, size))
        pos = pygame.mouse.get_pos()
        if x_off <= pos[0] <= x_off + 6*(size*1.1) and y_off > pos[1]:
            x = int((pos[0] - x_off)/(size*1.1))
            pygame.draw.rect(screen, player_colors[game.turn()], pygame.Rect(x_off + size * x * 1.1, y_off + size * (-1) * 1.1, size, size))
    elif game.state == 0:
        screen.blit(myfont.render("Click to start", 0, (255,255,255)), (470,380))
        screen.blit(myfont.render("One player vs ai", 0, (255,255,255)), (170,480))
        screen.blit(myfont.render("Two players", 0, (255,255,255)), (670,480))





#Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            ai.save()
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if game.state == 0:
                if pos[0] < 500:
                    players = 1
                else:
                    players = 2
                game.state = 1

            elif game.state == 1:
                if x_off <= pos[0] <= x_off + 6*(size*1.1) and y_off > pos[1]:
                    x = int((pos[0] - x_off)/(size*1.1))
                    ai.add_data((game.grid, x))
                    game.place(x)
                    if game.win():
                        game.state = 5
                    else:
                        game.state = 3
            elif game.state == 3:
                if players == 2:
                    if x_off <= pos[0] <= x_off + 6*(size*1.1) and y_off > pos[1]:
                        x = int((pos[0] - x_off)/(size*1.1))
                        game.place(x)

                    if game.win():
                        game.state = 5
                    else:
                        game.state = 1
            elif game.state == 5:
                game.reset()
                game.state == 1
        if players == 1 and game.state == 3:
            #Make AI move
            game.place(ai.make_move(game))
            if game.win():
                game.state = 5
            else:
                game.state = 1

    draw_game()

    #pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
    pygame.display.flip()
    clock.tick(60)
