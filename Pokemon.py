import random
import time
import sys
import os

import pygame
try:
    pygame.mixer.init()
    pygame.mixer.music.load('Background.mp3')
    pygame.mixer.music.play(-1)
except:
    pass

def clear_screen():
    if sys.platform.startswith('win'):
        # For Windows
        os.system('cls')
    else:
        # For Linux and macOS
        os.system('clear')


space_pattern = '⬜'

charmander_pattern = [
'⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜',
'⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥⬛⬜⬜', 
'⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥🟥⬛⬜', 
'⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥🟥⬛⬜', 
'⬜⬜⬜⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬛🟥🟨🟨🟥⬛', 
'⬜⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬛🟥🟨🟨🟥⬛', 
'⬜⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬛🟥🟨🟨🟥⬛', 
'⬜⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬛🟥🟥⬛⬜', 
'⬛🟧🟧🟧⬜⬛🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬛🟧⬛⬜⬜', 
'⬛🟧🟧🟧⬛⬛🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬛🟧🟧⬛⬜⬜', 
'⬛🟧🟧🟧⬛⬛🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬛🟧🟧⬛⬜⬜', 
'⬜⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜⬜⬛🟧🟧⬛⬜⬜⬜', 
'⬜⬜⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛🟧🟧🟧⬛⬜⬜⬜', 
'⬜⬜⬜⬜⬛⬛⬛🟧🟧⬛🟧🟧🟧⬛⬛🟧🟧⬛⬜⬜⬜⬜', 
'⬜⬜⬜⬜⬜⬛🟨🟧⬛🟧🟧🟧🟧🟧⬛🟧⬛⬜⬜⬜⬜⬜', 
'⬜⬜⬜⬜⬜⬛🟨🟨🟨⬛⬛🟧🟧🟧⬛⬛⬜⬜⬜⬜⬜⬜', 
'⬜⬜⬜⬜⬛⬜⬛🟨🟨🟨🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜', 
'⬜⬜⬜⬜⬜⬛⬛⬛🟧🟧🟧🟧🟧⬛⬛⬜⬜⬜⬜⬜⬜⬜', 
'⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟧⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜', 
'⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜🟧⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜']

bulbasaur_pattern = [
'⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜',
'⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟩🟩🟩⬛⬜⬜⬜⬜',
'⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟩🟩🟩⬛⬜⬜⬜⬜',
'⬜⬜⬜⬜⬜⬜⬜⬛⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛⬜⬜',
'⬜⬜⬜⬛⬜⬜⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬜',
'⬜⬜⬛🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛',
'⬜⬜⬛🟦🟦🟦⬛⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛',
'⬜⬜⬛🟦🟦🟦🟦🟦⬛🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛',
'⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟩🟩🟩🟩🟩🟩⬛⬜',
'⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟩🟩🟩⬛⬛⬛⬛⬜',
'⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦⬛⬛⬛🟦🟦🟦⬛⬜',
'⬛🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦⬜⬛⬜',
'⬛🟦🟦🟦🟦🟦⬛🟥⬜⬜🟦🟦⬛🟦🟦⬛⬛⬛⬜⬜',
'⬜⬛🟦🟦🟦🟦⬛🟥⬜🟦🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜',
'⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜',
'⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜',
'⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜',
]

