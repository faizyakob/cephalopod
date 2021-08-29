
import sys
import time 

a = 2
b = 0.2
c = 0.08


def intro():
    print()
    print("(EVERYTHING IS DARK)")
    time.sleep(a)
    print("You feel around, using your hands to see.")
    time.sleep(a)
    print("The ground is cold, damp, and covered in thick vines.")
    time.sleep(a)
    print("You feel a round rock that sinks into the floor when you press it.")
    time.sleep(a)
    print("The ground starts rumbling.")
    print("Light begins flooding in.")
    time.sleep(a)
    print()
    s = '"I\'m in a cave...?"'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1)
    print()
    print()
    print("The rock released a boulder that was blocking the cave entrance")
    time.sleep(a)
    print("Three paths are revealed:")
    time.sleep(a)
    print()
    print("Path #1: Exit forward through the caves entrance, into the light.")
    time.sleep(a)
    print("Path #2: Explore the depths of the rear of the cave, into the darkness")
    time.sleep(a)
    print("Path #3: Climb down the vines into a bottomless hole in the ground")
    print()
    firstPath = input("Which path will you choose? (1/2/3): ")

    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()


def path1():
    pass
def path1_1():
    pass 
def path1_2():
    pass
def path2():
    pass 
def path2_1():
    pass 
def path2_2():
    pass
def path3():
    print("You climb down the vines into a bottomless hole in the ground.")
    time.sleep(a)
    print("It's dark, damp and hard to climb down the vines, but your vision and muscles eventually adjusted.")
    time.sleep(a)
    print("A huge boulder slides into the place above you, blocking your escape.")
    time.sleep(a)
    print("You continue climbing down the vinees until you hear something whirring up at you.")
    print()
    s1 = '"Hey, hey there!..."\n'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    s2 = "...My name is HERMES... I'll be your guide to freedom... \n"
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    s3 = "...Yes, I know all about you! You're looking for CHRONOS...\n"
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    s4 = "...He's the one who trapped you in the time loop...\n"
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    s5 = "...I'm on my way to deliver a message, so I can't escort you personally...\n"
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    s6 = "However, I can transport you there, or anywhere else on Mount OLYMPUS...\n"
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    s7 = "...CHRONOS is just below and he'll certainly TEST YOU when you meet him...\n"
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()
    print("HERMERS will transport you anywhere on Mount OLYMPUS.")
    time.sleep(a)
    print("Path #1: Continue below to face CHORONOS.")
    print("Path #2: Read: THE SECRETS OF TIME.")
    print("Path #3: Speak with ARES.")
    print("Path #4: Speak with ARTEMIS.")
    print("Path #5: Speak with APOLLO.")
    print()
    secondPath = input("Which path will you choose? (1/2/3/4/5): ")
    if secondPath == '2':
        path2_2()
    elif secondPath == '3':
        path1_1()
    elif secondPath == '4':
        path1()
    elif secondPath == '5':
        path2()
    else:
        print()
    print("You continue down the vines until you reach the bottom.")
    time.sleep(a)
    print("You see a small old woman next to the largest red and black iron-wrought double doors you've ever seen.")
    time.sleep(a)
    print("The old woman calls out to you.")
    print()
    d1 = '"Hello there, young traveler..."\n'
    for character in d1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    d2 = "I know who you seek... CHRONOS is just beyond this door...\n"
    for character in d2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    d3 = "...If you enter, you may speak with him and restore your freedom.\n"
    for character in d3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    d4 = "...But before you do so, would you take me HOME?...\n"
    for character in d4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    d5 = "...I\'m unable to escape this code, dark cave on my own...\n"
    for character in d5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    d6 = '"...The choice is yours."'
    for character in d6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()
    print("Path #1: Forget the old woman. Enter the doors and speak with CHRONOS.")
    print("Path #2: Honor the woman's request. Help MOIRAE return home safely.")
    thirdPath = input("Which path would you like to take? (1/2): ")
    if thirdPath == '1':
        path3_1()
    elif thirdPath == '2':
        path3_2()

def path3_1():
    print()
    print("You beging wallking toward the doors, ignoring MOIRAE's request")
    time.sleep(a)
    print('"I would help you out but I\'m a bit of a hurry, you understand."')
    time.sleep(a)
    print("You pull open the massive doors will all of your might and enter.")
    time.sleep(a)
    print("Standing now in the largest room, in front of the largest man you've ever seen.")
    time.sleep(a)
    print("The room is dark, but you can see the source of the thunderous voice which calls out to you...")
    time.sleep(a)
    print()
    e0 = '"Ah...I\'ve been expecting you. But you\re somewhat early...\n'
    for character in e0:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    e1 = "...It appears you've taken a fairly hard route...\n"
    for character in e1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    e2 = "...Your vision is keen. You see through the darkness and the light...\n"
    for character in e2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    e3 = "...And your strength has grown from your travels...\n"
    for character in e3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    e4 = "...However, there is still just one...\n"
    for character in e4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    e5 = "...One more thing you need to learn\n"
    for character in e5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    e6 = "...And learn you will...\n"
    for character in e6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    e7 = "...In time.\"\n"
    for character in e7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    intro()



def path3_2():
    
    print("You begin walking toward MOIRAE, honoring her request.")
    time.sleep(a)
    f1 = '"I understand. I know what it\'s like to miss home... That\'s why I need to get out of here...\n'
    for character in f1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    f2 = 'But before I walk through those doors, I promise that I\'ll get you home safely."\n'
    for character in f2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print()
    print("You kneel in front of MOIRAE, allowing her to climb easily onto yur back.")
    time.sleep(a)
    print("Standing up, you make your way back to the vine wall to make your ascent.")
    time.sleep(a)
    print("Just as you grab the vines, the enormous red and black iron doors thrust open, slamming to a halt.")
    time.sleep(a)
    print("The largest man you've ever seen steps out and his thunderous voice calls out to you.")
    print()
    f3 = '"Ah... I\'ve been expecting you. And you\'re right on time!...\n'
    for character in f3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    f4 = '...It appears you\'ve taken a very difficult route...\n'
    for character in f4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    f5 = "Your vision is keen. You see through the darkness and the light...\n"
    for character in f5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    f6 = "...And your strength has grown from your travels...\n"
    for character in f6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    f7 = "...You've even put others needs before your own...\n"
    for character in f7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    f8 = "...You have learned everything I have to teach you...\n"
    for character in f8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    f9 = "...So you may finally be free...\n"
    for character in f9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1)
    print("...It's time to return.")
    time.sleep(a)
    print()
    print("Thank you playing!!!")


print()
print()
print("     #########################")
print("     #                       #")
print("     #    Time Unraveled     #")
print("     #                       #")
print("     #########################")
print()
print()
time.sleep(a)
print("Wha.. What happened? Where am I?")
time.sleep(a)
print("It's too dark to see anything...")
time.sleep(a)
print()
startGame = input("Would you like to start the game? (Y/N): ")
if startGame == 'n' or startGame == 'N':
    print("Maybe next time")
elif startGame == 'y' or startGame == 'Y':
    intro()

