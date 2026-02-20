import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()

if __name__ == "__main__":
    main()