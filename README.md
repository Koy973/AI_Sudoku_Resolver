# Projet_Sudoku_python_b2


il manque le debug de la fonction graph pour le couleur et de faire interface graphique
power point

# Sudoku Solver Project

This project implements a Sudoku solver with various methods, including backtracking and graph coloring. It also includes performance benchmarking between pure Python and NumPy implementations, as well as visualizations to illustrate the solving process.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
  - [1. Solving Sudoku](#1-solving-sudoku)
  - [2. Benchmarking](#2-benchmarking)
  - [3. Graph Representation and Coloring](#3-graph-representation-and-coloring)
  - [4. Visualizations](#4-visualizations)
  - [5. Performance Analysis](#5-performance-analysis)
- [Example Grids](#example-grids)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project provides a comprehensive Sudoku solver, which can:
- Solve Sudoku puzzles using a backtracking algorithm.
- Represent Sudoku as a graph and solve it using a graph coloring algorithm.
- Compare the performance of different solving techniques using pure Python and NumPy.
- Visualize the solving process both statically and interactively.
- Analyze the performance of different solving methods.

## Project Structure

```
├── benchmark.py # Benchmarking the performance of different Sudoku solvers
├── graph_sudoku.py # Solving Sudoku using graph representation and coloring
├── main.py # Core Sudoku solving logic with backtracking
├── performance_analysis.py # Analyzing and visualizing performance results
├── visualization.py # Static and interactive visualizations of the solving process
├── sudoku_grilles.csv # Example Sudoku grids for testing (easy, medium, hard)
└── README.md # Project documentation (this file)
```

## Setup and Installation

### Requirements

- Python 3.7 or higher
- Install the required Python packages:

```bash
pip install matplotlib pandas numpy networkx
```
```bash
pip install r requirements.txt
```

## Files

- **`main.py`**: The core script that contains the Sudoku solver using a backtracking algorithm, as well as functions for loading grids from a CSV file and visualizing them.
- **`benchmark.py`**: Script to benchmark the performance of the Sudoku solver using pure Python vs. NumPy.
- **`graph_sudoku.py`**: Script to represent the Sudoku grid as a graph using NetworkX and solve it using a graph coloring algorithm.
- **`visualization.py`**: Script for creating static and interactive visualizations of the Sudoku solving process.
- **`performance_analysis.py`**: Script to analyze and visualize the performance results of different Sudoku solving methods.
- **`sudoku_grilles.csv`**: A CSV file containing Sudoku puzzles of different difficulties (easy, medium, hard).

## Usage

### 1. Solving Sudoku

You can solve Sudoku puzzles using the `main.py` file. This script will prompt you to load a Sudoku grid from a CSV file, select a difficulty, and solve the puzzle.

```bash
python main.py
```
### 2. Benchmarking

To compare the performance between pure Python and NumPy implementations, use the `benchmark.py` script:

```bash
python benchmark.py
```
This script will execute the Sudoku solver using both pure Python and NumPy-based methods across different grid sizes (3x3, 9x9, 16x16). It will output the time taken to solve puzzles of different difficulties using both methods, allowing you to compare their efficiency.

### 3. Graph Representation and Coloring

To solve a Sudoku puzzle using a graph coloring algorithm, run the `graph_sudoku.py` script:

```bash
python graph_sudoku.py
```
This script converts the Sudoku grid into a graph using the NetworkX library. Each cell in the grid is represented as a node, and edges are created between nodes that correspond to cells that cannot have the same number (i.e., cells in the same row, column, or sub-grid). The graph coloring algorithm is then used to solve the Sudoku puzzle by assigning colors (numbers) to nodes (cells) such that no two adjacent nodes share the same color.
### 4. Visualizations

You can visualize the solving process either statically or interactively:

- **Static Visualization**: The initial and solved Sudoku grids can be visualized using the `plot_sudoku` function in `main.py`. The grids are displayed using Matplotlib, with numbers placed in their respective cells. This visualization helps you see the Sudoku grid before and after the solving process.

- **Interactive Visualization**: To observe the backtracking process in real-time, run the `visualization.py` script:

```bash
python visualization.py
```
This script provides an animated view of the backtracking algorithm as it solves the Sudoku puzzle. You can watch how the solver attempts to fill in the grid step-by-step, backtracks when necessary, and eventually finds a solution.
### 5. Performance Analysis

To analyze and compare the performance of different Sudoku solving techniques, use the `performance_analysis.py` script:

```bash
python performance_analysis.py
```
This script generates performance graphs that compare the time taken by the pure Python and NumPy implementations to solve Sudoku grids of various sizes and difficulties. The results are visualized using Matplotlib, allowing you to easily see which method is more efficient for different grid sizes and complexities.

The analysis will help you understand the trade-offs between using pure Python code versus leveraging NumPy for solving Sudoku puzzles, particularly as grid size increases.
## Example Grids

The project includes a CSV file (`sudoku_grilles.csv`) with Sudoku grids of varying difficulties:

- **Easy**: A 3x3 grid.
- **Medium**: A 9x9 grid.
- **Hard**: A 16x16 grid.

These grids can be used to test the solver across different levels of complexity. Each grid size presents its own challenges, allowing you to evaluate the solver's performance and accuracy under various conditions.

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## Power Point
lien du canva : https://www.canva.com/design/DAGPyJdXgVM/11hRjgaMYOdU6W-emcmSMw/edit?utm_content=DAGPyJdXgVM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
