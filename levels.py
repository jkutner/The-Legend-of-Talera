import functions
import text
import sys
import time
import random
import os
import game
import city

# name = game.user_name

def waiting_room():
	typing("Ah, welcome back!\n")
	#guides = ["Alice", "Jerry", "Brian", "Rachel", "Pepe", "Steve", "Hipster Dave", "Vadercat", "Albert", "Alfred", "Bruce", "Alfredo", "Phil", "Macy", "Santa", "The Easter Bunny", "The Thanksgiving Turkey", "Tammie", "Clyde", "Chris", "Joy", "Joe", "Benny", "Wolf", "Don", "Mr. Lemon", "Andrew", "Stephanie", "Michelle", "Laura", "Carl", "Harriet", "Danny", "Joey", "Jessie", "Becky", "Nicky", "Alex", "Frank", "Rich", "Dana", "Lily", "Sabrina", "Hilda", "Zelda", "Salem", "Amanda", "Harvey", "Mark", "Waldo", "Stefan", "Weasel", "Eddie", "Judy", "Myra", "Kimmy", "D.J.", "Fernando", "Jimmy", "John", "Mike", "Meatball Sub", "Mr. Subway", "Greg", "Netherite", "Enderman", "George,", "Adam", "Thomas", "Abraham", "Lincoln", "Denzel", "Zachary", "Garfield", "Peter", "Paige", "Andy", "Monty", "Roomba", "Arnold", "Terry", "Simon", "Mel", "Howie", "Heidi", "Frances", "Tommy", "Donald", "Kevin", "Harry", "Marv", "Fuller", "Buzz", "Buddy", "Narwahl", "Rudolph", "Michael", "Tiger", "Metta", "Tiki", "Lewis", "Clark", "Sacajawea", "Reginald", "Jacques", "Augustus", "Charlie", "A person with a very long name and this is it so yes this is his name and you should like it and if you don't deal with it and oh no i am running out of things to say so i will put in a bunch of filler words to make this longer and whoever came up with this name is the greatest person on earth no wait the galaxy actually the universe wow this name is very long but i am proud of it well i am running out of space so goodbye wait did i mention that i can count to 10 do you want to hear it ok you do 1 2 3 4 5 6 7 8 9 9 10 oh no i did it wrong i need to restart but it will take a long time 1   2   3   4   5   6   7   8   9   10 yay i am now done wow that was some superb counting ok goodbye for real oh just one more thing i will miss you a lot bye bye"]
	#randomguide = random.choice(guides)
	#typing("Welcome to Talera waiting room! Today, " + randomguide + " will be your guide.\n")
	#typing(randomguide + " - Let's see what trophies you currently have.\n")
	#if trophies == []:
		#typing("Hmm... seems like you do not have any trophies.\n")
	#else:
		#typing("Your trophies are:\n")
		#for t in trophies:
			#typing(t + "\n")
	typing("Would you like to go to the city, start another quest, or take a break and leave the game?\n")
	text.city_or_quest()
	city_or_quest = ""
	while city_or_quest not in ["1", "2"]:
		city_or_quest = input("> ")
	if city_or_quest == "1":
		clear()
		typing("Ok! You want to go to the city!\n")
		time.sleep(2)
		city.city_teleport()
	elif city_or_quest == "2":
		clear()
		text.levels()
		levelpick = ""
		while levelpick not in ["1", "2", "3"]:
			levelpick = input("> ")
		if levelpick == "1":
			mines()
		elif levelpick == "2":
			forest()
		elif levelpick == "3":
			mountains()
	elif city_or_quest == "3":
		typing("Are you sure you want to leave? You will lose all of your progress. (y/n)\n")
		exit_confirm = ""
		while exit_confirm not in ["y", "n"]:
			exit_confirm = input("> ")
		if exit_confirm == "y":
			typing("Okay, then. See you next time!\n")
			exit()
		elif exit_confirm == "n":
			typing("Okay. ")
			functions.waitingroom_teleport()

typingspeed = 100

def clear():
	if sys.platform.startswith("linux"):
		os.system("clear")
	elif sys.platform.startswith("win32"):
		os.system("cls")
	elif sys.platform.startswith("darwin"):
		os.system("clear")

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typingspeed)

def settype(text, typing_speed):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/typing_speed)

