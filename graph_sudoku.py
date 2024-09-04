import networkx as nx
from main import load_sudoku_from_csv, plot_sudoku

def sudoku_to_graph(grid, n):
    """
    Convertit une grille de Sudoku en un graphe avec NetworkX.
    """
    G = nx.Graph()
    nodes = [(i, j) for i in range(n) for j in range(n)]
    G.add_nodes_from(nodes)

    for i in range(n):
        for j in range(n):
            # Add edges for the same row
            for col in range(n):
                if col != j:
                    G.add_edge((i, j), (i, col))

            # Add edges for the same column
            for row in range(n):
                if row != i:
                    G.add_edge((i, j), (row, j))

            # Add edges for the same sub-grid
            sqrt_n = int(n ** 0.5)
            start_row, start_col = sqrt_n * (i // sqrt_n), sqrt_n * (j // sqrt_n)
            for row in range(start_row, start_row + sqrt_n):
                for col in range(start_col, start_col + sqrt_n):
                    if (row, col) != (i, j):
                        G.add_edge((i, j), (row, col))

    return G

def color_sudoku(graph, grid, n):
    """
    Résout une grille de Sudoku en utilisant un algorithme de coloration de graphe.
    """
    colors = nx.coloring.greedy_color(graph, strategy="largest_first")

    for (i, j), color in colors.items():
        grid[i][j] = color + 1

    return grid

if __name__ == "__main__":
    filepath = 'sudoku_grilles.csv'
    sudokus = load_sudoku_from_csv(filepath)
    
    grid = sudokus['medium']  # Choose a difficulty level (easy, medium, hard)
    n = len(grid)
    
    G = sudoku_to_graph(grid, n)
    solved_grid = color_sudoku(G, grid, n)

    plot_sudoku(solved_grid, n, title="Sudoku Résolu par Graph Coloring")