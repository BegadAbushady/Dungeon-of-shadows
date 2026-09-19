import random
import time

player = {"name": input("Enter your name: "), "hp": 100,
          "max_hp": 100, "attack": 20,
            "defense": 10, "xp": 0,
            "potions": 3, "potion_capacity": 20
            , "level": 1, "base_defense" : 10}
Goblin = {"name": "Goblin", "hp": 40, "attack": 10, "defense": 5, "base_defense": 5, "xp": 40}
Orc = {"name": "Orc", "hp": 60, "attack": 15, "defense": 8,"base_defense": 8, "xp": 100}
Skeleton = {"name": "Skeleton", "hp": 50, "attack": 12, "defense": 6,"base_defense": 6, "xp": 75}
Dark_Knight = {"name": "Dark_Knight", "hp": 80, "attack": 20, "defense": 12, "base_defense": 12, "xp": 150}
Dragon = {"name": "Dragon", "hp": 350, "attack": 40, "defense": 30, "base_defense": 30, "xp": 450}

#all character's dictionaries assigned 

normal_enemies = [Goblin, Orc, Skeleton, Dark_Knight]

#all enemies except for the Dragon for he is the boss

time.sleep(0.5)

def game_start(player_stats,enemy_stats):

      #the whole start of the game
      print("\n\n===============================")
      print("      DUNGEON OF SHADOWS       ")
      print("===============================\n\n")
      time.sleep(1)
      
      showing_player_stats(player_stats)
      print("\nYou walk deeper into the dungeon...\n\n")
      time.sleep(1.5)
      print("There were huge, very large, vigorous shadows.\n\n")
      time.sleep(1.5)
      print("You encounter a " + enemy_stats["name"] + "!") if enemy_stats != Orc else print("You encounter an " + enemy_stats["name"] + "!")
      time.sleep(1.5)

      
def create_enemy(template):
      #creating a template of the chosen enemy
      #important for not changing the standard enemy values
      return {
            "name": template["name"],
            "hp": template["hp"],
            "attack": template["attack"],
            "defense": template["defense"],
            "xp": template["xp"],
            "base_defense": template["base_defense"]
      }

def showing_player_stats(player_stats):
      # Displayed after every battle round so the player can see
      # temporary defense changes and current HP.
      print(f"\n\nPlayer: {player_stats["name"]}\n")
      print(f"HP: {player_stats["hp"]}\n")
      print(f"Attack: {player_stats["attack"]}\n")
      print(f"Defense: {player_stats["defense"]}\n")
      print(f"level: {player_stats["level"]}\n")
      time.sleep(2)     
      

def showing_enemy_stats(enemy_stats):
     #it shows the enemy stats on the screen
     #will be called on every turn
     print(f"\n\nHP: {enemy_stats['hp']}")
     print(f"Attack: {enemy_stats['attack']}")
     print(f"Defense: {enemy_stats['defense']}\n\n")

def player_turn(choice, player_stats, enemy_stats):
      #player choices are handled here
      
      match choice:
            case '1':
                  damage =  player_stats['attack'] - enemy_stats['defense']
                  if damage < 0: damage = 0
                  enemy_stats['hp'] -= damage
                  if enemy_stats['hp'] <= 0:
                        enemy_stats['hp'] = 0
                  print(f"You dealt {damage} damage to the enemy!\n\n")
            case '2':
                  print("You defend against the enemy's attack using the shield!\n\n")
                  print("defense 10 --> 20\n\n")
                  player_stats['defense'] += 10

            case '3':
                  if player_stats['potions'] > 0:
                        if player_stats['hp'] == player_stats['max_hp']: print("You are already at full health!\n\n")

                        else: 
                              print(f"You have used a pation now you have {player_stats['potions']} potions\n\n")
                              player_stats['potions'] -= 1
                              player_stats['hp'] += player_stats['potion_capacity']
                              if player_stats['hp'] > player_stats['max_hp']: player_stats['hp'] = player_stats['max_hp']
                              print(f"Your health is now {player_stats['hp']}\n\n")

            case '4':
                  print("You attempt to hit him from behind the back!...\n\n")
                  print("\n\n")
                  time.sleep(2)
                  if random.random() < 0.5:
                        print("You hit him from behind the back!\n\n")
                        damage = player_stats['attack']
                        enemy_stats['hp'] -= damage
                        print(f"You dealt {damage} damage!\n\n")
                  else:
                        print("You missed!\n\nThe enemy attacks you!\n\n")
                        damage = enemy_stats['attack']
                        player_stats['hp'] -= damage
                        print(f"You took {damage} damage!\n\n")