def mines():
	clear()
	typing("Before we travel to THE MINES, we need to set your levels.\n")
	time.sleep(1)
	clear()
	global speed
	global charisma
	global strength
	global knowledge
	functions.textloading(3, "Rolling Dice")
	levelnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	knowledge = random.choice(levelnumbers)
	strength = random.choice(levelnumbers)
	charisma = random.choice(levelnumbers)
	speed = random.choice(levelnumbers)
	typing("Your knowledge level is " + str(knowledge) + ".\n")
	typing("Your strength level is " + str(strength) + ".\n")
	typing("Your charisma level is " + str(charisma) + ".\n")
	typing("Your speed level is " + str(speed) + ".\n")
	averageleveladd = knowledge + strength + charisma + speed
	averageleveldivide = averageleveladd/4
	typing("Your average level is " + str(averageleveldivide) + ".\n")
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	functions.textloading(3, "Traveling to THE MINES")
	typing("Welcome to THE MINES! Today, your goal is the get the famous TALERA RUBY.\n")
	typing("You will need to get past rock monsters and big avalanches.\n")
	typing("Let's begin!\n")
	typing("As you walk to the entrance of the mine, you realize that your mine pass has expired. You are not allowed to go in the mines without one.\n")
	typing("You do have the chance to convince the worker to let you in. You need a charisma level above 3 to do that.\n")
	typing("You can also try to sneak in. If it goes wrong, you will spend the rest of your life in prison.\n")
	text.mine_entrance()
	entrance = ""
	while entrance not in ("1", "2"):
		entrance = input("> ")
	if entrance == "1":
		clear()
		if charisma >= 4:
			typing("You sucessfully convinced the worker to let you in.\n")
			mines_again()
		else:
			typing("You were unable to convince the worker to let you in. You walk away in defeat.\n")
			text.youlost()
			functions.waitingroom_teleport()
	elif entrance == "2":
		clear()
		typing("You attempt to sneak in.\n")
		typing("Right as you sneak in to the mine, a police officer sees you.\n")
		typing("Quick! We need to do something!\n")
		text.policeoptions()
		police_options = ""
		while police_options not in ["1", "2", "3", "4"]:
			police_options = input("> ")
		if police_options == "1":
			clear()
			typing("You attempt to run away.\n")
			if speed >= 5:
				typing("Since you have a speed level of over 4, you are pretty fast. The policeman is no match for you.\n")
				mines_again()
			else:
				typing("You have a speed level under 4. You are so slow! The policeman catches you, and you get put in jail forever.\n")
				text.youlost()
				functions.waitingroom_teleport()
		if police_options == "2":
			clear()
			typing("You attempt to negotiate.\n")
			typing("You REALLY think you are going to get away with this? I THINK NOT!\n")
			text.youlost()
			functions.waitingroom_teleport()
		if police_options == "3":
			clear()
			typing("You attempt to hide.\n")
			if knowledge >= 4:
				typing("Since you have a knowledge level of over 3, you at least know a good place to hide.\n")
				mines_again()
			else:
				typing("You have a knowledge level under 3.\n")
				typing("You are pretty dumb, because you for some reason you hid behind the police officer.\n")
				text.youlost()
				functions.waitingroom_teleport()
		if police_options == "4":
			clear()
			typing("You attempt to fight.\n")
			if strength >= 5:
				typing("Since you have a strength level over 4, you are pretty strong. That police man was no match for you.\n")
				mines_again()
			else:
				typing("Why do you even try? You arms are like floppy noodles!\n")
				text.youlost()
				functions.waitingroom_teleport()

