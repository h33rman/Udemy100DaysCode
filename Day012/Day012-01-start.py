##### SCOPE #######

enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# Global Scope
player_health = 10
# print(potion_strength) # NameError: name 'potion_strength' is not defined