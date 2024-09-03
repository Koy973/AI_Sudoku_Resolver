import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from main import plot_sudoku, solve_sudoku, load_sudoku_from_csv

def interactive_sudoku(grid, n):
    """
    Visualisation interactive du processus de résolution d'un Sudoku.
    """
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        plot_sudoku(grid, n)
        if not solve_sudoku(grid, n):
            return

    ani = FuncAnimation(fig, update, frames=range(1, 100), repeat=False)
    plt.show()

if __name__ == "__main__":
    filepath = 'sudoku_grilles.csv'
    sudokus = load_sudoku_from_csv(filepath)
    
    grid = sudokus['easy']  # Choose a difficulty level (easy, medium, hard)
    n = len(grid)
    
    interactive_sudoku(grid, n)