def mines_again():
	typing("As you walk through the mine, you see green gems, yellow gems, blue gems, but no TALERA RUBY.\n")
	typing("Then, you see a giant glimmering ruby sitting in a glass cage.\n")
	text.rubysteal()
	glass = ""
	while glass not in ["1", "2", "3"]:
		glass = input("> ")
	if glass == "1":
		clear()
		typing("You attempt to break the glass with a stone.\n")
		typing("BEEP BEEP BEEP! An alarm sounds and a rock monster comes out of the cave.\n")
		text.rockmonster()
		rockmonster = ""
		while rockmonster not in ["1", "2"]:
			rockmonster = input("> ")
		if rockmonster == "1":
			clear()
			typing("You attempt to fight the rock monster.\n")
			if strength >= 7:
				typing("WOW! You have a strength level of over 6! You successfully defeated the rock monster!\n")
				typing("You obtain the TALERA RUBY!\n")
				typing("As you run for the exit of the mine, an AVALANCHE starts!\n")
				text.avalanche()
				avalanche = ""
				while avalanche not in ["1", "2", "3"]:
					avalanche = input("> ")
				if avalanche == "1":
					clear()
					typing("You attempt to run.\n")
					if speed == 10:
						typing("WHAT??? You have a speed level of 10! You successfully made it out of the cave.\n")
						if "Talera Ruby" not in city.trophies:
							city.trophies.append("Talera Ruby")
							typing("You obtained the TALERA RUBY!\n")
							typing("You have also earned 20 coins!\n")
							city.coins = city.coins + 20
							text.youwon()
							if "Shattered Ruby Pieces" not in city.trophies:
								typing("You may have won, but you can also get the shattered ruby pieces.\n")
							functions.waitingroom_teleport()
						else:
							typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
							typing("You still have earned 10 coins!\n")
							city.coins = city.coins + 10
							text.youwon()
							functions.waitingroom_teleport()
					else:
						typing("The avalanche was too fast...\n")
						text.youlost()
						functions.waitingroom_teleport()
				elif avalanche == "2":
					clear()
					typing("You attempt to find a safe place to hide.\n")
					typing("You find a big rock to hide under.\n")
					typing("The avalanche ends.\n")
					if "Talera Ruby" not in city.trophies:
						city.trophies.append("Talera Ruby")
						typing("You obtained the TALERA RUBY!\n")
						typing("You have also earned 20 coins!\n")
						city.coins = city.coins + 20
						text.youwon()
						if "Shattered Ruby Pieces" not in city.trophies:
							typing("You may have won, but you can also get the shattered ruby pieces.\n")
						functions.waitingroom_teleport()
					else:
						typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
						typing("You still have earned 10 coins!\n")
						city.coins = city.coins + 10
						functions.waitingroom_teleport()
				elif avalanche == "3":
					clear()
					typing("You attempt to shield yourself with the ruby.\n")
					typing("As the rocks fall on the ruby, it shatters to pieces.\n")
					typing("Still, you have made it out of the mines.\n")
					if "Shattered Ruby Pieces" not in city.trophies:
						city.trophies.append("Shattered Ruby Pieces")
						typing("You obtained the SHATTERED RUBY PIECES!\n")
						typing("You have also earned 15 coins!\n")
						city.coins = city.coins + 15
						text.youwon()
						if "Talera Ruby" not in city.trophies:
							typing("You may have won, but you can still get the full ruby.\n")
						functions.waitingroom_teleport()
					else:
						typing("Seems like you already have the SHATTERED RUBY PIECES inside your trophy room...\n")
						typing("You still have earned 8 coins!\n")
						city.coins = city.coins + 8
						functions.waitingroom_teleport()
		elif rockmonster == "2":
			clear()
			typing("You ran away from the monster, but you forgot one key item...\n")
			typing("THE RUBY.\n")
			text.youlost()
			functions.waitingroom_teleport()
	elif glass == "2":
		clear()
		typing("You attempt to slowly lift up the glass.\n")
		typing("You obtain the TALERA RUBY!\n")
		typing("As you run for the exit of the mine, an AVALANCHE starts!\n")
		text.avalanche()
		avalanche = ""
		while avalanche not in ["1", "2", "3"]:
			avalanche = input("> ")
		if avalanche == "1":
			clear()
			typing("You attempt to run.\n")
			if speed == 10:
				typing("WHAT??? You have a speed level of 10! You successfully made it out of the cave.\n")
				if "Talera Ruby" not in city.trophies:
					city.trophies.append("Talera Ruby")
					typing("You obtained the TALERA RUBY!\n")
					typing("You have also earned 20 coins!\n")
					city.coins = city.coins + 20
					text.youwon()
					typing("You may have won, but you can also get the shattered ruby pieces.\n")
					functions.waitingroom_teleport()
				else:
					typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
					typing("You still have earned 10 coins!\n")
					city.coins = city.coins + 10
					text.youwon()
					functions.waitingroom_teleport()
			else:
				typing("The avalanche was too fast...\n")
				text.youlost()
				functions.waitingroom_teleport()
		elif avalanche == "2":
			clear()
			typing("You attempt to find a safe place to hide.\n")
			typing("You find a big rock to hide under.\n")
			typing("The avalanche ends.\n")
			if "Talera Ruby" not in city.trophies:
				city.trophies.append("Talera Ruby")
				typing("You obtained the TALERA RUBY!\n")
				typing("You have also earned 20 coins!\n")
				city.coins = city.coins + 20
				text.youwon()
			if "Shattered Ruby Pieces" not in city.trophies:
				typing("You may have won, but you can also get the shattered ruby pieces.\n")
				functions.waitingroom_teleport()
			else:
				typing("Seems like you already have the TALERA RUBY inside your trophy room...\n")
				typing("You still have earned 10 coins!\n")
				city.coins = city.coins + 10
				functions.waitingroom_teleport()
		elif avalanche == "3":
			clear()
			typing("You attempt to shield yourself with the ruby.\n")
			typing("As the rocks fall on the ruby, it shatters to pieces.\n")
			typing("Still, you have made it out of the mines.\n")
			if "Shattered Ruby Pieces" not in city.trophies:
				city.trophies.append("Shattered Ruby Pieces")
				typing("You obtained the SHATTERED RUBY PIECES!\n")
				typing("You have also earned 15 coins!\n")
				city.coins = city.coins + 15
				text.youwon()
				if "Talera Ruby" not in city.trophies:
					typing("You may have won, but you can still get the full ruby.\n")
				functions.waitingroom_teleport()
			else:
				typing("Seems like you already have the SHATTERED RUBY PIECES inside your trophy room...\n")
				typing("You have still earned 8 coins!\n")
				city.coins = city.coins + 8				
				functions.waitingroom_teleport()
	elif glass == "3":
		clear()
		typing("You admire the ruby.\n")
		time.sleep(1)
		functions.textloading(3, "Admiring the TALERA RUBY")
		typing("How is this going to help?\n")
		text.youlost()
		functions.waitingroom_teleport()

