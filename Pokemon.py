import random
import time
import sys
import os

import pygame
pygame.mixer.init()
pygame.mixer.music.load('Background.mp3')
pygame.mixer.music.play(-1)

def clear_screen():
    if sys.platform.startswith('win'):
        # For Windows
        os.system('cls')
    else:
        # For Linux and macOS
        os.system('clear')


charmander_pattern = """
⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧⬛⬜⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜
⬛🟥🟨🟨🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜
⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜
⬜⬜⬛🟧⬛⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧⬛⬜🟧🟧🟧⬛
⬜⬜⬛🟧🟧⬛⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧⬛⬛🟧🟧🟧⬛
⬜⬜⬛🟧🟧⬛⬜⬜⬜⬜⬛🟧🟧🟧🟧🟧⬛⬛🟧🟧🟧⬛
⬜⬜⬜⬛🟧🟧⬛⬜⬜⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜
⬜⬜⬜⬛🟧🟧🟧⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛⬜⬜
⬜⬜⬜⬜⬛🟧🟧⬛⬛🟧🟧🟧⬛🟧🟧⬛⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟧⬛🟧🟧🟧🟧🟧⬛🟧🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛🟧🟧🟧⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟧🟧🟧🟧🟨🟨🟨⬛⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟧🟧🟧🟧🟧⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟧⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜🟧⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
"""
bulbasaur_pattern = """
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟩🟩🟩⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬜⬜
⬜⬜⬜⬛⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜
⬜⬜⬛🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬜⬛🟦🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛
⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩🟩🟩⬛⬛⬛⬛⬜
⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛🟦🟦🟦⬛⬜
⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦⬜⬛⬜
⬛🟦🟦🟦🟦🟦⬛🟥⬜⬜🟦🟦⬛🟦🟦⬛⬛⬛⬜⬜
⬜⬛🟦🟦🟦🟦⬛🟥⬜🟦🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜
"""

class Event:
    NORMAL = 0
    MISS = 1
    NO_EFFECT = 2
    NOT_EFFECTIVE = 3
    VERY_EFFECTIVE = 4

    def __init__(self, event, move, damage):
        self.event = event
        self.move = move
        self.damage = damage

    def __str__(self):
        match self.event:
            case 0:
                return f'uses {self.move["Name"]} and does {self.damage:.2f} damage!'
            case 1:
                return f'uses {self.move["Name"]} but missed!'
            case 2:
                return f'uses {self.move["Name"]} but it had no effect!'
            case 3:
                return f"uses {self.move['Name']} and does {self.damage:.2f} damage! It wasn't very effective..."
            case 4:
                return f'uses {self.move["Name"]} and does {self.damage:.2f} damage! It was super effective!!'


class Pokemon:
    '''Defense -> Attack'''
    type_chart = {
        'Fire': {'Normal': 1, 'Fire': 0.5, 'Water': 2, 'Grass': 0.5, 'Electric': 1, 'Ice': 0.5, 'Fighting': 1,
                 'Poison': 1, 'Ground': 2, 'Flying': 1, 'Psychic': 1, 'Bug': 0.5, 'Rock': 2, 'Ghost': 1, 'Dragon': 1,
                 'Dark': 1, 'Steel': 0.5, 'Fairy': 0.5},
        'Grass': {'Normal': 1, 'Fire': 2, 'Water': 0.5, 'Grass': 0.5, 'Electric': 0.5, 'Ice': 2, 'Fighting': 1,
                  'Poison': 1, 'Ground': 0.5, 'Flying': 2, 'Psychic': 1, 'Bug': 2, 'Rock': 1, 'Ghost': 1, 'Dragon': 1,
                  'Dark': 1, 'Steel': 1, 'Fairy': 1},
        'Fighting': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Grass': 1, 'Electric': 1, 'Ice': 1, 'Fighting': 1,
                     'Poison': 1, 'Ground': 1, 'Flying': 2, 'Psychic': 2, 'Bug': 0.5, 'Rock': 0.5, 'Ghost': 1,
                     'Dragon': 1, 'Dark': 0.5, 'Steel': 1, 'Fairy': 2},
    }

    def __init__(self, name, types, moves, HP, Attack, SA, Defense, SD, Level):
        self.name = name
        self.type = types
        self.moves = moves  # List of 4 moves
        self.hp = HP
        self.max_hp = HP
        self.attack = Attack
        self.sa = SA
        self.defense = Defense
        self.sd = SD
        self.level = Level

    def aiMoveCalculator(self, pokemon):
        best_move_index = 0
        best_damage = 0

        for move_index, move in enumerate(self.moves):
            damage, _ = self.damageCalculator(move_index, pokemon)
            if damage > best_damage:
                best_damage = damage
                best_move_index = move_index

        return best_move_index

    def damageCalculator(self, move_index, pokemon):
        move = self.moves[move_index]
        power = move['Power']
        accuracy = move['Accuracy']
        a = self.attack if move['Category'] == 'Physical' else self.sa
        d = pokemon.defense if move['Category'] == 'Physical' else pokemon.sd
        effectiveness = Pokemon.type_chart[pokemon.type][move['Type']]

        # Calculate critical hit chance
        critical_hit_chance = 6.25

        if (move['Type'] == 'Fire' or move['Type'] == 'Grass') and self.hp <= (self.max_hp / 3):
            power *= 1.5

        if random.randint(1, 100) <= critical_hit_chance:
            critical_damage = ((((((2 * self.level) / 5) + 2) * power * (a / d)) / 50) + 2) * effectiveness * 2
            event = Event(Event.NORMAL, move, critical_damage)
            event.event = Event.NORMAL
            event.damage = critical_damage
            event.is_critical = True
            return critical_damage, event

        if random.randint(1, 100) > accuracy:
            damage = 0
            event = Event(Event.MISS, move, damage)
        else:
            damage = ((((((2 * self.level) / 5) + 2) * power * (a / d)) / 50) + 2) * effectiveness

            if effectiveness == 0:
                event = Event(Event.NO_EFFECT, move, damage)
            elif effectiveness == 0.5:
                event = Event(Event.NOT_EFFECTIVE, move, damage)
            elif effectiveness == 2:
                event = Event(Event.VERY_EFFECTIVE, move, damage)
            else:
                event = Event(Event.NORMAL, move, damage)

        return damage, event

    def display_moves(self):
        print(f"Available moves for {self.name}:")
        for i, move in enumerate(self.moves):
            print(f"{i + 1}. {move['Name']} ({move['Type']} type)")


