import matplotlib.pyplot as plt
import math
from utils import load_sudoku_from_csv, plot_sudoku  # Importer depuis utils.py
from graph_sudoku import sudoku_to_graph, color_sudoku  # Importer les fonctions nécessaires


def is_valid(grid, row, col, num, n):
    """
    Vérifie si un numéro peut être placé dans une cellule donnée pour une grille de taille n x n.
    """
    for i in range(n):
        if grid[row][i] == num or grid[i][col] == num:
            return False

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
    """
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 0:
                for num in range(1, n + 1):
                    if is_valid(grid, row, col, num, n):
                        grid[row][col] = num
                        if solve_sudoku(grid, n):
                            return True
                        grid[row][col] = 0
                return False
    return True




if __name__ == "__main__":
    filepath = input("Entrez le chemin du fichier CSV : ")
    sudokus = load_sudoku_from_csv(filepath)

    print("Difficultés disponibles :")
    for difficulty in sudokus.keys():
        print(f"- {difficulty}")

    chosen_difficulty = input("Choisissez une difficulté (easy, medium, hard) : ")

    if chosen_difficulty in sudokus:
        grid = sudokus[chosen_difficulty]
        n = len(grid)

        print("Méthodes de résolution disponibles :")
        print("1. Backtracking")
        print("2. Coloration de Graphe")
        method_choice = input("Choisissez une méthode (1 ou 2) : ")

        if method_choice == '1':
            print("Grille avant résolution :")
            plot_sudoku(grid, n, title=f"Grille {chosen_difficulty} avant résolution")
            if solve_sudoku(grid, n):
                print("Grille après résolution :")
                plot_sudoku(grid, n, title=f"Grille {chosen_difficulty} après résolution")
            else:
                print("Pas de solution trouvée.")
        elif method_choice == '2':
            G = sudoku_to_graph(grid, n)
            solved_grid = color_sudoku(G, grid, n)
            plot_sudoku(solved_grid, n, title=f"Grille {chosen_difficulty} après résolution (Coloration de Graphe)")
        else:
            print("Méthode non reconnue.")
    else:
        print("Difficulté non trouvée.")

