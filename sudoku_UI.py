import tkinter as tk 
from tkinter import filedialog, messagebox
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph_sudoku import sudoku_to_graph, color_sudoku
from main import solve_sudoku, plot_sudoku, load_sudoku_from_csv

class SudokuSolverApp:
    def __init__(self, root):       
        self.root = root
        self.root.title("Sudoku Solver GUI")
        self.filepath = None
        self.sudokus = None
        self.method = tk.StringVar(value="backtracking")

        # Ajouter les widgets à l'interface
        self.create_widgets()

    def create_widgets(self):
        # Bouton pour charger le fichier CSV
        self.load_button = tk.Button(self.root, text="Charger le fichier CSV", command=self.load_csv)
        self.load_button.pack(pady=10)

        # Boutons radio pour sélectionner la méthode de résolution
        self.method_label = tk.Label(self.root, text="Choisissez une méthode de résolution :")
        self.method_label.pack()

        self.backtracking_radio = tk.Radiobutton(self.root, text="Backtracking", variable=self.method, value="backtracking")
        self.backtracking_radio.pack()

        self.graph_coloring_radio = tk.Radiobutton(self.root, text="Coloration de Graphe", variable=self.method, value="graph_coloring")
        self.graph_coloring_radio.pack()

        # Liste déroulante pour choisir la difficulté
        self.difficulty_label = tk.Label(self.root, text="Choisissez la difficulté :")
        self.difficulty_label.pack()

        self.difficulty = tk.StringVar(value="easy")
        self.difficulty_menu = tk.OptionMenu(self.root, self.difficulty, "easy", "medium", "hard")
        self.difficulty_menu.pack(pady=10)

        # Bouton pour résoudre le Sudoku
        self.solve_button = tk.Button(self.root, text="Résoudre le Sudoku", command=self.solve_sudoku)
        self.solve_button.pack(pady=20)

    def load_csv(self):
        # Ouvre une boîte de dialogue pour sélectionner un fichier CSV
        self.filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.filepath:
            try:
                self.sudokus = load_sudoku_from_csv(self.filepath)
                messagebox.showinfo("Succès", "Fichier CSV chargé avec succès.")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors du chargement du fichier CSV : {e}")

    def solve_sudoku(self):
        if not self.sudokus:
            messagebox.showwarning("Attention", "Veuillez charger un fichier CSV d'abord.")
            return

        chosen_difficulty = self.difficulty.get()
        grid = self.sudokus[chosen_difficulty]
        n = len(grid)

        # Choisir la méthode de résolution
        start_time = time.time()
        if self.method.get() == "backtracking":
            solved = solve_sudoku(grid, n)
            duration = time.time() - start_time
        elif self.method.get() == "graph_coloring":
            G = sudoku_to_graph(grid, n)
            color_sudoku(G, grid, n)
            solved = True
            duration = time.time() - start_time

        if solved:
            messagebox.showinfo("Résolu", f"Sudoku résolu en {duration:.6f} secondes.")
            self.show_sudoku(grid, n)
        else:
            messagebox.showwarning("Non résolu", "Pas de solution trouvée pour cette grille.")

    def show_sudoku(self, grid, n):
        # Créer une nouvelle fenêtre pour afficher le Sudoku résolu
        fig, ax = plt.subplots(figsize=(6, 6))
        plot_sudoku(grid, n, title="Sudoku Résolu")

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()