mankey_pattern = [
'⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜',
'⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜',
'⬜⬜⬜⬜⬜⬜⬛🟨⬛🟨🟧🟧🟧⬛⬛⬜⬛🟧🟧🟫🟫⬛⬜⬜⬜',
'⬜⬜⬜⬛⬛⬛⬛🟨🟧🟨🟨⬛⬛⬛🟧⬛⬛🟫🟫🟫⬛⬛⬜⬜⬜',
'⬜⬜⬜⬛🟨⬛🟨🟨🟨🟨🟨⬛🟨🟧⬛⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜',
'⬜⬜⬜⬛🟧⬛🟨🟨🟨🟨🟨🟨🟫🟧🟧⬛⬛⬛🟫🟫⬛⬜⬜⬜⬜',
'⬜⬛⬛⬜⬛🟨🟧🟧🟧🟧🟧⬛🟧🟧🟧🟧🟧🟫🟧🟧⬛⬜⬜⬜⬜',
'⬛🟧🟫⬛⬛⬛🟧🟧🟧🟨⬛⬜⬛🟧🟧⬛⬛⬛⬛🟧⬛⬜⬜⬜⬜',
'⬛🟧🟫⬛⬛⬜⬛⬛⬛⬛⬛⬜🟨🟧🟧🟧⬛⬜⬛⬛⬜⬜⬜⬜⬜',
'⬛🟫🟫⬛⬛⬛🟥🟥🟥⬛🟨🟨🟨🟧🟧⬛⬛⬜⬜⬜⬜⬜⬛⬛⬜',
'⬛🟫⬛🟫⬛⬛🟫🟥🟫⬛🟨🟨🟧🟧🟧⬛🟫⬛⬛⬜⬜⬛🟫🟫⬛',
'⬜⬛⬛⬛⬛⬛⬛⬛⬛🟧🟧🟧🟧⬛⬛⬛⬛🟫🟧⬛⬛⬛⬛🟫⬛',
'⬜⬜⬜⬜⬜⬜⬛🟫⬛⬛⬛⬛⬛🟧⬛⬜⬜⬛⬛🟧🟧🟧🟫⬛⬜',
'⬜⬜⬜⬜⬜⬛🟫⬛🟫🟫⬛⬜⬛🟫⬛⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜',
'⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬛🟫🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜',
'⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟫⬛🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜',
'⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜',
]

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

    def __init__(self, name, types, moves, HP, Attack, SA, Defense, SD, Level, Pattern):
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
        self.pattern = Pattern

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
            sys.stdout.write(let)
            sys.stdout.flush()

            if let != ' ':
                time.sleep(0.1)


def healthbar(pokemon, reverse=False):
    max_hp = int(pokemon.max_hp)
    hp = int(pokemon.hp)

    red = '\u001b[41m \033[0m'
    empty = '\u001b[40m \033[0m'

    if not reverse:
        return 'HP: ' + (red * hp) + empty * (max_hp - hp)
    else:
        return (' ' * (100 - max_hp - 5)) + empty * (max_hp - hp) + (red * hp) + ' : HP'

def print_visuals(player, opponent):
    player_len = len(player.pattern)
    player_width = len(player.pattern[0])
    opponent_len = len(opponent.pattern)
    opponent_width = len(opponent.pattern[0])
    len_max = max(player_len, opponent_len)
    
    
    for i in range(len_max):
        if i < player_len:
            print(player.pattern[i], end = '')
        else:
            print(space_pattern * player_width, end = '')
        
        print(space_pattern * 3, end = '')
        
        if i < opponent_len:
            print(opponent.pattern[i], end = '')
        else:
            print(space_pattern * opponent_width, end = '')
        print(end='\n')

def print_battle(player, opponent):
    print('\n' * 50)

    print(opposite(f"Opponent's {opponent.name}"))
    print(healthbar(opponent, True) if opponent.hp > 0 else opposite(f'{opponent.name} fainted!'))
    print()
    
    print_visuals(player,opponent)

    print(f'Your {player.name}')
    print((f'HP: {healthbar(player)}') if player.hp > 0 else f'{player.name} fainted!')
    print()

def reverse_sprite(pattern):
  return [i[::-1] for i in pattern]

def main(player, opponent):
    player.pattern = reverse_sprite(player.pattern)
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

charmander = Pokemon('Charmander', 'Fire', charmander_moves, 39, 52, 60, 43, 50, 5, charmander_pattern)
bulbasaur = Pokemon('Bulbasaur', 'Grass', bulbasaur_moves, 45, 49, 65, 49, 65, 5, bulbasaur_pattern)
mankey = Pokemon('Mankey', 'Fighting', mankey_moves, 40, 80, 35, 35, 45, 5, mankey_pattern)

main(charmander, bulbasaur)

time.sleep(2)
charmander.hp = charmander.max_hp

main(charmander, mankey)
