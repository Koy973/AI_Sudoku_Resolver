import matplotlib.pyplot as plt
import math

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
    ax.matshow(grid, cmap='Blues')

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


def create_empty_grid(n):
    """
    Crée une grille de Sudoku vide de taille n x n.
    
    Args:
        n (int): Taille de la grille (n x n).
        
    Returns:
        list of list: La grille de Sudoku vide.
    """
    return [[0 for _ in range(n)] for _ in range(n)]


# Exemple d'utilisation avec choix de taille de grille
def main():
    print("Choisissez la taille de la grille :")
    print("1. 4x4")
    print("2. 9x9")
    print("3. 16x16")
    
    choice = int(input("Entrez votre choix (1/2/3) : "))
    
    if choice == 1:
        n = 4
        grid = [
            [1, 0, 0, 0],
            [0, 0, 3, 4],
            [0, 0, 0, 0],
            [0, 2, 0, 0]
        ]
    elif choice == 2:
        n = 9
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
    elif choice == 3:
        n = 16
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    else:
        print("Choix invalide. Utilisation par défaut de la grille 9x9.")
        n = 9
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

    print("Grille avant résolution :")
    plot_sudoku(grid, n, title="Grille avant résolution")

    if solve_sudoku(grid, n):
        print("Grille après résolution :")
        plot_sudoku(grid, n, title="Grille après résolution")
    else:
        print("Pas de solution trouvée.")


if __name__ == "__main__":
    main()
