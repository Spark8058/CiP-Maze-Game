import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 430
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Maze Game')

# Load images
wall_image = pygame.image.load('wall.jpg')
floor_image = pygame.image.load('floor.png')
player_image = pygame.image.load('player1.png')
exit_image = pygame.image.load('exit.png')

# Resize images to fit the tile size
TILE_SIZE = 40
wall_image = pygame.transform.scale(wall_image, (TILE_SIZE, TILE_SIZE))
floor_image = pygame.transform.scale(floor_image, (TILE_SIZE, TILE_SIZE))
player_image = pygame.transform.scale(player_image, (TILE_SIZE, TILE_SIZE))
exit_image = pygame.transform.scale(exit_image, (TILE_SIZE, TILE_SIZE))

# Maze layout: 0 = floor, 1 = wall, 2 = player start, 3 = exit
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Find player starting position
player_x, player_y = [(x, y) for y, row in enumerate(maze) for x, tile in enumerate(row) if tile == 2][0]

# Function to draw the maze
def draw_maze():
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            if tile == 1:
                window.blit(wall_image, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 0:
                window.blit(floor_image, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 3:
                window.blit(exit_image, (x * TILE_SIZE, y * TILE_SIZE))

# Function to display text
def display_text(text, color, size, position):
    font = pygame.font.Font(None, size)
    surface = font.render(text, True, color)
    window.blit(surface, position)

start_time = time.time()

# Game loop
running = True
won = False
while running:
    elapsed_time = time.time() - start_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            new_x, new_y = player_x, player_y
            if event.key == pygame.K_LEFT:
                new_x -= 1
            elif event.key == pygame.K_RIGHT:
                new_x += 1
            elif event.key == pygame.K_UP:
                new_y -= 1
            elif event.key == pygame.K_DOWN:
                new_y += 1
            # Check for walls
            if maze[new_y][new_x] != 1:
                player_x, player_y = new_x, new_y
                # Check for win
                if maze[player_y][player_x] == 3:
                    won = True

    # Draw the maze and player
    window.fill((0, 0, 0))
    draw_maze()
    window.blit(player_image, (player_x * TILE_SIZE, player_y * TILE_SIZE))

    elapsed_seconds = int(elapsed_time)
    display_text(f"Time: {elapsed_seconds} s", (255, 255, 255), 36, (10, 10))

    # Check win condition
    if won:
        total_time = elapsed_seconds
        display_text(f"You won in {total_time} seconds!", (255, 0, 0), 50, (width // 4 - 50, height // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
