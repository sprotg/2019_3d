import pygame
from game import Game

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))#, pygame.FULLSCREEN)
myfont = pygame.font.SysFont("monospace", 12)
clock = pygame.time.Clock()

# Initialize game variables
done = False
game = Game()
current_tile = (3,3)
effects = []

# tile vars
tile_colors = [(0,0,0), (255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255)]
tile_offset = [280,530]
tile_size = [50,50]


def draw_game():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,800,600))
    if current_tile is not None:
        t = abs((pygame.time.get_ticks() % 512) - 256) % 256
        c = (t,t,t)
        pygame.draw.rect(screen, c, pygame.Rect(tile_offset[0] + current_tile[0]*tile_size[0] - 3, tile_offset[1] - (current_tile[1]+1)*tile_size[1] - 3, tile_size[0], tile_size[1]))
    screen.blit(myfont.render("{} points".format(game.points), 0, (255,255,255)), (50,50))
    for y in range(0,len(game.grid)):
        for x in range(0,len(game.grid[y])):
            if game.anim[x][y] > 0:
                game.anim[x][y] -= 1
                if game.anim[x][y] == 0:
                    dp = game.detect_matches(True)
                    if dp > 0:
                        effects.append(["+{}".format(dp), 100, cell_to_pixels(x,y)])
            pygame.draw.rect(screen, tile_colors[game.grid[x][y]], pygame.Rect(tile_offset[0] + x*tile_size[0], tile_offset[1] - (y+1)*tile_size[1] - game.anim[x][y], tile_size[0]-5, tile_size[1]-5))
    for e in effects:
        if e[1] > 0:
            e[1] -= 1
            pygame.draw.rect(screen, (200,200,200),pygame.Rect(e[2][0],e[2][1], 20,20))
            screen.blit(myfont.render(e[0], 0, (255,255,255)), (e[2][0],e[2][1]))

def pixels_to_cell(x,y):
    x1 = int((x - tile_offset[0])/tile_size[0])
    y1 = int((-y + tile_offset[1])/tile_size[1])
    return x1,y1

def cell_to_pixels(x,y):
    x1 = int(tile_offset[0] + x * tile_size[0])
    y1 = int(tile_offset[1] - y * tile_size[1])
    return x1,y1

def output_logic(tilstand):
    if tilstand == 1:
        draw_game()
    elif tilstand == 0:
        draw_menu()

def draw_menu():
    pass

tilstand = 0

#Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
        if tilstand == 0:
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                tilstand = 1
        elif tilstand == 1:
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                tilstand = 0



        #Håndtering af input fra mus
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x_cell, y_cell = pixels_to_cell(pos[0],pos[1])
            print(pos, cell_to_pixels(x_cell,y_cell))
            if 0 <= x_cell < len(game.grid) and 0 <= y_cell < len(game.grid[0]):
                if current_tile is None:
                    current_tile = (x_cell, y_cell)
                else:
                    game.swap_tiles(x_cell, y_cell, current_tile[0], current_tile[1])

                    #Når der er byttet brikker, kan vi kontrollere om der er lavet et match
                    dp = game.detect_matches()
                    if dp > 0:
                        effects.append(["+{}".format(dp), 100, cell_to_pixels(current_tile[0], current_tile[1])])
                    current_tile = None

    output_logic(tilstand)

    #pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
    pygame.display.flip()
    clock.tick(60)
