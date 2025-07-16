# 🐍 Python Maze Generator & Solver

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational?style=flat&logo=tcl&logoColor=white)](https://docs.python.org/3/library/tkinter.html)

## 📝 Description
This desktop application, built with Python and its standard Tkinter library, dynamically generates intricate mazes using a **recursive backtracking algorithm**. Following generation, it provides an interactive visualization of the maze being solved, demonstrating a valid path from start to finish using a **Depth-First Search (DFS) algorithm**.

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
    git clone https://github.com/Josephus-git/Maze_solver.git
    cd maze_solver
    ```

2.  **No further `pip` installations are strictly required** as the project primarily relies on standard Python libraries.

### Running the Application

From the `maze_solver/` root directory:
```bash
python3 src/main.py
```

## 💡 Usage
Once the application window appears:
1. **Observe Maze Generation**: The application will first display the maze being generated dynamically, step-by-step, using an animated process. Walls will be removed as the algorithm explores.

2. **Solve the Maze**: After the maze generation is complete, a "Solve Maze" button will appear at the bottom center of the window. Click this button to initiate the maze-solving algorithm.

3. **Watch the Solution**: The application will then animate the depth-first search algorithm as it finds a path from the top-left cell (start) to the bottom-right cell (exit) of the maze.

   * **Red lines** indicate forward progress along the potential solution path.
   * **Grey lines** indicate backtracking when a dead end is reached.
  
## 🎬 Video
https://github.com/user-attachments/assets/5338cc2d-7885-411f-ab7f-98d98cf9804a

## 🤝 Contributing
Contributions are always welcome! If you have suggestions for improvements, new features, or bug fixes, please consider contributing.
1. Fork the repository on GitHub.
   
2. Create a new branch for your feature or bug fix:

   ```
   git checkout -b feature/your-feature-name
   ```
   (or bugfix/fix-description for bug fixes).

3. Make your changes. Ensure your code adheres to the existing style and conventions.

4. Write or update tests for your changes.

5. Commit your changes with a clear, concise, and descriptive message (e.g., `feat: Add option for different maze sizes`, `fix: Correct wall drawing bug`).

Push your branch to your forked repository:
```
git push origin feature/your-feature-name
```
Open a Pull Request against the main branch of this repository. Please describe your changes in detail in the PR description.






