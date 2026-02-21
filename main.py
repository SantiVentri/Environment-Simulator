# Libraries
import os

# Classes
from animals import Animal
from environment import Environment

# Environment settings
HEIGHT = 20
WIDTH = 50
LOGS = []

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_animals():
    choices = {
        1: ["🐇", "Rabbit", "Grass"],
        2: ["🐑", "Sheep", "Grass"],
        3: ["🐐", "Goat", "Grass"],
        4: ["🦤", "Dodo", "Grass"],
        5: ["🦃", "Turkey", "Grass"],
        6: ["🐓", "Rooster", "Grass"],
        7: ["🐅", "Tiger", "Meat"],
        8: ["🐆", "Leopard", "Meat"]
    }
    print("Herbivores: \n1. 🐇 Rabbit\n2. 🐑 Sheep\n3. 🐐 Goat\n")
    print("Birds: \n4. 🦤  Dodo  \n5. 🦃 Turkey\n6. 🐓 Rooster\n")
    print("Carnivores: \n7. 🐅 Tiger\n8. 🐆 Leopard\n")
    
    animals = []
    while True:
        try:
            animal = int(input("Add animal to the environment (Type ID, 0 to exit): "))
            if animal == 0:
                break

            if animal in range(1, 9):
                name = choices[animal][1].lower()
                plural = name if animal == 2 else name + 's'
                quantity = int(input(f"How many {plural}?: "))
                for _ in range(quantity):
                    animals.append(Animal(
                        id=len(animals) + 1,
                        icon=choices[animal][0],
                        name=choices[animal][1],
                        food_source=choices[animal][2],
                        world_width=WIDTH,
                        world_height=HEIGHT
                    ))
                print(f"✅ {choices[animal][0]} {choices[animal][1]}(s) added to the environment.")
            else:
                raise ValueError
            
            
        except ValueError:
            print("❌ Please enter a valid ID.")
        except Exception as e:
            print("❌ An error occurred.", e)

    return animals

def main():
    clear_screen()
    try:
        environment = Environment(WIDTH, HEIGHT)
        animals = ask_animals()
        environment.add_animals(animals)
        environment.display(logs=LOGS)
    except (KeyboardInterrupt, SystemExit):
        print("Exiting matrix...")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()