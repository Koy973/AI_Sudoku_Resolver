import pandas as pd
import matplotlib.pyplot as plt
import math

def is_valid(grid, row, col, num, n):
    sqrt_n = int(math.sqrt(n))
    start_row, start_col = sqrt_n * (row // sqrt_n), sqrt_n * (col // sqrt_n)
    
    # Vérification de la ligne et de la colonne
    if num in grid[row] or num in [grid[i][col] for i in range(n)]:
        return False
    
    # Vérification de la sous-grille √n x √n
    for i in range(start_row, start_row + sqrt_n):
        for j in range(start_col, start_col + sqrt_n):
            if grid[i][j] == num:
                return False
    
    return True

def solve_sudoku(grid, n):
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

def plot_sudoku(grid, n, title="Sudoku"):
    sqrt_n = int(math.sqrt(n))
    fig, ax = plt.subplots(figsize=(sqrt_n * 2, sqrt_n * 2))
    ax.matshow([[1 if cell == 0 else 0 for cell in row] for row in grid], cmap='Blues')

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

def import_sudoku(file_path):
    """
    Import a Sudoku grid from a CSV file.
    The CSV file should contain the grid where 0 represents empty cells.
    """
    grid = pd.read_csv(file_path, header=None).values
    n = len(grid)  # Assuming a square grid
    return grid, n

def export_sudoku(grid, file_path):
    """
    Export a solved Sudoku grid to a CSV file.
    """
    df = pd.DataFrame(grid)
    df.to_csv(file_path, header=False, index=False)

def main():
    # Prompt the user to choose difficulty level
    print("Choisissez la difficulté de la grille :")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    
    choice = int(input("Entrez votre choix (1/2/3) : "))
    
    if choice == 1:
        file_name = "easy_csv.csv"
    elif choice == 2:
        file_name = "medium_csv.csv"
    elif choice == 3:
        file_name = "hard_csv.csv"
    else:
        print("Choix invalide. Utilisation par défaut du fichier facile.")
        file_name = "easy_csv.csv"
    
    # Import the selected Sudoku grid1
    
    grid, n = import_sudoku(file_name)

    print("Grille avant résolution :")
    plot_sudoku(grid, n, title="Grille avant résolution")

    if solve_sudoku(grid, n):
        print("Grille après résolution :")
        plot_sudoku(grid, n, title="Grille après résolution")
        # Export the resolved grid to a CSV file named 'resolved.csv'
        export_sudoku(grid, "resolved.csv")
        print("Grille résolue exportée vers resolved.csv")
    else:
        print("Pas de solution trouvée.")

if __name__ == "__main__":
    main()
