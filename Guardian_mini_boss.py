import random
import time
name = "Jude"

def main():

    is_playing = True
    while is_playing:      
        print("\033[1;33mYou can 'attack' or 'quit'\033[0m")
        command = input("What do you want to do? ")
        
        if(command == "quit"):
            is_playing = False
            print("Goodbye 👋")
        elif(command == "attack"):
            hasWon = enter_combat()
            if hasWon:
                is_playing = False
            else:
                print("You lost, attack to try again.")
        
        else:
            print("Please insert a VALID response")

def enter_combat():
    enemy_health = 20
    player_health = 20

    def print_health(colour, hp_name, current_hp, max_hp):
        enemy_health_bar = ((f"\033[1;3{colour}m█" * current_hp * 2), ("▒" * (max_hp - current_hp) * 2))
        print (f"{hp_name} Health: [", *enemy_health_bar, f"\033[0m] {current_hp}/{max_hp}", sep="") 

    def player_attack(attack):   
        if attack == "bonk":
            strength = random.randint(1, 4)
            print(f"{name} bonks the suit of armour with a candleabra they found")
            return strength
        elif attack == "rust":
            strength = random.randint(5, 10)
            print(f"{name} implies the suit of armour is rusty, that hurts its feelings and it takes {strength} damage")
            return strength
        elif attack == "kill":
            strength = 20
            return strength
        else:
            print("That is not a valid attack")

    while (enemy_health > 0) and (player_health > 0):
        # Printing HP bars using print health function
        print_health(4, "Set of armour", enemy_health, 20)
        print_health(3, "Jude", player_health, 20)

        # Choosing an attack and performing an attack
        print("Attack options [bonk, rust]")
        attack = input("Choose attack: ")
        strength = player_attack(attack)
        enemy_health -= strength
        if attack == "die":
            player_health = 0

        # Choosing a random speech option
        villain_speech = [  
            "The armour clanks angrily",
            "The set of armour points its sword at you",
            "It's helmet chatters and you swear it is cursing your family",
            "It marches tauntingly on the spot"
        ]
        rand_speech = random.choice(villain_speech)

        # Enemy chooses an attack if they are still alive
        if enemy_health > 0:
            print(rand_speech)
            enemy_attack = ["glare", "bash"]
            rand_enemy_attack = random.choice(enemy_attack)
            if rand_enemy_attack == "glare":
                strength = random.randint(1,4)
                print(f"The suit of armout glares at you menecingly, or you think it does.. Either way you take {strength} damage")
                player_health -= strength
            elif rand_enemy_attack == "bash":
                strength = random.randint(4,5)
                print(f"The suit of armour bashes you with it's shield, this is rude. You take {strength} damage")
                player_health -= strength

        # Endings depending on the outcome of the battle and bond points
        if enemy_health <= 0:
            print("The suit of armour flails its arms and falls apart angrily")

    # Finishing the combat
    if(enemy_health <= 0):
        return True
    else:
        return False

main()