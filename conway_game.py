from tkinter import ttk
from tkinter import Tk

# * GOAL: Simulate Conway's Game of life with OOP
# ? can game class be written using the tkinter Frame class as an abstract class

class game(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.container = container

        self.grid(row = 0, column = 0)
        self.size_x = 100
        self.size_y = 100

    def starting_ui(self):
        # TODO: start/stop/reset/randomise buttons
        # * each button addressable depending on state of the game
        # TODO: generations window
        pass
    
    def build_grid(self):
        # TODO: build game grid
        pass
    
    def toggle(self):
        # TODO: per cell clickable toggle 
        pass

    def simulate(self):
        # TODO: simulate n generations
        pass

    def randomise(self):
        # TODO: randomise initial grid conditions
        pass

    def reset(self):
        # TODO: stop simulation and reset grid
        pass

    def count_neighbours(self):
        # TODO: compute number of neighbours for each valid cell
        pass

if __name__ == '__main__':
    root = Tk()
    game_of_life = game(root)
    root.mainloop()