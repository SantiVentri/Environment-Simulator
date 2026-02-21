import random

class Animal:
    def __init__(self, id: int, name: str, icon: str, food_source: str, environment):
        # User-defined atributes
        self.id = id
        self.name = name
        self.icon = icon
        self.food_source = food_source
        self.environment = environment

        # Auto-assign atributes
        self.gender = random.choice(["🚹", "🚺"])
        self.luck = random.randint(1, 10)

        # Default atributes
        self.pos_x = 0
        self.pos_y = 0
        self.alive = True
        self.age = 0.0
        self.hunger = 0.0

    def live(self):
        if self.hunger >= 10 or self.age >= 15:
            self.alive = False

        self.age += 1
        self.hunger += 1

        self.move(random.choice(["up", "down", "left", "right"]))

    def get_occupied_positions(self):
        """Get all occupied positions in the environment."""
        occupied = set()
        for animal in self.environment.animals:
            if animal.pos_x > 0 or animal.pos_y > 0:
                occupied.add((animal.pos_x, animal.pos_y))
        for plant in self.environment.plants:
            occupied.add((plant.pos_x, plant.pos_y))
        return occupied

    def can_move(self, direction):
        """Check if the animal can move in the given direction."""
        new_x, new_y = self.pos_x, self.pos_y
        
        if direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        elif direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1
        
        # Check bounds and occupied positions
        occupied = self.get_occupied_positions()
        if (0 <= new_x < self.environment.width) and (0 <= new_y < self.environment.height) and ((new_x, new_y) not in occupied):
            return True
        return False
            
    def move(self, direction):
        """Move the animal in the given direction if possible."""
        if self.can_move(direction):
            if direction == "up":
                self.pos_y -= 1
            elif direction == "down":
                self.pos_y += 1
            elif direction == "left":
                self.pos_x -= 1
            elif direction == "right":
                self.pos_x += 1