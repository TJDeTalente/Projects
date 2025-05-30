potions = {
    "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"],
    "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"],
    "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"]
}

# Display available potions
print("Welcome, here are the available Potions:")
for potion in potions:
    print(f"- {potion}")

# Ask the user to choose a potion
chosen_potion = input("\nWhich potion would you like to craft? ").strip()

# Check if the chosen potion exists
if chosen_potion in potions:
    ingredients = potions[chosen_potion]
    print(f"\nYou selected '{chosen_potion}'. It requires the following ingredients:")

    # Start shopping for ingredients
    index = 0
    bought_ingredients = []

    while index < len(ingredients):
        ingredient = ingredients[index]
        choice = input(f"Do you want to buy '{ingredient}'? (yes/no): ").strip().lower()

        if choice == "yes":
            bought_ingredients.append(ingredient)
            index += 1
        else:
            print("You chose to stop shopping.")
            break

    # Check if all ingredients are bought
    if len(bought_ingredients) == len(ingredients):
        print(f"\n Success! You bought all ingredients for the '{chosen_potion}'.")
    else:
        print(f"\n⚠ You did not buy all the ingredients for the '{chosen_potion}'.")
else:
    print("\n Potion not found. Please check the name and try again.")
