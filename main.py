import sys
from cli import CLISimulator
from gui import GUISimulator
import tkinter as tk

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        simulator = CLISimulator()
        simulator.run()
    else:
        root = tk.Tk()
        app = GUISimulator(root)
        root.mainloop()