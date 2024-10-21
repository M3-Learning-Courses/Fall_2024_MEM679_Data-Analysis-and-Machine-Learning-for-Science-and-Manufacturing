# Homework 2: Building a Graphical Game of Minesweeper Using Pygame

## Due: Thursday 10/26/2024 by 11:59pm EST

## Objective

The objective of this homework is to introduce you to Python package management, graphical game development using `pygame`, and modern software engineering practices such as continuous integration and documentation. You will create a Python package for the classic Minesweeper game, using `pygame` for the graphical interface. This exercise emphasizes the importance of structuring code with classes, organizing it into Python files and packages, and employing tools like PyScaffold to automate project setup, testing, and documentation generation.

To complete this homework, it is recommended to follow the PyScaffold Tutorial {doc}`Homework 2: PyScaffold Tutorial            <../../topic_3/2_pyscaffold_tutorial>`

## Prerequisites

- Python 3.x
- pip
- Virtual environment (optional, but recommended)
- PyScaffold
- pygame

## Requirements

### 1. **Initialize the Package**

Create a new Python package using PyScaffold. The package should be named `minesweeper`.

```bash
putup minesweeper
```

This will scaffold the package with a standardized project structure, including directories for source code, tests, and documentation. If you create the folder first using PyScaffold, you will need to connect it to the remote repository on gitub classroom using the git remote add origin command.

### 2. **Connect to GitHub Classroom**

Use the provided [Github Classroom Link](https://classroom.github.com/a/IGMWKBA0) to create a repository for your assignment. Note, if you create the python repository first you will need to use the --force flag when calling putup.

### 3. **Implement Minesweeper Game**

Develop a Python script that implements the Minesweeper game using `pygame`. Key requirements:

- The game should have a graphical grid-based interface.
- Players should be able to left-click to reveal cells and right-click to place flags.
- The game should notify the player when they win or lose.
- The game should allow the user to set the difficulty level (e.g., number of rows, columns, and mines).
- The game should have a timer to track the player's progress.
- The game should have a reset button to start a new game.

Make use of classes to design the game's logic and user interface. For example, you may have classes such as `Cell`, `Board`, and `Game`. The use of object-oriented principles will help structure the code and make it more maintainable and testable.

### 4. **Comment the Code**

Provide detailed inline comments to explain your code. While ChatGPT can assist with this, it is important that you understand your code thoroughly. You may need to comment code on your final exam, so this will serve as good practice.

### 5. **Add Documentation**

Add `docstrings` for all classes and functions. Use the Google style for the documentation, describing the functionality, parameters, and return values of each function. This will facilitate the automatic generation of documentation.

### 6. **Add Requirements**

Add `pygame` to the package requirements, as it is not part of the standard Python distribution.

### 7. **Install the Package Locally**

Test the package locally by installing it using pip:

```bash
pip install -e .
```

This installs the package in "editable" mode, allowing you to test changes without reinstalling the package every time.

### 8. **Manual Testing**

Test your Minesweeper game to ensure all functionality works as expected. Play through the game to confirm that winning, losing, and basic interaction mechanics function correctly.

### 9. **Generate Documentation with Sphinx**

Use Sphinx to generate professional documentation for your package. The documentation should include:

- Installation instructions
- Usage examples for your Minesweeper game
- An explanation of the game's mechanics and rules

Ensure the documentation is clear and helpful for potential users and developers.

### 10. **Add Unit Tests**

Write unit tests to cover at least 80% of the codebase. Focus on testing the game logic, such as:

- Correct behavior when clicking on cells
- Winning and losing conditions
- Flagging functionality

Make sure to test edge cases such as clicking on already revealed cells or flagging all mines correctly.

### 11. **Continuous Integration (CI)**

Set up continuous integration for your package by using a service such as GitHub Actions. This will automatically run your tests and verify that the code meets the required standards whenever you push changes to your repository. Having CI in place will help you catch errors early and ensure your code is always in a working state.

### 12. **Bonus: Add to TestPyPI**

As a bonus, publish your package to TestPyPI to simulate the process of releasing a Python package. Creating an account and successfully publishing your package demonstrates that it can be installed and used by others.

## Turning in the Assignment

To submit your assignment, ensure your local repository is connected to the GitHub Classroom repository. You will turn in your assignment by committing and pushing your changes to GitHub.

## Assessment Criteria

Here’s the rubric adjusted to a 100-point scale:

| **Category**                             | **Criteria**                                                                             | **Points** | **Description**                                                                                                               |
| ---------------------------------------- | ---------------------------------------------------------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Package Initialization and Structure** | Correct use of PyScaffold to initialize package.                                         | 8          | The package is initialized correctly using PyScaffold, following a clear and organized structure.                             |
|                                          | Proper directory and file structure for Python package.                                  | 8          | The directory contains appropriate subdirectories (e.g., `src`, `tests`, `docs`) and files like `setup.py`, `README.md`, etc. |
| **Game Implementation**                  | Correct and complete functionality for Minesweeper game using `pygame`.                  | 12         | The Minesweeper game works as intended, with all essential features (grid, mines, flags, win/loss detection, etc.).           |
|                                          | Use of object-oriented programming principles, with appropriate classes.                 | 8          | Classes like `Cell`, `Board`, and `Game` are designed to structure the code logically and reduce redundancy.                  |
|                                          | Handling edge cases (e.g., clicking flagged cells, revealing all mines when lost).       | 4          | The game handles special cases without crashing or unexpected behavior.                                                       |
| **Code Comments and Documentation**      | Detailed inline comments explaining logic and code behavior.                             | 8          | Code is thoroughly commented, explaining each significant block and helping the reader understand the logic.                  |
|                                          | Proper use of docstrings in classes and functions using Google style.                    | 8          | Every class and function has appropriate docstrings describing its purpose, parameters, and return values.                    |
| **Automated Documentation with Sphinx**  | Successful generation of Sphinx documentation.                                           | 8          | Sphinx documentation is correctly generated, providing clear installation instructions, function usage, and dependencies.     |
|                                          | Includes detailed game explanation and usage examples in documentation.                  | 4          | The documentation explains how to play the game and includes working examples of how to use the code.                         |
| **Dependencies and Requirements**        | Correct inclusion of `pygame` in the `requirements.txt` file.                            | 4          | The package includes `pygame` and any other necessary dependencies, making it easy to install and run.                        |
| **Testing**                              | Unit tests achieve at least 80% code coverage.                                           | 8          | Unit tests cover the core game logic, and coverage is at least 80%.                                                           |
|                                          | Tests cover edge cases, including various game-ending scenarios (win/loss).              | 8          | Tests address different scenarios such as a win, a loss, flagging, and uncovering mines.                                      |
|                                          | Continuous integration (CI) is configured to automatically run tests.                    | 8          | CI (e.g., GitHub Actions) is set up to automatically run tests on each commit/pull request.                                   |
| **Code Readability and Organization**    | Code is logically organized into classes and functions, following Python best practices. | 4          | Code is modular, follows good design principles, and is easy to understand and modify.                                        |
|                                          | Code is clean and adheres to Python conventions (PEP 8).                                 | 4          | Code follows PEP 8 standards, with proper indentation, spacing, and variable naming conventions.                              |
| **Bonus (Optional)**                     | Package is published to TestPyPI.                                                        | 4 (Bonus)  | The package is successfully published to TestPyPI, and the process is documented in the assignment.                           |

### Total: 100 points (plus 4 bonus points)

Good luck!
