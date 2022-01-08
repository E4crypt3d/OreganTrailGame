#By E4crypt3d
print("Welcome to the Oregan Trail Game")
print("You set off west with your family")
input("PRESS ANY KEY TO START THE GAME")
def challenge_1():
    print("You hear a scream")
    print("You see a bear attacking your son Jabbar")
    print("You have two choices to save Jabbar")
    print("a. You go and get your gun")
    print("b. You run away")
    choice_1=input()
    if choice_1=="a":
        print("You killed the bear and saved Jabbar")
        return "alive"
    elif choice_1=="b":
        print("You ran away and bear ate your son Jabbar")
        return "dead"
    else:
        print("You didnt choice neither option and Jabbar died")
        return "dead"
def challenge_2():
    print("You were on the way to home and you meet a Witch and she ask to choose a spell to cross")
    print("You have two choices")
    print("a. Red Spell")
    print("b. Blue Spell")
    choice_2=input()
    if choice_2=="a":
        print("You choosed the wrong spell and died")
        return "dead"
    elif choice_2=="b":
        print("You somehow choosed the correct spell and you live")
        return "alive"
    else:
        print("You refused to choose Witch got angry and killed you")
        return "dead"
def challenge_3():
    print("A member of the jungle associate ask you to choose a number between 4 and 9")
    print("You must choose a correct number or else he will kill you")
    choice_3=int(input())
    if choice_3 > 5 and choice_3 < 9:
        print("Wow you somehow survived")
        return "alive"
    else:
        print("Unlucky you Try Again")
        return "dead"
def challenge_4():
	print("You have to cross a land known for snakes")
	print("Pick a number between 10 and 15. If you pick the unlucky number you die")
	choice_4 = int(input())
	if choice_4 < 10 or choice_4 > 15:
		print("you couldn't follow the rules and died")
		return "dead"
	else:
		if choice_4 != 13:
			print("the snake does not attack you")
			return "alive"
		else:
			print("you knew that was an unlucky number but you picked it anyway and died")
			return "dead"

player_status= "alive"
import random
choice_history = []
history= ""
while player_status=="alive":
    challenge_number = random.randint(1,4)
    choice_history.append(choice_history)
    if challenge_number==1:
        player_status = challenge_1()
        history = history + "1 "
    elif challenge_number==2:
        player_status = challenge_2()
        history = history + "2 "
    elif challenge_number== "3":
        player_status= challenge_3()
        history = history + "3 "
    elif challenge_number== "4":
        player_status=challenge_4()
        history= history+ "4 "

print("You are now dead Good Game")

savefile= "gamehistory.txt"
with open(savefile,'w') as f:
    f.write(history)
