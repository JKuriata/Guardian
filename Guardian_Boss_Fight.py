import random
import time

bond_point = ""
name = ""
def main():
    global name
    global bond_point
    bond_point = 3
    name = input ("What is your name? ")
    print(f"Hello {name}")

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
    enemy_health = 30
    player_health = 20

    def print_health(colour, hp_name, current_hp, max_hp):
        enemy_health_bar = ((f"\033[1;3{colour}m█" * current_hp * 2), ("▒" * (max_hp - current_hp) * 2))
        print (f"{hp_name} Health: [", *enemy_health_bar, f"\033[0m] {current_hp}/{max_hp}", sep="") 

    def player_attack(attack):   
        if attack == "slash":
            strength = random.randint(1, 4)
            print(f"{name} slashes at the demon but it manages to jump back, only taking {strength} damage")
            return strength
        elif attack == "stab":
            strength = random.randint(5, 10)
            print(f"{name} stabs the demon, the creature lets out a pained cry as it sustains {strength} damage")
            return strength
        elif attack == "parry":
            strength = random.randint(7, 20)
            print(f"As the demon moves to slash at {name} you whip around, blocking gracefully before delivering a deep strike of your own causing {strength} damage")
            return strength
        elif attack == "kill":
            strength = 30
            return strength
        else:
            print("That is not a valid attack")

    # Making typewriter effect for text
    def list_of_speech(speech):
        for line in speech:
            for character in line:
                print(character, end= '', flush=True)
                time.sleep(0.040)
            print("")

    while (enemy_health > 0) and (player_health > 0):
        # Printing HP bars using print health function
        print_health(1, "Demon", enemy_health, 30)
        print_health(3, f"{name}\'s", player_health, 20)

        # Choosing an attack and performing an attack
        print("Attack options [slash, stab, parry]")
        attack = input("Choose attack: ")
        strength = player_attack(attack)
        enemy_health -= strength
        if attack == "die":
            player_health = 0

        # Choosing a random speech option
        villain_speech = [  
            "The demon smiles unnaturally wide... \"My turn\"",
            f"As {name} jumps back from an attack the demon lunges forward",
            f"Before {name} could strike again, the demon makes its move",
            "\"You think a shiny sword is enough to defeat me?\" the demon laughs.",
            "\"Foolish mortal!\""
        ]
        rand_speech = random.choice(villain_speech)

        # Enemy chooses an attack if they are still alive
        if enemy_health > 0:
            print(rand_speech)
            enemy_attack = ["roar", "breathe fire", "helhound attack"]
            rand_enemy_attack = random.choice(enemy_attack)
            if rand_enemy_attack == "roar":
                strength = random.randint(1,4)
                print(f"The demon roared, terrifying {name}, you take {strength} damage")
                player_health -= strength
            elif rand_enemy_attack == "breathe fire":
                strength = random.randint(4,5)
                print(f"The demon breathes fire, causing burns to {name}'s body. You take {strength} damage")
                player_health -= strength
            elif rand_enemy_attack == "helhound attack":
                strength = random.randint(5,7)
                print(f"The demon summons a dark shadowy hound which lunges at {name}. You take {strength} damage")
                player_health -= strength

        # Endings depending on the outcome of the battle and bond points
        if enemy_health <= 0:
            print("The demon roars in a mixture of disbelief and horror. It flails at it's own body as it begins to disintegrate.")
            print("\"Please... Not like this\" It begs.")
            if bond_point == 3:
                # Giving a speech
                list_of_speech([f"{name} pauses, watching the demon. They step forward, still gripping you tightly in your sword form", 
                                f"\"You have done unspeakable evil... But I will not be like you\" as they say this they plunge you into the demons heart",
                                f"Your angelic power seeps into the demon. It screams, light pouring from its pores.",
                                "Weeks later...",
                                "The king is once again well, the staff that had been turned to gargoyles return to themselves,",
                                "having no memory of the weeks they spent inprisoned",
                                f"{name} has taken their rightful place as the heir of the kingdom and are learning from their father",
                                f"You stay to watch over {name}, knowing that no matter what the forces of evil throw at you-",
                                "You will be ready"])
            elif bond_point < 3:
                # Giving a speech
                list_of_speech([f"{name} stands over the demon, panting from the exersion of battle",
                                "\"You... are a monster. You robbed me of my life, stole my face, why should I show you mercy?\"",
                                "The demons answer was lost in a pained cry and gargle as black sludge poured from its mouth",
                                f"\"Help it\" you ask {name}",
                                "But they shake their head and watch. The demons death is long and painful.",
                                f"You must have missed some chance to influance {name} towards the light.",
                                "You feel a weight on your shoulders...",
                                "Then on your feet, on your ankles, on your legs..",
                                "You look down and see chains wrapping around you",
                                "They pull and you are gone.",
                                "You see a familiar demonic face \"Seems you're on my turf now\""
                ])
        elif player_health <= 0:
            # Giving a speech
            list_of_speech([f"Despite all your efforts {name} loses the battle.",
                            f"The demon cuts {name} down with one final blow and as they lay on thr ground, bleeding",
                            f"The demon draws their blood into a symbol on the ground.",
                            f"\"A servent you were, a servant you will be\" it says, smiling mouth dripping with blood",
                            f"As it completes the symbol {name} begins to transform...",
                            f"Their limbs break and reshape as their body turns to stone,",
                            f"they scream but nothing comes out as the stone travels down their throat",
                            f"The demon smiles, its glamour returning, \"Place this thing ousdie\" it shouts to the guards outside",
                            "Now you'll always see " "\033[1;31mmy\033[0m", "kingdom"
                ])

    # Finishing the combat
    if(enemy_health <= 0):
        return True
    else:
        return False

main()