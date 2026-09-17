import random
import time

print("\n\n")
PlayerName = input("Enter your name: ")
time.sleep(0.5)
player_hp = 100
max_player_hp = 100
player_attack = 20
player_defense = 10
Potions = 3
potions_heal = 20
xp = 0
level = 1
now_defense = player_defense


print("\n\n")
print("===============================")
print("      DUNGEON OF SHADOWS       ")
print("===============================")
time.sleep(1)
print("\n\n")
print(f"Player: {PlayerName}\n")
print(f"HP: {player_hp}\n")
print(f"Attack: {player_attack}\n")
print(f"Defense: {player_defense}\n")
print(f"level: {level}\n")



Goblin = {"name": "Goblin", "hp": 40, "attack": 10, "defense": 5}
Orc = {"name": "Orc", "hp": 60, "attack": 15, "defense": 8}
Skeleton = {"name": "Skeleton", "hp": 50, "attack": 12, "defense": 6}
Dark_Knight = {"name": "Dark_Knight", "hp": 80, "attack": 20, "defense": 12}
Dragon = {"name": "Dragon", "hp": 350, "attack": 40, "defense": 30}


normal_enemies = [Goblin, Orc, Skeleton, Dark_Knight]
enemy_actions = ["attack", "defend"]

time.sleep(3.5)
print("\nYou walk deeper into the dungeon...\n")
while True:
   random_enemy = random.choice(normal_enemies)
   if random_enemy != Dragon:
      break


time.sleep(2.5)
if random_enemy != Orc:
   print("You encounter a " + random_enemy["name"] + "!")
else:
   print("You encounter an " + random_enemy["name"] + "!")

time.sleep(2)

now_enemy_hp = random_enemy["hp"]
now_enemy_defense = random_enemy["defense"]

def game():
  global player_hp, now_enemy_hp, player_attack, player_defense, Potions, potions_heal, xp, level, now_defense, now_enemy_defense
  while player_hp > 0 and now_enemy_hp > 0:
      print("\n\n")
      print(f"{random_enemy['name']} HP: {now_enemy_hp}\n")
      print(f"{random_enemy['name']} Attack: {random_enemy['attack']}\n") 
      print(f"{random_enemy['name']} Defense: {now_enemy_defense}\n")
      print("\n\n")
      time.sleep(2.5)

      
      print("What will you do?\n")
      print("1. Attack\n")
      print("2. Defend\n")
      print("3. Use Potion\n")
      print("4. hit him from behind\n")
      print("\n\n")

      input_choice = input("Enter your choice (1-4): ")
      print("\n\n")
      match input_choice:
            case "1":
                  damage = player_attack - now_enemy_defense
                  if damage < 0:
                        damage = 0

                  now_enemy_hp -= damage
                  print(f"the enemy shield absorbs {now_enemy_defense} damage from your attack!")
                  print(f"You attack the {random_enemy['name']} for {damage} damage!")
                  print("\n\n")
                  time.sleep(2)
                  if now_enemy_hp <= 0:
                        break
                  now_enemy_defense = random_enemy["defense"]
            case "2":
                  print("You defend against the enemy's attack using the shield!")
                  print("\n\n")
                  time.sleep(2)
                  print("Defense: 10--> 20")
                  now_defense = player_defense
                  now_defense = player_defense + 10
                  print("\n\n")
            case "3":
                  if Potions > 0:
                   if player_hp < max_player_hp:
                        player_hp += potions_heal
                        if player_hp > max_player_hp:
                              player_hp = max_player_hp
                        Potions -= 1
                        print(f"You used a potion and restored 20 HP! Current HP: {player_hp}")
                        print("\n\n")
                        time.sleep(2)
                   elif player_hp == max_player_hp:
                        print("Your HP is already full! You cannot use a potion.")
                        print("\n\n")
                        time.sleep(2)
                  else:
                   print("You have no potions left!")
                   print("\n\n")
                   time.sleep(2)
                  
            case "4":
                  print("You attempt to escape...")
                  print("\n\n")
                  time.sleep(2)
                  if random.random() < 0.5:
                        print("You successfully escaped!")
                        print("\n\n")
                        time.sleep(2)
                        print("you hit him from the back dealing true damage!")
                        now_enemy_hp -= player_attack
                        print(f"You attack the {random_enemy['name']} for {player_attack} true damage!")
                        print("\n\n")
                  else:
                        print("You failed to escape! The enemy attacks you!")
                        print("\n\n")
                        time.sleep(2)
                        damage = random_enemy["attack"] - player_defense
                        player_hp -= damage
                        print(f"The {random_enemy['name']} attacks you for {damage} damage! Current HP: {player_hp}")
                        time.sleep(2)
      
      print(f"{random_enemy['name']}'s turn")
      print("\n\n")
      time.sleep(2)
      action = random.choice(enemy_actions)
      if action == "attack":
            damage = random_enemy["attack"] - now_defense
            if damage < 0:
                  damage = 0
            player_hp -= damage
            print(f"The {random_enemy['name']} attacks you for {damage} damage! Current HP: {player_hp}")
            print("\n\n")
            time.sleep(2)
      elif action == "defend":
            print(f"The {random_enemy['name']} defends against your attack!")
            print("\n\n")
            time.sleep(2)
            print("enemy Defense increases by 5 only for the next turn!")
            now_defense = player_defense
            now_enemy_defense = random_enemy["defense"] + 5
            print("\n\n")
      time.sleep(2)

