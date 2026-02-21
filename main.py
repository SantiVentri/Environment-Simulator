# Classes
from animals import Animal
from environment import Environment

# Helpers
from helpers import clear_screen

# Environment settings
HEIGHT = 20
WIDTH = 50

def ask_grass():
    percentage = 0
    while True:
        try:
            percentage = int(input("What percentage of land should be covered with grass? (0-50%) (5-10% recommended): "))
            if 0 <= percentage <= 50:
                print(f"✅ Grass will cover {percentage}% of the environment.\n")
                break
            else:
                raise ValueError
        except ValueError:
            print("❌ Please enter a valid percentage (0-50).")
        except Exception as e:
            print("❌ An error occurred.", e)

    total_cells = HEIGHT * WIDTH
    grass_cells = int((percentage / 100) * total_cells)
    return grass_cells

def ask_animals(plant_cells, environment):
    animals = []
    choices = {
        # ID: [Icon, Name, Food Source, Life Span]
        1: ["🐇", "Rabbit", "Grass", 5],
        2: ["🐑", "Sheep", "Grass", 10],
        3: ["🐐", "Goat", "Grass", 12],
        4: ["🦤", "Dodo", "Grass", 15],
        5: ["🦃", "Turkey", "Grass", 8],
        6: ["🐓", "Rooster", "Grass", 7],
        7: ["🐅", "Tiger", "Meat", 20],  
        8: ["🐆", "Leopard", "Meat", 18]
    }

    space = HEIGHT * WIDTH - plant_cells - len(animals)
    print("Choose animals to add to the environment:")
    print("Herbivores: \n1. 🐇 Rabbit\n2. 🐑 Sheep\n3. 🐐 Goat\n")
    print("Birds: \n4. 🦤  Dodo  \n5. 🦃 Turkey\n6. 🐓 Rooster\n")
    print("Carnivores: \n7. 🐅 Tiger\n8. 🐆 Leopard\n")

    while True:
        percentage_left = (space / (HEIGHT * WIDTH)) * 100
        print(f"❗ Available space: {space} cells. {percentage_left:.0f}% left. (80-90% recommended)\n")
        try:
            animal = int(input("Add animal to the environment (Type ID, 0 to exit): "))
            if animal == 0:
                break

            if animal in range(1, 9):
                # Determine the correct plural form of the animal name
                name = choices[animal][1].lower()
                plural = name if animal == 2 else name + 's'

                # Check if there's enough space for the new animals
                quantity = int(input(f"How many {plural}?: "))
                if quantity > space:
                    raise ValueError("❌ Maximum quantity surpassed. Enter ID 0 to exit.\n")
                if quantity <= 0:
                    raise ValueError("❌ Please enter a valid quantity.\n")
                
                # Add the specified number of animals to the list
                for _ in range(quantity):
                    animals.append(Animal(
                        id=len(animals) + 1,
                        icon=choices[animal][0],
                        name=choices[animal][1],
                        food_source=choices[animal][2],
                        life_span=choices[animal][3],
                        environment=environment
                    ))
                print(f"✅ {choices[animal][0]} {choices[animal][1]}(s) added to the environment.\n")
                space -= quantity
            else:
                raise ValueError("❌ Please enter a valid ID.")
            
        except ValueError as ve:
            print(ve, "\n")
        except Exception as e:
            print(f"❌ An error occurred. {e}\n")

    return animals

def main():
    clear_screen()
    print("🌿 Welcome to the Environment Simulator! 🌿")
    print("In this simulator, you can create a virtual environment by adding animals and plants. 🌱 🐇 🐅\n")

    try:
        environment = Environment(WIDTH, HEIGHT)
        grass = ask_grass()
        environment.add_plants(grass)
        animals = ask_animals(grass, environment)
        environment.add_animals(animals)
        environment.display()
    except (KeyboardInterrupt, SystemExit):
        print("Exiting matrix...")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()