import matplotlib.pyplot as plt
import math
import pandas as pd


def is_valid(grid, row, col, num, n):
    """
    Vérifie si un numéro peut être placé dans une cellule donnée pour une grille de taille n x n.

    Args:
        grid (list of list): La grille de Sudoku.
        row (int): L'indice de la ligne.
        col (int): L'indice de la colonne.
        num (int): Le numéro à placer.
        n (int): Taille de la grille (n x n).

    Returns:
        bool: True si le numéro peut être placé, False sinon.
    """
    # Vérifier la ligne
    for i in range(n):
        if grid[row][i] == num:
            return False

    # Vérifier la colonne
    for i in range(n):
        if grid[i][col] == num:
            return False

    # Vérifier la sous-grille √n x √n
    sqrt_n = int(math.sqrt(n))
    start_row, start_col = sqrt_n * (row // sqrt_n), sqrt_n * (col // sqrt_n)
    for i in range(start_row, start_row + sqrt_n):
        for j in range(start_col, start_col + sqrt_n):
            if grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid, n):
    """
    Résout la grille de Sudoku en utilisant l'algorithme de backtracking pour une grille de taille n x n.

    Args:
        grid (list of list): La grille de Sudoku à résoudre.
        n (int): Taille de la grille (n x n).

    Returns:
        bool: True si la grille est résolue, False sinon.
    """
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 0:  # Trouver une cellule vide
                for num in range(1, n + 1):
                    if is_valid(grid, row, col, num, n):
                        grid[row][col] = num  # Essayer ce numéro
                        if solve_sudoku(grid, n):
                            return True
                        grid[row][col] = 0  # Backtrack si le numéro ne convient pas
                return False
    return True


def plot_sudoku(grid, n, title="Sudoku"):
    """
    Visualise une grille de Sudoku avec Matplotlib.

    Args:
        grid (list of list): La grille de Sudoku à visualiser.
        n (int): Taille de la grille (n x n).
        title (str): Titre de la visualisation.
    """
    sqrt_n = int(math.sqrt(n))
    fig, ax = plt.subplots(figsize=(sqrt_n * 2, sqrt_n * 2))
    ax.matshow([[1 if cell == 0 else 0 for cell in row] for row in grid], cmap='Blues', alpha=0.3)

    for i in range(n):
        for j in range(n):
            c = grid[i][j]
            if c != 0:
                ax.text(j, i, str(c), va='center', ha='center')

    # Définir les lignes de la grille
    ax.set_xticks([x - 0.5 for x in range(1, n)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, n)], minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    ax.tick_params(which='minor', size=0)

    plt.xticks([])
    plt.yticks([])
    plt.title(title)
    plt.show()


def load_sudoku_from_csv(filepath):
    """
    Charge des grilles de Sudoku à partir d'un fichier CSV.

    Args:
        filepath (str): Le chemin du fichier CSV.

    Returns:
        dict: Un dictionnaire avec des clés de difficultés et des valeurs de grilles de Sudoku.
    """
    df = pd.read_csv(filepath, header=None)
    sudokus = {'easy': [], 'medium': [], 'hard': []}

    for index, row in df.iterrows():
        if index == 0:  # Skipping the header line (indices)
            continue
        if index < 4:  # First three rows are for the easy 3x3 grid
            sudokus['easy'].append(list(row[:3]))  # Only take the first 3 elements for 3x3 grid
        elif index < 13:  # Next nine rows are for the medium 9x9 grid
            sudokus['medium'].append(list(row[:9]))  # Only take the first 9 elements for 9x9 grid
        else:  # The rest are for the hard 16x16 grid
            sudokus['hard'].append(list(row[:16]))  # Take the first 16 elements for 16x16 grid

    # Convert all elements to integers
    for key in sudokus.keys():
        sudokus[key] = [[int(cell) for cell in row] for row in sudokus[key]]

    return sudokus


# Charger les grilles de Sudoku depuis le fichier CSV
filepath = input("Entrez le chemin du fichier CSV : ")
sudokus = load_sudoku_from_csv(filepath)

# Demander à l'utilisateur de choisir une difficulté
print("Difficultés disponibles :")
for difficulty in sudokus.keys():
    print(f"- {difficulty}")

chosen_difficulty = input("Choisissez une difficulté (easy, medium, hard) : ")

# Vérifier si la difficulté choisie existe et résoudre la grille
if chosen_difficulty in sudokus:
    grid = sudokus[chosen_difficulty]
    n = len(grid)  # Taille de la grille (n x n)

    print("Grille avant résolution :")
    plot_sudoku(grid, n, title=f"Grille {chosen_difficulty} avant résolution")

    if solve_sudoku(grid, n):
        print("Grille après résolution :")
        plot_sudoku(grid, n, title=f"Grille {chosen_difficulty} après résolution")
    else:
        print("Pas de solution trouvée.")
else:
    print("Difficulté non trouvée.")
