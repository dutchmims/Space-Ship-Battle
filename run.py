import random

# Function to create an empty game board
def create_board():
    board = []
    for _ in range(5):
        row = ["O"] * 5
        board.append(row)
    return board

# Function to print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to randomly place the ships on the board
def place_ships(board):
    ships = []
    for _ in range(5):
        ship_row = random.randint(0, 4)
        ship_col = random.randint(0, 4)
        ship = [ship_row, ship_col]
        if ship not in ships:
            ships.append(ship)
            board[ship_row][ship_col] = "S"

# Function to get user's guess
def get_guess():
    while True:
        try:
            guess_row = int(input("Guess Row (0-4): "))
            guess_col = int(input("Guess Col (0-4): "))
            if guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
                print("Please enter a valid guess!")
            else:
                return guess_row, guess_col
        except ValueError:
            print("Please enter valid numbers for the guess!")

# Function to check if the guess hit a ship
def check_guess(guess, ships):
    if guess in ships:
        ships.remove(guess)
        return True
    else:
        return False

# Function to play the game
def play_game():
    print("Welcome to Space Ship Battle!")
    print("You have 10 attempts to destroy 5 Space Ships.")
    print("Let's Go!")
    print()
    
    player_board = create_board()
    ships = []
    place_ships(ships)
    attempts = 10
    while attempts > 0:
        print("Attempts remaining:", attempts)
        print_board(player_board)
        print()
        guess = get_guess()
        if check_guess(guess, ships):
            print("Congratulations! You hit a ship!")
            if len(ships) == 0:
                print("You sank all the ships! You win!")
                break
        else:
            print("Oops! That was a miss!")
        attempts -= 1
        print()
    
    if attempts == 0 and len(ships) > 0:
        print("Game Over! You ran out of attempts.")
        print("The remaining ships were located at:")
        for ship in ships:
            print(ship[0], ship[1])

# Run the game
play_game()
  