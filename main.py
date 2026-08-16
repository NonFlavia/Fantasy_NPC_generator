import tkinter as tk
from gui import NPCGeneratorGUI


def main() -> None:
    root = tk.Tk()
    NPCGeneratorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
