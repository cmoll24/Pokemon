import random
class Pokemon:
    type_chart = {
        'Fire': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Electric': 1, 'Ice': 2, 'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 2, 'Rock': 0.5, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 2, 'Fairy': 1},
        'Grass': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Electric': 1, 'Ice': 2, 'Fighting': 1,
                 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 2, 'Rock': 0.5, 'Ghost': 1, 'Dragon': 0.5,
                 'Dark': 1, 'Steel': 2, 'Fairy': 1},

    }

    def __init__(self, name, types, moves, HP, Attack, SA, Defense, SD, Level, speed):
        self.name = name
        self.type = types
        self.moves = moves  # List of 4 moves
        self.hp = HP
        self.attack = Attack
        self.sa = SA
        self.defense = Defense
        self.sd = SD
        self.level = Level
        self.speed = speed

    def aiMoveCalculator(self, pokemon):
        best_move_index = 0
        best_damage = 0

        for move_index, move in enumerate(self.moves):
            damage = self.damageCalculator(move_index, pokemon)
            if damage > best_damage:
                best_damage = damage
                best_move_index = move_index

        return best_move_index


    def damageCalculator(self, move_index, pokemon):
        move = self.moves[move_index - 1]
        power = move['Power']
        accuracy = move['Accuracy']
        a = self.attack if move['Category'] == 'Physical' else self.sa
        d = pokemon.defense if move['Category'] == 'Physical' else pokemon.sd
        effectiveness = self.type_chart[pokemon.type][move['Type']]
        if random.randint(1, 100) > accuracy:
            damage = 0
        if move['Category'] == 'Status':
            damage = 0

        else:
            damage = ((((((2 * self.level) / 5) + 2) * power * (a / d)) / 50) + 2) * effectiveness
        return damage
    def display_moves(self):
        print(f"Available moves for {self.name}:")
        for i, move in enumerate(self.moves):
            print(f"{i + 1}. {move['Name']} ({move['Type']} type)")

charmander_moves = [
    {'Name': 'Scratch', 'Type': 'Normal', 'Power': 40, 'Category': 'Physical', 'Accuracy': 100},
    {'Name': 'Ember', 'Type': 'Fire', 'Power': 40, 'Category': 'Special', 'Accuracy': 100},
    {'Name': 'Dragon Rage', 'Type': 'Dragon', 'Power': 40, 'Category': 'Special', 'Accuracy': 100},
    {'Name': 'Flamethrower', 'Type': 'Fire', 'Power': 80, 'Category': 'Special', 'Accuracy': 100},
]

bulbasaur_moves = [
    {'Name': 'Tackle', 'Type': 'Normal', 'Power': 40, 'Category': 'Physical', 'Accuracy': 100},
    {'Name': 'Seed Bomb', 'Type': 'Grass', 'Power': 80, 'Category': 'Physical', 'Accuracy': 100},
    {'Name': 'Razor Leaf', 'Type': 'Grass', 'Power': 55, 'Category': 'Special', 'Accuracy': 95},
    {'Name': 'Bullet Seed', 'Type': 'Grass', 'Power': 25, 'Category': 'Physical', 'Accuracy': 100},
]

def select_move(pokemon):
    while True:
        pokemon.display_moves()
        choice = input(f"Select a move for {pokemon.name} (1-4): ")
        try:
            choice = int(choice)
            if 1 <= choice <= 4:
                return choice - 1  # Adjust for 0-based index
            else:
                print("Invalid input. Please select a move by entering a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

charmander = Pokemon('Charmander', 'Fire', charmander_moves, 39, 52, 60, 43, 50, 5, 65)
bulbasaur = Pokemon('Bulbasaur', 'Grass', bulbasaur_moves, 45, 49, 65, 49, 65, 5, 45)

def main():
    while charmander.hp > 0 and bulbasaur.hp > 0:
        # Let the user select moves for Charmander and Charmeleon
        print()
        charmander_move_index = select_move(charmander)
        bublasaur_move_index = bulbasaur.aiMoveCalculator(charmander)

        # Calculate damage for the selected moves and apply it to the opponent
        charmander_damage = charmander.damageCalculator(charmander_move_index, bulbasaur)
        charmeleon_damage = bulbasaur.damageCalculator(bublasaur_move_index, charmander)

        charmander.hp -= charmeleon_damage
        bulbasaur.hp -= charmander_damage

        print(f'{charmander.name} uses {charmander.moves[charmander_move_index]["Name"]} and does {charmander_damage:.2f} damage!')
        print(f'{bulbasaur.name} uses {bulbasaur.moves[bublasaur_move_index]["Name"]} and does {charmeleon_damage:.2f} damage!')

        print(f'{charmander.name}\'s HP: {charmander.hp:.2f}')
        print(f'{bulbasaur.name}\'s HP: {bulbasaur.hp:.2f}')

    # Determine the winner
    if charmander.hp <= 0:
        print(f'{bulbasaur.name} wins the battle!')
    elif bulbasaur.hp <= 0:
        print(f'{charmander.name} wins the battle!')


main()
