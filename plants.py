class Plant:
    def __init__(self, id: int, name: str, icon: str):
        # User-defined atributes
        self.id = id
        self.name = name
        self.icon = icon
        
        # Default atributes
        self.alive = True
        self.pos_x = 0
        self.pos_y = 0