def game_over():
      global xp, level, player_attack, player_defense, max_player_hp, Potions, potions_heal
      print("\n\n")
      if player_hp <= 0:
            print("You have been defeated! Game Over.")
            print("\n\n")
            time.sleep(2)
      else:
      
       print("===============================")
       print("       VICTORY! YOU WIN!       ")
       print("===============================")
       print("\n\n")
       time.sleep(2)
       if random_enemy == Goblin:
            xp += 40
       elif random_enemy == Orc:
            xp += 100
       elif random_enemy == Skeleton:
            xp += 75
       elif random_enemy == Dark_Knight:
            xp += 150
       print(f"You gained {xp} XP!")
       new_level = xp // 100 + 1
       if new_level > level:
            level = new_level
            print(f"You leveled up! You are now level {level}!")
            time.sleep(2)
            print("you can now choose to increase your stats!")
            time.sleep(2)
            print("1. Increase Attack by 5")
            print("2. Increase Defense by 5")
            print("3. Increase maximum HP by 20")
            print("4. Increase Potions by 1 and capacity to 10")
            print("\n\n")
            stat_choice = input("Enter your choice (1-4): ")
            match stat_choice:
                  case "1":
                        player_attack += 5
                        print(f"Your Attack has increased to {player_attack}!")
                        print("\n\n")
                        time.sleep(2)
                  case "2":
                        player_defense += 5
                        print(f"Your Defense has increased to {player_defense}!")
                        print("\n\n")
                        time.sleep(2)
                  case "3":
                        max_player_hp += 20
                        print(f"Your max HP has increased to {max_player_hp}!")
                        print("\n\n")
                        time.sleep(2)
                  case "4":
                        Potions += 1
                        potions_heal += 20
                        print(f"You now have {Potions} potions!")
                        print("\n\n")
                        time.sleep(2)
game()
game_over()
print("do you want to play again? (y/n)")
play_again = input().lower()
if play_again == "y":
      print("Starting a new game...")
      print("\n\n")
      time.sleep(2)
      print("You restore 20 HP for the new game!")
      print("\n\n")
      time.sleep(2)
      player_hp = player_hp + 20
      if player_hp > max_player_hp:
            player_hp = max_player_hp
            print("\n\n")
      now_enemy_hp = random_enemy["hp"]
      print("do you want to fight the Boss? (y/n)")
      if input().lower() == "n":
            game()
      else:
            random_enemy = Dragon
            now_enemy_hp = random_enemy["hp"]
            print("\n\n")
            print("You encounter the Dragon!")
            print("\n\n")
            time.sleep(2)
            print("The Dragon is a formidable foe with high HP, attack, and defense!")
            time.sleep(2)
            print("\n\n")
            print("Prepare for a tough battle!")
            time.sleep(2)
            print("\n\n")
            print("================================")
            print("           BOSS FIGHT!          ")
            print("================================")
            game()
else:
      print("Thanks for playing!")
      time.sleep(2)
      exit()