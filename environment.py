class Environment:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.animals = []
        self.plants = []

    def display(self, logs):
        """Displays the current state of the environment."""

        # Create empty grid
        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

        # Display animal and plant icons in their current position
        for plant in self.plants:
            grid[plant.pos_y][plant.pos_x] = plant.icon

        for animal in self.animals:
            grid[animal.pos_y][animal.pos_x] = animal.icon

        # Print grid
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += grid[y][x]
            print(row)

        # Display Logs
        for log in logs[-5:]:
            print(log)