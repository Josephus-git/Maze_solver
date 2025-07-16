# 🐍 Python Maze Generator & Solver

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational?style=flat&logo=tcl&logoColor=white)](https://docs.python.org/3/library/tkinter.html)

## 📝 Description
This desktop application, built with Python and its standard Tkinter library, dynamically generates intricate mazes using a **recursive backtracking algorithm**. Following generation, it provides an interactive visualization of the maze being solved, demonstrating a valid path from start to finish using a **depth-first search (DFS) algorithm**.

## 🤔 Why? (Motivation/Goal)
This project was developed primarily as a practical exercise to deepen understanding and visualize two fundamental computer science algorithms: recursive backtracking for maze generation and depth-first search for pathfinding. It aims to provide an interactive and engaging way to observe these algorithms in action within a graphical user interface, making abstract concepts more concrete and accessible.

## 🚀 Quick Start

To get this maze generator and solver up and running on your local machine, follow these simple steps:

### Prerequisites
* **Python 3.x:** (Tested with Python 3.8 and newer). You can download it from [python.org](https://www.python.org/downloads/).
* **Tkinter:** Usually bundled with Python installations. If you encounter issues (e.g., "ModuleNotFoundError: No module named '_tkinter'"), you might need to install it via your operating system's package manager.
    * **Debian/Ubuntu:** `sudo apt-get install python3-tk`
    * **macOS (with Homebrew Python):** `brew install python-tk` (or `brew install python` if Tkinter is missing)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/maze_solver.git](https://github.com/your-username/maze_solver.git)
    cd maze_solver
    ```
    *(Remember to replace `https://github.com/your-username/maze_solver.git` with the actual URL of your repository.)*

2.  **No further `pip` installations are strictly required** as the project primarily relies on standard Python libraries.

### Running the Application

From the `maze_solver/` root directory:
```bash
python src/main.py
```