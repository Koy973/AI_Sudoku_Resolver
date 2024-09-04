import numpy as np
import time
from main import solve_sudoku, is_valid, load_sudoku_from_csv

def solve_sudoku_numpy(grid, n):
    """
    Résout la grille de Sudoku en utilisant l'algorithme de backtracking avec NumPy.
    """
    for row in range(n):
        for col in range(n):
            if grid[row, col] == 0:  # Trouver une cellule vide
                for num in range(1, n + 1):
                    if is_valid(grid.tolist(), row, col, num, n):
                        grid[row, col] = num  # Essayer ce numéro
                        if solve_sudoku_numpy(grid, n):
                            return True
                        grid[row, col] = 0  # Backtrack si le numéro ne convient pas
                return False
    return True

def benchmark():
    grid_sizes = ['easy', 'medium', 'hard']
    filepath = 'sudoku_grilles.csv'
    sudokus = load_sudoku_from_csv(filepath)

    for difficulty in grid_sizes:
        grid = sudokus[difficulty]
        n = len(grid)

        # Convert grid to NumPy array for NumPy benchmark
        grid_np = np.array(grid)

        # Pure Python
        start_time = time.time()
        solve_sudoku(grid, n)
        python_duration = time.time() - start_time

        # NumPy
        start_time = time.time()
        solve_sudoku_numpy(grid_np, n)
        numpy_duration = time.time() - start_time

        print(f"Performance for {difficulty} grid:")
        print(f"Pure Python: {python_duration:.6f} seconds")
        print(f"NumPy: {numpy_duration:.6f} seconds")

if __name__ == "__main__":
    benchmark()
