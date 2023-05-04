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

# Function to play the game
def play_game():
    print("Welcome to Spaceship Battle")
    print("Let's play Spaceship Battle!")
    print("Pleae input your Spaceship Name Captain: ")
    name = input()
    print("Good luck, " +name+ ".")

    print_grid()
    attempts = 0
    while True:
        row = int(input("Enter the row coordinate: "))
        col = int(input("Enter the column coordinate: "))

        if grid[row][col] == '#':
            print("Hit!")
            grid[row][col] = 'X'
            attempts += 1
            print_grid()
        elif grid[row][col] == '~':
            print("Miss!")
            grid[row][col] = 'O'
            attempts += 1
            print_grid()
        else:
            print("We are not based here, try different coordinates!")

        if attempts == sum(ship_sizes):
            print("Congratulations! You've hit and destroyed all the Space Ships!")
            break

# Start the game
place_ships()
play_game()





  