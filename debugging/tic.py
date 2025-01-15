#!/usr/bin/python3

def print_board(board):
    # Affichage du plateau avec une ligne de séparation entre chaque ligne
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:  # Empêche l'affichage de la ligne de séparation après la dernière ligne
            print("-" * 5)

def check_winner(board):
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifie les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        
        # Entrée du joueur pour la ligne et la colonne
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            # Vérification si l'entrée est dans la bonne plage
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter a number between 0 and 2.")
                continue

            # Vérification si la case est déjà occupée
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            
            # Placer le symbole du joueur sur le plateau
            board[row][col] = player

            # Vérifier si quelqu'un a gagné
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break

            # Changer de joueur
            player = "O" if player == "X" else "X"
        
        except ValueError:
            print("Invalid input. Please enter numbers only.")

tic_tac_toe()

