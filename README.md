# Simple Pundulum
This project simulates the motion of a simple pendulum using Python and matplotlib. It includes a graphical user interface (GUI) built with tkinter to allow users to input values for the gravitational constant and pendulum length before running the simulation.

<hr>

## Features
- Interactive GUI to input values for gravitational constant g and pendulum length L.
- Visual animation of the pendulum's motion.
- Easy setup with detailed instructions on creating an executable version of the program.

## Requirements
Before running the program, ensure that you have the following dependencies installed:

- matplotlib
- tkinter (comes pre-installed with Python on most platforms)
- scipy
- numpy
- pyinstaller (optional, for creating an executable)<br>

You can install all the required libraries via pip:

```
pip install matplotlib tkinter scipy numpy pyinstaller
```

## Usage
1. <b>Running the Program:</b>

    To run the program, simply execute main.py. A window will pop up asking for input values for the gravitational constant (g) and the pendulum length (L). Default values are provided if no input is given.<br>
    To run the script:

    ```
    py main.py
    ```

2. <b>Creating an Executable:</b>

    If you want to create a standalone executable (so the program can run on systems without Python installed), you can use pyinstaller.

    To create an executable for the program, follow the steps below:<br>
    In your virtual environment terminal:

    ```
    pyinstaller --onefile --windowed main.py
    ```
    - `onefile`: This bundles everything into a single executable file.
    - `windowed`: This prevents a terminal window from opening alongside the GUI (for GUI apps).

## How to use
1. After running the program or executable, a GUI will prompt you to enter the gravitational constant and the pendulum length.
2. If no values are entered, default values (g = 9.81 m/s² and L = 1.0 meters) will be used.
3. The pendulum simulation will be displayed after entering the inputs and clicking "OK".
### Example:
- Gravitational Constant (g): Enter 9.81 for Earth's gravity.
- Pendulum Length (L): Enter 1.0 for a pendulum of 1 meter in length.

Once the inputs are provided, the pendulum motion will be simulated, and you can observe the motion in real-time.