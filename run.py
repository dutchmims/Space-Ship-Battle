if __name__ == "__main__":
  while True:
    print("Welcome to Spaceship Battle")
    print("")
    print("")
    print("")
    print("Let's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    introScene()

import random

# Set up the game
grid_size = 15
num_ships = 5
ship_sizes = [5, 4, 3, 3, 2]

# Create the game grid
grid = [['~' for _ in range(grid_size)] for _ in range(grid_size)]

# Place the ships randomly on the grid
def place_ships():
    for size in ship_sizes:
        while True:
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                row = random.randint(0, grid_size - 1)
                col = random.randint(0, grid_size - size)
                if all(grid[row][col+i] == '~' for i in range(size)):
                    for i in range(size):
                        grid[row][col+i] = '#'
                    break
            else:  # direction == 'vertical'
                row = random.randint(0, grid_size - size)
                col = random.randint(0, grid_size - 1)
                if all(grid[row+i][col] == '~' for i in range(size)):
                    for i in range(size):
                        grid[row+i][col] = '#'
                    break
                    
# Function to print the grid
def print_grid():
    print('   ' + ' '.join(str(i) for i in range(grid_size)))
    for i in range(grid_size):
        print(str(i) + '  ' + ' '.join(grid[i]))


