"""A tic-tac-toe game built with Python and Tkinter."""

import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple


# Define the board class
class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe -nderitunjau")  # string
        self._cells = {}
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)  # creates a frame object to hold the game display
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    # this one right here creates the grid of cells using Button objects.
    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)

                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


def main():
    """Create the game's board and run its main loop."""

    board = TicTacToeBoard()
    board.mainloop()


if __name__ == "__main__":
    main()