def forest():
	clear()
	typing("Before we travel to THE FOREST, we need to set your levels.\n")
	time.sleep(1)
	clear()
	functions.textloading(3, "Rolling Dice")
	levelnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	knowledge = random.choice(levelnumbers)
	strength = random.choice(levelnumbers)
	charisma = random.choice(levelnumbers)
	speed = random.choice(levelnumbers)
	typing("Your knowledge level is " + str(knowledge) + ".\n")
	typing("Your strength level is " + str(strength) + ".\n")
	typing("Your charisma level is " + str(charisma) + ".\n")
	typing("Your speed level is " + str(speed) + ".\n")
	averageleveladd = knowledge + strength + charisma + speed
	averageleveldivide = averageleveladd/4
	typing("Your average level is " + str(averageleveldivide) + ".\n")
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	functions.textloading(3, "Traveling to THE FOREST")
	typing("Welcome to THE FOREST! Today, your goal is to get the ELVERN FLUTE.\n")
	typing("Let's begin!\n")
	typing("For this adventure, you need to choose a weapon. This will affect the game later on.\n")
	text.weapon_forest()
	weapon = ""
	while weapon not in ["1", "2", "3"]:
		weapon = input("> ")
	if weapon == "1":
		clear()
		typing("You have chosen the sword. Good choice!\n")
	elif weapon == "2":
		clear()
		typing("Nice! You chose the bow!\n")
	elif weapon == "3":
		clear()
		typing("The mace is a good choice!\n")
	typing("As you walk through the forest trail, you see many trees and flowers.\n")
	typing("Then, you see a sign. Would you like to read it? (y/n)\n")
	sign = ""
	while sign not in ["y", "n"]:
		sign = input("> ")
	if sign == "y":
		clear()
		typing("You read the sign. It reads:\n\n")
	elif sign == "n":
		clear()
		typing("You do not read the sign. It might have important information that will affect you later on.\n")
	typing("You continue on the road.\n")

