import os
import time
import random

# Terminal configuration
WIDTH, HEIGHT = 40, 15
LOGO = "DVD"

# Initial state
x, y = random.randint(1, WIDTH - 4), random.randint(1, HEIGHT - 2)
dx, dy = 1, 1

try:
    while True:
        # Move logo
        x += dx
        y += dy

        # Bounce off walls
        if x <= 0 or x >= WIDTH - len(LOGO):
            dx *= -1
        if y <= 0 or y >= HEIGHT - 1:
            dy *= -1

        # Render frame
        grid = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
        for i, char in enumerate(LOGO):
            if 0 <= y < HEIGHT and 0 <= x + i < WIDTH:
                grid[y][x + i] = char

        # Clear screen and print
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n".join("".join(row) for row in grid))
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nAnimation stopped!")
