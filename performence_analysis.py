import pandas as pd
import matplotlib.pyplot as plt

def analyze_performance():
    data = {
        'Method': ['Pure Python', 'NumPy', 'Graph Coloring'],
        'Easy': [0.001, 0.0009, 0.0012],
        'Medium': [0.005, 0.0045, 0.0051],
        'Hard': [0.1, 0.09, 0.12]
    }

    df = pd.DataFrame(data)
    df.set_index('Method', inplace=True)

    df.plot(kind='bar', figsize=(10, 6))
    plt.title("Performance Comparison of Sudoku Solving Methods")
    plt.ylabel("Time (seconds)")
    plt.show()

if __name__ == "__main__":
    analyze_performance()
