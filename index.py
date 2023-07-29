import random

import pygame

width = 800
height = 900
blockSize = 30

O = [['.....',
      '.00..',
      '.00..',
      '.....',
      '.....']]

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
L = [['....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
shapes = [S, I ,Z, L, O ,J , T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


pygame.font.init()

def draw_text_middle(window):
    font = pygame.font.SysFont("comicsans", 30, bold=True) #TODO
    label = font.render("Welcome to Tetris!", 1, (255, 255, 255)) #TODO: set color of the font
    window.blit(label, (280,300 )) #TODO

def create_grid(locked_positions = {}):
    #Create 2D list filled with 5 , row = 100, col=10
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)] # matrix with 10 columns and 20 rows
    # TODO: outer loop for rows and inner loop for columnf -> grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c

    return grid

def get_piece():
    return Piece(5, 0, random.choice(shapes))

def draw_grid(window, grid):
    #nested for loops
    #pygame.draw.line()
    #outer for loop: (row)
    # pygame.draw.line(surface , color , starting position, end position)
    #innter for loops: (column)

    for i in range(len(grid)): # 20 times
        pygame.draw.line(window,
                         (128, 128, 128), #color (RGB)
                         (200, 100 + i * blockSize),
                         # ending position (x,y)
                         (500, 100 + i * blockSize)
                         )
        #TODO: 숙제로 진행해주세요요
        for j in range(len(grid[i])):
            pygame.draw.line(window,
                             (128, 128, 128),  # color (RGB)
                             (200 + j * blockSize, 100 ),
                             # ending position (x,y)
                             (200 + j * blockSize, 700)
                             )

def draw_shape(piece):

    #TODO: get the shape from piece
    shape = piece.shape

    #TODO: get the rotation from piece
    rotation = piece.rotation

    format = shape[rotation % len(shape)]

    positions = []
    #['.....', '.....', '..00.', '.00..', '.....']
    for i in range(len(format)):
        row = list(format[i])

        for j in range(len(row)):
            if( row[j] == "0"):
                positions.append((piece.x + j, piece.y + i))
            #TODO: compare if it equals "0" if it is print("HELLO)
            # ['.', '0', '.', '.', '.']
    for i , pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions

def draw_window(window, grid):
    #TODO: 새로운 window의 배경 색을 넣어주세요~
    window.fill((0, 0, 0))
    #TODO: Tetris 문구를 window 맨 상단에 띄어주세요~
    font = pygame.font.SysFont("comicsans", 30, bold=True)  # TODO
    label = font.render("Tetris!", 1, (255, 255, 255))  # TODO: set color of the font
    window.blit(label, (350, 50))

    #10 columns, 20 rows
    #for loops (outer ,inner loops) . print("Hello")
    #TODO: outer loop for rows and inner loop for columns. print("Hello") -> grid (matrix)
    # [[ 1, 2, 3],
    #  [4, 5 ,6,],
    #  [7, 8, 9]]
    for i in range(len(grid)): #row
        for j in range(len(grid[i])): #column
            #TODO: draw rectangle for tetris shape
            pygame.draw.rect(
                window,
                grid[i][j],
                (200 + j * blockSize,
                 100 + i * blockSize,
                 blockSize,
                 blockSize),
                0
            )

    pygame.draw.rect(window,
                     (128, 128, 128),#color of border > RGB
                     (200, 100,300, 600), #starting x, starting y, grid's width, grids'height
                      5) #thickness of border
    draw_grid(window, grid)

def draw_next_shape(window, piece):
    #TODO: Put a label "Next Shape" on the right hand side of the grid

    font = pygame.font.SysFont("comicsans", 30, bold=True)  # TODO
    label = font.render("Next Shape", 1, (255, 255, 255))  # TODO: set color of the font

    shape = piece.shape
    rotation = piece.rotation
    format = shape[rotation % len(shape)]
    #TODO: use outer and inner loops to draw the shape
    for i in range(len(format)):
        row = list(format[i])

        for j in range(len(row)):
            if( row[j] == "0"):
                # TODO: draw rectanble shape for tetris piece
                pass

    window.blit(label, (550, 350))



def main(window):
    locked_positions = {}
    grid = create_grid(locked_positions)
    current_shape = get_piece()
    next_shape = get_piece()

    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0

    run = True
    while (run):
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/ 1000 > 5 :
            level_time = 0

            if level_time > 0.12:
                level_time -= 0.005

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_shape.y += 1



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    current_shape.y += 1
                if event.key == pygame.K_UP:
                    current_shape.rotation += 1
                if event.key == pygame.K_LEFT:
                    current_shape.x -= 1
                if event.key == pygame.K_RIGHT:
                    current_shape.x += 1
        current_piece_position = draw_shape(current_shape)
        for i in range(len(current_piece_position)):
            x, y = current_piece_position[i]
            if y >= 0:
                grid[y][x] = current_shape.color
        draw_window(window, grid)
        draw_next_shape(window, next_shape)
        pygame.display.update()

def main_menu(window):
    run = True
    while(run): #RGB : red green blue
        window.fill((0,0,0))
        draw_text_middle(window)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(window)
    pygame.display.quit()



window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")
main_menu(window)
