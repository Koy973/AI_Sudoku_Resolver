# utils.py
import matplotlib.pyplot as plt
import pandas as pd
import math

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
        if index == 0:
            continue
        if index < 4:
            sudokus['easy'].append(list(row[:3]))
        elif index < 13:
            sudokus['medium'].append(list(row[:9]))
        else:
            sudokus['hard'].append(list(row[:16]))

    for key in sudokus.keys():
        sudokus[key] = [[int(cell) for cell in row] for row in sudokus[key]]

    return sudokus
