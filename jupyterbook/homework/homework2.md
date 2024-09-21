# Homework 2: Building a Package for a Graphical Game of Tic-Tac-Toe

## Due: Thursday 10/19/2023

## Objective

The aim of this homework is to familiarize you with Python package management tools, specifically PyScaffold. You will use ChatGPT to create a python package for tic-tac-toe game. You will use `pyfiglet` to show who won or lost. You will include all tests and documentation in your package. You will also use Sphinx to generate documentation for your package.

To complete this homework assignment it is recommended to follow the PyScaffold Tutorial {doc}`Homework 2: Pyscaffold Tutorial            <../../topic_4_tools_for_software_development/2_pyscaffold_tutorial>`

## Prerequisites

- Python 3.x
- pip
- Virtual environment (optional, but recommended)
- PyScaffold
- pyfiglet

## Requirements

1. **Initialize the Package**: Create a new Python package using PyScaffold. The package should be named `tic-tac-toe`.

    ```bash
    putup tic_tac_toe
    ```
2. Connect to the github classroom
   
   [Github Classroom Link](https://classroom.github.com/a/6OlQnbms)

   This will create a repository for your assignment.


3. **Implement Functionality**: build a python script `tic_tac_toe` that plays the game of tic-tac-toe. It is recommended and allowed that you use ChatGPT.

4. **Comment the Code**: It is important to provide detailed inline comments. This will also help you understand your code. You can use ChatGPT to help with this, however, it is important that you understand your code. Hint: You might have to comment code on your final exam. 

5. **Add Documentation**: Integrate  `docstring` for all of the classes and functions, explaining its functionality, parameters, and return values. Add comments within the code where necessary. Use the google format. It might help to have the `autodocstring` addon.

6. **Add Requirements**: You require a package `pyfiglet` that is not included with the anaconda python distribution. Please add this to the requirements for your package. 

7. **Install the Package Locally**: Use pip to install the package locally for testing.

    ```bash
    pip install -e .
    ```

8. **Maunally Test**: Test your script to ensure it functions as expected. 
   
9. **Package Documentation**: Use Sphinx to generate documentation for your package. Provide installation instructions, function usage examples, and any dependencies. 

10. **Testing**: Add unit tests that achieve at least 80\% code coverage. 

11. **Bonus: Add to testpypi**: Create an account and publish your code to testpypi. It would not make sense to publish it to pip. 

## Turning in the Assignment

To turn in the assignment you need to connect your local repository to the remote git repository from your github classroom. Assignments are turned in when committing. 

## Assessment Criteria

- Correct package initialization and local installation (20%)
- Implementation of `tic-tac-toe` (20%)
- Quality of documentation and comments (30%)
- Presence and quality of unit tests (20%)
- Code readability and organization (10%)

Good luck!
