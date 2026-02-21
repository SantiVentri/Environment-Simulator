# Libraries
import random

# Classes
from plants import Plant

class Animal:
    def __init__(self, id: int, name: str, icon: str, food_source: str, life_span, environment):
        # User-defined atributes
        self.id = id
        self.name = name
        self.icon = icon
        self.food_source = food_source
        self.environment = environment
        self.life_span = life_span

        # Auto-assign atributes
        self.gender = random.choice(["🚹", "🚺"])
        self.luck = random.randint(-5, 10)
        self.__will_die_at = self.life_span + self.luck

        # Default atributes
        self.pos_x = 0
        self.pos_y = 0
        self.alive = True
        self.age = 0.0
        self.hunger = 0.0

    def live(self):
        # Increment age and hunger
        self.age += 1
        self.hunger += 1
        
        # Check death conditions
        if self.hunger >= 10:
            self.alive = False
            self.environment.logs.append(f"💀 {self.icon}  {self.name} (N°{self.id}) died of hunger at age {self.age}.")
            return
        
        if self.age >= self.__will_die_at:
            self.alive = False
            self.environment.logs.append(f"💀 {self.icon}  {self.name} (N°{self.id}) died of old age at age {self.age}.")
            return

        # Only move if still alive
        self.move(random.choice(["up", "down", "left", "right"]))

        # Check for food in the cells around the animal
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                target_x = self.pos_x + dx
                target_y = self.pos_y + dy
                
                # Check bounds
                if 0 <= target_x < self.environment.width and 0 <= target_y < self.environment.height:
                    if self.food_source == "Grass":
                        for plant in self.environment.plants:
                            if plant.alive and plant.name == "Grass" and plant.pos_x == target_x and plant.pos_y == target_y:
                                self.eat(plant)
                                break
                    elif self.food_source == "Meat":
                        for animal in self.environment.animals:
                            if animal.alive and animal.food_source != "Meat" and animal.pos_x == target_x and animal.pos_y == target_y:
                                self.eat(animal)
                                break

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

    def eat(self, entity):
        """Animal eats the given entity if it's a valid food source."""
        if self.hunger > 5:
            if self.food_source == "Grass" and isinstance(entity, Plant) and entity.name == "Grass":
                entity.alive = False
                self.hunger = 0
                self.environment.logs.append(f"🍽️  {self.icon}  {self.name} (N°{self.id}) ate {entity.icon} {entity.name}.")
            elif self.food_source == "Meat" and isinstance(entity, Animal) and entity.alive and entity.food_source != "Meat":
                entity.alive = False
                self.hunger = 0
                self.environment.logs.append(f"🍽️  {self.icon}  {self.name} (N°{self.id}) ate {entity.icon}  {entity.name} (N°{entity.id}).")