def enemy_turn(player_stats, enemy_stats):
      #the enemy randomly chooses to attack or defend
      #based on random.random function
      print("enemy's turn!\n\n")
      if random.random() > 0.5:
            print("The enemy is attacking you")
            damage = enemy_stats['attack'] - player_stats['defense']
            if damage < 0:
                  damage = 0
            print(f"He dealt {damage} damage\n\n")
            player_stats['hp'] -= damage
            if player_stats['hp'] <= 0:
                  player_stats['hp'] = 0

      else:
            print("The enemy choses to defend!\n\n")
            print(f"The enemy's defense is now {enemy_stats['defense']+10}")
            enemy_stats['defense'] += 10

def game_loop(player_stats, enemy_stats):
      #the core of the game's logic
      
      while player_stats['hp'] > 0 and enemy_stats['hp'] > 0: #the loop continues till the player or enemy's hp is 0
            print("What will you do?\n")
            print("1. Attack\n")
            print("2. Defend\n")
            print("3. Use Potion\n")
            print("4. hit him from behind\n")
            choice = input()
            while choice not in ['1', '2', '3', '4']:
                  print("Invalid choice. Please choose again")
                  choice = input()
            
            player_turn(choice, player_stats, enemy_stats)
            enemy_stats['defense'] = enemy_stats['base_defense']
            enemy_turn(player_stats, enemy_stats)
            player_stats['defense'] = player_stats['base_defense']
            showing_player_stats(player_stats)
            showing_enemy_stats(enemy_stats)

def finish_game(player_stats, enemy_stats):
       #the function to end the game and check if the player still wants to continue and weither he wants to face the boss or not
       if player_stats['hp'] <= 0:
             print("Game Over! You have been defeated!\n\n")
       else:
             print("===============================")
             print("       VICTORY! YOU WIN!       ")
             print("===============================")
             print("\n\n")
             time.sleep(2)
             leveling_up(player_stats, enemy_stats['xp'])

       print("Do you wanna play again? y/n")
       choice = input()
       while choice not in ['y', 'n']:
            print("Invalid choice. Please choose again")
            choice = input()
       if choice == 'y':
            print("do you wanna face the boss? y/n")
            choice = input()
            while choice not in ['y', 'n']:
                  print("Invalid choice. Please choose again")
                  choice = input()
            if choice == 'y':
                 template = create_enemy(Dragon)
            else:
                 template = create_enemy(random.choice(normal_enemies))
            return template
       else:
            print("game is closing...")
            time.sleep(2)
            return None

                                    
def leveling_up(player_stats,xp):
      #this function controls leveling up logic
      print(f"Congratulations! You have won {xp} XP!")
      player_stats['xp'] += xp
      new_level = player_stats['xp'] // 100 + 1
      if new_level > player_stats['level']:
            player_stats['level'] = new_level
            print(f"Your new level is {player_stats['level']}!")
            player_stats['max_hp'] += 150
            player_stats['attack'] += 30
            player_stats['defense'] += 20
            player_stats['base_defense'] +=20
            player_stats['potion_capacity'] += 10
            print("All your stats has increased and enhanced!!")

temp = create_enemy(random.choice(normal_enemies))
while temp!=None: #the loop continues till the player choses to end the game
    game_start(player,temp)
    showing_enemy_stats(temp)
    game_loop(player, temp)
    temp = finish_game(player,temp)
print("thanks for playing")