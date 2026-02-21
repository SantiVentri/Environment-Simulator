# Libraries
import os

# Classes
from animals import Animal
from environment import Environment

# Environment settings
HEIGHT = 20
WIDTH = 50
LOGS = []

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    try:
        environment = Environment(WIDTH, HEIGHT)
        environment.display(logs=LOGS)
    except (KeyboardInterrupt, SystemExit):
        print("Exiting matrix...")
    except Exception as e:
        print("An error occured:", e)

if __name__ == "__main__":
    main()