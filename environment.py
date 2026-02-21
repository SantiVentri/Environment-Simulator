# Helpers
from helpers import clear_screen

class Environment:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.animals = []
        self.plants = []

    def display(self, logs):
        """Displays the current state of the environment."""
        # Clear the screen
        clear_screen()

        # Create empty grid
        grid = [["  " for _ in range(self.width)] for _ in range(self.height)]

        # Display animal and plant icons in their current position
        for plant in self.plants:
            grid[plant.pos_y][plant.pos_x] = plant.icon

        for animal in self.animals:
            grid[animal.pos_y][animal.pos_x] = animal.icon

        # Print title
        print("==" * self.width)
        print("🌱 ENVIRONMENT SIMULATOR 🌱".center(self.width * 2))
        print("==" * self.width)

        # Print grid
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += grid[y][x]
            print(row)

        # Display Logs
        for log in logs[-5:]:
            print(log)

    def add_animals(self, animals):
        """Adds a list of animals to the environment with valid positions."""
        import random
        
        # Collect occupied positions by existing animals and plants
        occupied_positions = []

        for animal in self.animals:
            occupied_positions.append((animal.pos_x, animal.pos_y))

        for plant in self.plants:
            occupied_positions.append((plant.pos_x, plant.pos_y))
        
        # Assign valid positions to each new animal
        for animal in animals:
            while True:
                animal.pos_x = random.randint(0, self.width - 1)
                animal.pos_y = random.randint(0, self.height - 1)
                if (animal.pos_x, animal.pos_y) not in occupied_positions:
                    occupied_positions.add((animal.pos_x, animal.pos_y))
                    break
        
        self.animals.extend(animals)