charmander_moves = [
    {'Name': 'Scratch', 'Type': 'Normal', 'Power': 55, 'Category': 'Physical', 'Accuracy': 100},
    {'Name': 'Ember', 'Type': 'Fire', 'Power': 40, 'Category': 'Special', 'Accuracy': 90},
    {'Name': 'Dragon Tail', 'Type': 'Dragon', 'Power': 65, 'Category': 'Physical', 'Accuracy': 90},
    {'Name': 'Flamethrower', 'Type': 'Fire', 'Power': 80, 'Category': 'Special', 'Accuracy': 70},
]

bulbasaur_moves = [
    {'Name': 'Tackle', 'Type': 'Normal', 'Power': 55, 'Category': 'Physical', 'Accuracy': 100},
    {'Name': 'Razor Leaf', 'Type': 'Grass', 'Power': 55, 'Category': 'Special', 'Accuracy': 80},
    {'Name': 'Seed Bomb', 'Type': 'Grass', 'Power': 80, 'Category': 'Physical', 'Accuracy': 90},
    {'Name': 'Solar Beam', 'Type': 'Grass', 'Power': 120, 'Category': 'Special', 'Accuracy': 60},
]

mankey_moves = [
    {'Name': 'Covet', 'Type': 'Normal', 'Power': 55, 'Category': 'Physical', 'Accuracy': 100},
    {'Name': 'Bulldoze', 'Type': 'Ground', 'Power': 55, 'Category': 'Physical', 'Accuracy': 45},
    {'Name': 'Assurance', 'Type': 'Dark', 'Power': 65, 'Category': 'Physical', 'Accuracy': 100},
    {'Name': 'Cross Chop', 'Type': 'Fighting', 'Power': 70, 'Category': 'Physical', 'Accuracy': 80},
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


def opposite(string):
    nspace = 100 - len(string)
    return (' ' * nspace) + string


def reveal(*values):
    for string in values:
        for let in string:
            print(let, end='')

            if let != ' ':
                time.sleep(0.1)


def healthbar(pokemon, reverse=False):
    max_hp = int(pokemon.max_hp)
    hp = int(pokemon.hp)

    if not reverse:
        return ('#' * hp) + '_' * (max_hp - hp)
    else:
        return '_' * (max_hp - hp) + ('#' * hp)


def print_battle(player, opponent):
    print('\n' * 50)

    print(opposite(f"Opponent's {opponent.name}"))
    print(opposite((f'{healthbar(opponent, True)} : HP') if opponent.hp > 0 else f'{opponent.name} fainted!'))
    print(opposite(f"{bulbasaur_pattern}"))
    print()

    print(f'Your {player.name}')
    print((f'HP: {healthbar(player)}') if player.hp > 0 else f'{player.name} fainted!')
    print(charmander_pattern)
    print()


def main(player, opponent):
    print_battle(player, opponent)

    while player.hp > 0 and opponent.hp > 0:
        # Player turn
        player_move_index = select_move(player)
        player_damage, player_event = player.damageCalculator(player_move_index, opponent)

        print_battle(player, opponent)

        opponent.hp -= player_damage
        reveal(f'Your {player.name} {player_event}')
        time.sleep(1)

        print_battle(player, opponent)

        # Opponent turn
        if opponent.hp > 0:
            opponent_move_index = opponent.aiMoveCalculator(player)
            opponent_damage, opponent_event = opponent.damageCalculator(opponent_move_index, player)

            player.hp -= opponent_damage
            reveal(opposite(f"Opponent's {opponent.name} {opponent_event}"))
            time.sleep(1)

            print_battle(player, opponent)

            time.sleep(1)

    # Determine the winner
    if player.hp <= 0:
        reveal(f"Opponent's {opponent.name} wins the battle!")
    elif opponent.hp <= 0:
        reveal(f'Your {player.name} wins the battle!')


charmander = Pokemon('Charmander', 'Fire', charmander_moves, 39, 52, 60, 43, 50, 5)
bulbasaur = Pokemon('Bulbasaur', 'Grass', bulbasaur_moves, 45, 49, 65, 49, 65, 5)
mankey = Pokemon('Mankey', 'Fighting', mankey_moves, 40, 80, 35, 35, 45, 5)

main(charmander, bulbasaur)

time.sleep(2)
charmander.hp = charmander.max_hp

main(charmander, mankey)
