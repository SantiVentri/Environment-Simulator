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

        # Find food if hungry
        if self.hunger > 5:
            self.find_food()

        # Attempt to breed if of age and not too hungry
        if self.age >= (self.life_span * 0.4) and self.hunger <= 4:
            self.find_partner()

        # Move randomly if not hungry or breeding
        if self.hunger < 4:
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

    def eat(self, entity):
        """Animal eats the given entity if it's a valid food source."""
        if self.food_source == "Grass" and isinstance(entity, Plant) and entity.name == "Grass":
            entity.alive = False
            self.hunger = 0
            self.environment.logs.append(f"🍽️  {self.icon}  {self.name} (N°{self.id}) ate {entity.icon} {entity.name}.")
        elif self.food_source == "Meat" and isinstance(entity, Animal) and entity.alive and entity.food_source != "Meat":
            entity.alive = False
            self.hunger = 0
            self.environment.logs.append(f"🍽️  {self.icon}  {self.name} (N°{self.id}) ate {entity.icon}  {entity.name} (N°{entity.id}).")

    def find_food(self):
        """Find and move to the nearest food source if hungry."""
        food_sources = []

        # Check for food sources in the environment
        if self.food_source == "Grass":
            food_sources = [plant for plant in self.environment.plants if plant.name == "Grass" and plant.alive]
        elif self.food_source == "Meat":
            food_sources = [animal for animal in self.environment.animals if animal.alive and animal.food_source != "Meat"]

        if not food_sources:
            # No food sources found, move randomly
            self.move(random.choice(["up", "down", "left", "right"]))
            return

        # Move to nearest food source if found
        if food_sources:
            nearest_food = min(food_sources, key=lambda f: abs(f.pos_x - self.pos_x) + abs(f.pos_y - self.pos_y))
            if nearest_food.pos_x > self.pos_x and self.can_move("right"):
                self.move("right")
            elif nearest_food.pos_x < self.pos_x and self.can_move("left"):
                self.move("left")
            elif nearest_food.pos_y > self.pos_y and self.can_move("down"):
                self.move("down")
            elif nearest_food.pos_y < self.pos_y and self.can_move("up"):
                self.move("up")

        # Eat the food source if in a neighboring cell
        if self.food_source == "Grass":
            for plant in self.environment.plants:
                if plant.name == "Grass" and plant.alive and abs(plant.pos_x - self.pos_x) <= 1 and abs(plant.pos_y - self.pos_y) <= 1:
                    self.eat(plant)
                    break
        elif self.food_source == "Meat":
            for animal in self.environment.animals:
                if animal.alive and animal.food_source != "Meat" and abs(animal.pos_x - self.pos_x) <= 1 and abs(animal.pos_y - self.pos_y) <= 1:
                    self.eat(animal)
                    break

    def find_partner(self):
        """Find and attempt to breed with a partner of the same species and opposite gender."""
        potential_partners = []

        # Look for potential partners in the environment
        for animal in self.environment.animals:
            if (
                animal.alive
                and animal.name == self.name
                and animal.age >= (animal.life_span * 0.4)
                and animal.hunger < 5
                and animal.gender != self.gender
            ):
                potential_partners.append(animal)

        if not potential_partners:
            return  # No partners available
        
        # Nearest partner position
        nearest_partner = min(potential_partners, key=lambda p: abs(p.pos_x - self.pos_x) + abs(p.pos_y - self.pos_y))

        # Move towards the nearest partner
        if nearest_partner.pos_x > self.pos_x and self.can_move("right"):
            self.move("right")
        elif nearest_partner.pos_x < self.pos_x and self.can_move("left"):
            self.move("left")
        elif nearest_partner.pos_y > self.pos_y and self.can_move("down"):
            self.move("down")
        elif nearest_partner.pos_y < self.pos_y and self.can_move("up"):
            self.move("up")

        # Attempt to breed if in a neighboring cell
        if abs(nearest_partner.pos_x - self.pos_x) <= 1 and abs(nearest_partner.pos_y - self.pos_y) <= 1:
            self.attempt_breed(nearest_partner)
        

    def attempt_breed(self, partner: 'Animal'):
        """Attempt to breed with a partner of the same species and opposite gender."""
        if not partner:
            return
        
        # 50% chance to successfully breed
        if random.random() < 0.5:
            # Create offspring
            offspring_id = len(self.environment.animals) + 1
            offspring = Animal(
                id=offspring_id,
                name=self.name,
                icon=self.icon,
                food_source=self.food_source,
                life_span=self.life_span,
                environment=self.environment
            )
            
            # Find an empty position near the parents for the offspring
            empty_position_found = False
            directions = ["up", "down", "left", "right"]
            random.shuffle(directions)
            
            for direction in directions:
                new_x, new_y = self.pos_x, self.pos_y
                
                if direction == "up":
                    new_y -= 1
                elif direction == "down":
                    new_y += 1
                elif direction == "left":
                    new_x -= 1
                elif direction == "right":
                    new_x += 1
                
                # Check if position is valid and empty
                if (0 <= new_x < self.environment.width) and (0 <= new_y < self.environment.height):
                    occupied = self.get_occupied_positions()
                    if (new_x, new_y) not in occupied:
                        offspring.pos_x = new_x
                        offspring.pos_y = new_y
                        empty_position_found = True
                        break
            
            # If no empty position near parents, place in any empty cell
            if not empty_position_found:
                for _ in range(100):  # Try up to 100 times
                    random_x = random.randint(0, self.environment.width - 1)
                    random_y = random.randint(0, self.environment.height - 1)
                    occupied = self.get_occupied_positions()
                    if (random_x, random_y) not in occupied:
                        offspring.pos_x = random_x
                        offspring.pos_y = random_y
                        empty_position_found = True
                        break
            
            # Only add offspring if a valid position was found
            if empty_position_found:
                self.environment.animals.append(offspring)
                self.environment.logs.append(f"😍 {self.icon}  {self.name} (N°{self.id}) and {partner.name} (N°{partner.id}) bred successfully! Offspring {offspring.name} N°{offspring_id} created.")
        