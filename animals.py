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