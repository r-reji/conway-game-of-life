from tkinter import ttk

# * GOAL: Simulate Conway's Game of life with OOP



# TODO: GUI buttons for start/stop/randomise/generations
# TODO: class method for reset

# ? can game class be written using the tkinter Frame class as an abstract class

class game(ttk.Frame):

    def __init__(self):
        pass

    def starting_ui(self):
        # TODO: start button
        # TODO: randomise button
        # TODO: reset button
        # TODO: generations button(s)
        pass
    
    def build_grid(self):
        # TODO: build game grid
        pass
    
    def toggle(self):
        # TODO: per cell toggle
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def simulate(self):
        # TODO: simulate n generations
        pass

    def randomise(self):
        # TODO: randomise intial conditions
        pass

if __name__ == '__main__':
    game_of_life = game()
