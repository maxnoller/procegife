from gui import Gui
from simulation import Simulation

class Procegife:
    def __init__(self):
        self.gui = Gui()
        self.simulation = Simulation()
        self.run = True

    def run(self):
        """Run the game main loop updating simulation and representation"""
        while self.run:
            self.simulation.update()
            self.gui.update()

#Only gets called when the procegife file gets called directly and not when imported
if __name__ == "__main__":
    procegife = Procegife()
    procegife.run()