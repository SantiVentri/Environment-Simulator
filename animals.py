import random

class Animal:
    def __init__( self, id: int, name: str, icon: str, food_source: str, world_width: int, world_height: int):
        # User-defined atributes
        self.id = id
        self.name = name
        self.icon = icon
        self.food_source = food_source

        # Auto-assign atributes
        self.gender = random.choice(["🚹", "🚺"])
        self.luck = random.randint(1, 10)
        self.pos_x = random.randint(0, world_width - 1)
        self.pos_y = random.randint(0, world_height - 1)

        # Default atributes
        self.alive = True
        self.age = 0.0
        self.hunger = 0.0

    def live(self):
        if self.hunger >= 10 or self.age >= 15:
            self.alive = False

        self.age += 1
        self.hunger += 1