def mountains():
	clear()
	typing("Before we travel to THE MOUNTAINS, we need to set your levels.\n")
	time.sleep(1)
	clear()
	functions.textloading(3, "Rolling Dice")
	levelnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	knowledge = random.choice(levelnumbers)
	strength = random.choice(levelnumbers)
	charisma = random.choice(levelnumbers)
	speed = random.choice(levelnumbers)
	typing("Your knowledge level is " + str(knowledge) + ".\n")
	typing("Your strength level is " + str(strength) + ".\n")
	typing("Your charisma level is " + str(charisma) + ".\n")
	typing("Your speed level is " + str(speed) + ".\n")
	averageleveladd = knowledge + strength + charisma + speed
	averageleveldivide = averageleveladd/4
	typing("Your average level is " + str(averageleveldivide) + ".\n")
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	functions.textloading(3, "Traveling to THE MOUNTAINS")
	typing("Welcome to THE MOUNTAINS! Today, your goal is to obtain the DWARVEN CLUB.\n")
	typing("Let's begin!\n")
	typing("Up ahead, you see a mountain range with many mountains.\n")
	typing("You must decide which mountain the dwarves live in.\n")
	time.sleep(1)
	clear()
	functions.textloading(3, "CHOOSING MOUNTAIN")
	typing("After hours of thinking about where dwarves may live, you narrow your options down to three choices.\n")
	text.mountain_range_mountains()
	typing("Which mountain do you choose?\n")
	chosen_mountain = ""
	while chosen_mountain not in ["1", "2", "3"]:
		chosen_mountain = input("> ")
	if chosen_mountain == "3":
		if knowledge > 4:
			typing("With a knowledge level of " + str(knowledge) + ", I'd expect you to know better.\n")
		else:
			typing("That is not the correct mountain.\n")
		text.youlost()
		functions.waitingroom_teleport()
	elif chosen_mountain == "1":
		if speed < 5 and strength < 5:
			typing("You try to climb up Talera Mountain, but according to your skill levels, you are too weak and slow to climb it before the dwarves run away with the club.\n")
			text.youlost()
			functions.waitingroom_teleport()
		else:
			typing("You hike towards Talera Mountain.\n")
			time.sleep(1)
			clear()
			typing("You made it to Talera Mountain. You need to climb to the top to reach the dwarves.\n")
			typing("As you climb the mountain, you run into a disco yeti.\n")
			typing("It tries to attack you.\n")
			print("What do you do? Here are your options:")
			print("1) Use your knowledge to formulate a plan.")
			print("2) Fight")
			print("3) Run")
			print("4) Negotiate")
			yeti_choice = ""
			while yeti_choice not in ["1", "2", "3", "4"]:
				yeti_choice = input("> ")
			if yeti_choice == "1":
				if knowledge >= 5:
					typing("Since you have a knowledge level of " + str(knowledge) + ", you decide the best thing to do is to put on some disco music to distract the yeti.\n")
				else:
					typing("With a knowledge level of " + str(knowledge) + ", you are pretty dumb. For some reason, you try to get away by running into the yeti's cave.\n")
					typing("That was a mistake.\n")
					text.youlost()
					functions.waitingroom_teleport()
			elif yeti_choice == "2":
				if strength >= 6:
					typing("You are strong, so you knock the yeti out.\n")
				else:
					typing("Your levels say that you are weak. You know what happens.\n")
					text.youlost()
					functions.waitingroom_teleport()
			elif yeti_choice == "3":
				if speed >= 5:
					typing("According to your levels, you are fast. You outrun the yeti.\n")
				else:
					typing("You are too slow.\n")
					text.youlost()
					functions.waitingroom_teleport()
			elif yeti_choice == "4":
				if charisma >= 4:
					typing("You talk to the yeti.\n")
					typing("He allows you to pass.\n")
				else:
					typing("You have a low charisma level, so he does not allow you to pass.\n")
					text.youlost()
					functions.waitingroom_teleport()
	elif chosen_mountain == "2":
		if knowledge < 4:
			typing("You try to climb the widest mountain in the mountain range, but since you have a knowledge level of " + str(knowledge) + ", you get lost.\n")
			text.youlost()
			functions.waitingroom_teleport()
		else:
			typing("You hike towards Mount Goat.\n")
			time.sleep(1)
			clear()
			typing("You made it to Mount Goat. Time to climb!\n")
			typing("You found a large area. It is a good place to take a break.\n")
			typing("As you sit down, a goat walks up to you.\n")
			typing("Goat - I AM KING GOAT! I COMMAND YOU TO GET OFF MY PROPERTY!\n")
			text.goat_king()
			goat_king = ""
			while goat_king not in ["1", "2", "3", "4", "5"]:
				goat_king = input("> ")
			if goat_king == "1":
				typing("You attempt to negotiate with the goat.\n")
				if charisma > 6:
					typing("You tell the goat that you are trying to get the DWARVEN CLUB.\n")
					typing("Goat - Ah, yes... \n")
					typing("Goat - I have heard rumors that something has happened to it. You may want to go check it out.\n")
					typing("The KING GOAT allows you to pass.\n")
				else:
					typing("Goat - Nice try.\n")
					text.youlost()
					functions.waitingroom_teleport()
			elif goat_king == "2":
				typing("You attempt to fight the goat.\n")
				if strength > 5:
					typing("You are strong enough to beat the goat.\n")
				else:
					typing("With the goat's horns, it charges at you.\n")
					typing("You have been beat by a goat.\n")
					text.youlost()
					functions.waitingroom_teleport()
			elif goat_king == "3":
				typing("You attempt to give a peace offering to the goat.\n")
				if knowledge > 4:
					typing("Goat - I will allow you to pass through my territory, as long as you do not harm any of us goats.\n")
				else:
					typing("The goat denies.\n")
					text.youlost()
					functions.waitingroom_teleport()
			elif goat_king == "4":
				typing("You attempt to run from the goat.\n")
				if speed > 5:
					typing("You successfully outrun the goat. He is no match for you!\n")
				else:
					typing("This goat is faster than you. With a speed level of " + str(speed) + ", never try to outrun a goat.")
					text.youlost()
					functions.waitingroom_teleport()
			elif goat_king == "5":
				typing("You ignore the goat.\n")
				typing("That was a mistake.\n")
				text.youlost()
				functions.waitingroom_teleport()
	typing("Now that you have successfully got past your obstacle, you can continue on to the top of the mountain.\n")
	time.sleep(2)
	clear()
	typing("You are almost at the top of the mountain, but there is a fork. One path leads to the tip-top of the mountain, while the other leads to a cave. Where would you like to go?\n")
	print("1) The tip-top of the mountain\n2) The cave")
	split_in_road = ""
	while split_in_road not in ["1", "2"]:
		split_in_road = input("> ")
	clear()
	if split_in_road == "1":
		typing("You continue on to the tip-top of the mountain.\n")
		time.sleep(1)
		typing("You reach the tip-top of the mountain, but you realize that it is too tiny to hold a group of dwarves.\n")
		text.youlost()
		functions.waitingroom_teleport()
	elif split_in_road == "2":
		typing("You walk into the cave.\n")
		time.sleep(1)
		typing("It is dark, so you rub some sticks together to light a fire.\n")
		time.sleep(1)
		clear()
		functions.textloading(2, "LIGHTING FIRE")
		typing("You successfully light a fire to guide you through the cave.\n")
		typing("You walk around the cave, but don't see anything.\n")
		time.sleep(1)
		clear()
		typing("After about a half-hour, you hear voices.\n")
		typing("Voice 1 - Ah, yes. A very fantastic club this is!\n")
		typing("Voice 2 - I can't believe it's ours now!\n")
		typing("The second voice confuses you. Didn't the dwarves already own a club?\n")
		typing("You walk over towards the voices to find some robbers holding the DWARVEN CLUB.\n")
		time.sleep(1)
		clear()
		typing("The robbers see you.\n")
		typing("Robber 1 - Hey, Gerald. We've got ourselves our first test subject.\n")
		typing("Gerald - I've got the club. Shall I knock him, Rob?\n")
		typing("Rob - Yeah!\n")
		typing("The robbers knock you out.\n")
		time.sleep(1)
		clear()
		typing("When you wake up, you find yourself in a small, rundown shack with Rob and Gerald looking down at you.\n")
		typing("Gerald - Wow! This club actually has powers! It knocked him out with the lightest touch.\n")
		typing("\"Oh no,\" you say to yourself.\n")
		typing("You were wondering why this club was so important.\n")
		time.sleep(1)
		clear()
		typing("All of a sudden, Gerald puts the club down and walks over to you.\n")
		typing("It appears that he wants to tie you up in a chair.\n")
		typing("You also notice some potions on a shelf next to you.\n")
		typing("You realize that you can escape the shack using one of these things.\n")
		typing("Which would you like to use?\n")
		print("1) Grab the club and escape with it\n2) Pick up a random potion and see what it does")
		shack_escape = ""
		while shack_escape not in ["1", "2"]:
			shack_escape = input("> ")
		clear()
		if shack_escape == "1":
			typing("You grab the DWARVEN CLUB, smash (or because the club is magic, lightly touch) the wall and run outside.\n")
			typing("Rob and Gerald hop on horses and chase after you.\n")
			typing("They chase you until you get cornered.\n")
			typing("Rob - It's over now.\n")
			time.sleep(1)
			clear()
			typing("When all seems lost, some police officers on horses ride up and arrest Rob and Gerald for not only chasing you and stealing the club, but also because they tried to steal the TALERA RUBY and the ELVERN FLUTE.\n")
			typing("Police Officer - It seems as though these guys were trying to steal your club.\n")
			typing("You - Uhh, yes. This was one-hundred percent my club...\n")
			typing("Police Officer - Anyway, we should probably get these robbers to jail.\n")
			typing("The police officers ride away with Rob and Gerald.\n")
			typing("You are excited to obtain the DWARVEN CLUB.\n")
			text.youwon()
			if "DWARVEN CLUB" not in city.trophies:
				city.trophies.append("DWARVEN CLUB")
				typing("Now that the DWARVEN CLUB is yours, you obtain 20 coins.\n")
				city.coins += 20
			else:
				typing("Hmm. It looks like you already have the DWARVEN CLUB in your trophy room.\n")
				typing("You have still earned 10 coins.\n")
				city.coins += 10
			if "NON-MAGIC DWARVEN CLUB" not in city.trophies:
				typing("You can still get the DWARVEN CLUB without its magic powers.\n")
			functions.waitingroom_teleport()
		elif shack_escape == "2":
			typing("You pick up a random potion and throw it towards Rob and Gerald.\n")
			list_of_numbers = ["1", "2", "3"]
			randomnumber = random.choice(list_of_numbers)
			if randomnumber == "1":
				typing("Unfortunately, the potion you threw was an invincibility potion.\n")
				text.youlost()
				functions.waitingroom_teleport()
			elif randomnumber == "2":
				typing("The potion seems to have made a cloud of smoke between you and the robbers.\n")
				typing("You still see the DWARVEN CLUB, so you grab it and turn around, only to find the potion shelf.\n")
				typing("The door is on the other side of the smoke.\n")
				typing("You smash the club through the shelf and through the wall to successfully break out of the shack.\n")
				typing("However, when you smashed through the potion shelf, you smashed a potion that made the DWARVEN CLUB lose its magic.\n")
				typing("Though this is true, you have successfully escaped the robbers!\n")
				text.youwon()
				if "NON-MAGIC DWARVEN CLUB" not in city.trophies:
					city.trophies.append("NON-MAGIC DWARVEN CLUB")
					typing("You have also earned 10 coins.\n")
					city.coins = city.coins + 10
				else:
					typing("It seems as though the NON-MAGIC DWARVEN CLUB is already in your trophy room.\n")
					typing("You have still earned 5 coins.")
					city.coins = city.coins + 5
				if "DWARVEN CLUB" in city.trophies:
					typing("You may have won, but you can still get the DWARVEN CLUB with its magic powers.\n")
				functions.waitingroom_teleport()
			elif randomnumber == "3":
				typing("The potion you threw was just a glass of water.\n")
				typing("It didn't do much.\n")
				text.youlost()
				functions.waitingroom_teleport()

def temple_level():
	clear()
	typing("Before we travel to THE TEMPLE, we need to set your levels.\n")
	time.sleep(1)
	clear()
	functions.textloading(3, "Rolling Dice")
	levelnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	knowledge = random.choice(levelnumbers)
	strength = random.choice(levelnumbers)
	charisma = random.choice(levelnumbers)
	speed = random.choice(levelnumbers)
	typing("Your knowledge level is " + str(knowledge) + ".\n")
	typing("Your strength level is " + str(strength) + ".\n")
	typing("Your charisma level is " + str(charisma) + ".\n")
	typing("Your speed level is " + str(speed) + ".\n")
	averageleveladd = knowledge + strength + charisma + speed
	averageleveldivide = averageleveladd/4
	typing("Your average level is " + str(averageleveldivide) + ".\n")
	typing("Please press enter to continue.\n")
	input("> ")
	clear()
	functions.textloading(3, "Traveling to THE TEMPLE")
	typing("Welcome to THE TEMPLE, long lost in the jungle.\n")
