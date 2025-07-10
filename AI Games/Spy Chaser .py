import pygame, time
from queue import PriorityQueue

# Constants
WIDTH, ROWS, TIME_LIMIT = 400, 10, 20
CELL = WIDTH // ROWS
pygame.init()
win = pygame.display.set_mode((WIDTH, WIDTH + 50))
pygame.display.set_caption("Spy vs Chaser")

# Colors and Fonts
WHITE, BLACK, GREEN, RED, BLUE = (255,255,255), (0,0,0), (0,255,0), (255,0,0), (0,0,255)
font = pygame.font.SysFont('Arial', 24)
clock = pygame.time.Clock()

# Positions
spy, chaser = [0, 0], [ROWS - 1, ROWS - 1]

# Drawing the grid and UI
def draw(spy_score, chaser_score, time_left):
    win.fill(BLACK)
    for i in range(ROWS):
        for j in range(ROWS):
            color = GREEN if [i,j] == spy else RED if [i,j] == chaser else WHITE
            pygame.draw.rect(win, color, (j*CELL, i*CELL, CELL, CELL))
            pygame.draw.rect(win, BLACK, (j*CELL, i*CELL, CELL, CELL), 1)
    pygame.draw.rect(win, BLACK, (0, WIDTH, WIDTH, 50))
    win.blit(font.render(f"Spy: {spy_score}", True, BLUE), (10, WIDTH + 10))
    win.blit(font.render(f"Chaser: {chaser_score}", True, BLUE), (150, WIDTH + 10))
    win.blit(font.render(f"Time: {int(time_left)}s", True, BLUE), (300, WIDTH + 10))
    pygame.display.update()

# Valid neighbor cells
def neighbors(pos):
    x, y = pos
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < ROWS and 0 <= ny < ROWS:
            yield (nx, ny)

# A* Pathfinding
def a_star(start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from, cost_so_far = {}, {start: 0}

    while not frontier.empty():
        _, current = frontier.get()
        if current == goal:
            break
        for next in neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + abs(goal[0]-next[0]) + abs(goal[1]-next[1])
                frontier.put((priority, next))
                came_from[next] = current

    path, current = [], goal
    while current != start:
        if current in came_from:
            path.append(current)
            current = came_from[current]
        else:
            return []
    path.reverse()
    return path

# Main game loop
def main():
    spy_score, chaser_score = 0, 0
    run_game = True

    while run_game:
        spy[:], chaser[:] = [0, 0], [ROWS - 1, ROWS - 1]
        ai_counter = 0
        start_time = time.time()
        round_active = True

        while round_active:
            clock.tick(30)
            time_left = max(0, TIME_LIMIT - (time.time() - start_time))

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run_game = False
                    round_active = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and spy[0] > 0: spy[0] -= 1
            if keys[pygame.K_DOWN] and spy[0] < ROWS - 1: spy[0] += 1
            if keys[pygame.K_LEFT] and spy[1] > 0: spy[1] -= 1
            if keys[pygame.K_RIGHT] and spy[1] < ROWS - 1: spy[1] += 1

            ai_counter += 1
            if ai_counter >= 10:
                path = a_star(tuple(chaser), tuple(spy))
                if path:
                    chaser[0], chaser[1] = path[0]
                ai_counter = 0

            draw(spy_score, chaser_score, time_left)

            if chaser == spy:
                chaser_score += 1
                round_active = False
            if time_left <= 0:
                spy_score += 1
                round_active = False

        # Show round result
        win.fill(BLACK)
        result = "Spy Wins!" if spy_score > chaser_score else "Chaser Wins!" if chaser_score > spy_score else "It's a Tie!"
        text = font.render(result, True, GREEN if "Spy" in result else RED if "Chaser" in result else WHITE)
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, WIDTH // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(2000)

    pygame.quit()

main()
