import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_new_position(x: int, y: int, direction: str) -> tuple:
    """Calculate new position based on direction.
    
    Args:
        x: Current x coordinate
        y: Current y coordinate
        direction: Direction ("up", "down", "left", "right")
    
    Returns:
        Tuple of (new_x, new_y)
    """
    if direction == "up":
        return (x, y - 1)
    elif direction == "down":
        return (x, y + 1)
    elif direction == "left":
        return (x - 1, y)
    elif direction == "right":
        return (x + 1, y)
    return (x, y)

def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    """Calculate Manhattan distance between two points."""
    return abs(x1 - x2) + abs(y1 - y2)

def get_occupied_positions(animals, plants) -> set:
    """Get all occupied positions from animals and plants.
    
    Args:
        animals: List of animals
        plants: List of plants
    
    Returns:
        Set of (x, y) tuples representing occupied positions
    """
    occupied = set()
    for animal in animals:
        if animal.pos_x > 0 or animal.pos_y > 0:
            occupied.add((animal.pos_x, animal.pos_y))
    for plant in plants:
        occupied.add((plant.pos_x, plant.pos_y))
    return occupied