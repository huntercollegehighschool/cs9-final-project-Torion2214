"""
Name(s): Maya Pandit, Nick Freeman
Name of Project: CS9 Final Project - Choose Your Own Adventure
"""

#Write the main part of your program here. Use of the other pages is optional.

yetidead = False
print ("As a note before you start this game, we recommend playing it on as wide of a screen as possble, due to formatting.")
def start():
  print ("You're exploring a cave you came across during a camping trip. \nWhile exploring the cave, a strong blizzard hits, and collapses the entrance to the cave. \nIf you want to escape, you must find another way out. \nIn front of you, there is a path leading downwards, and a path branching off to the left. \nThe path leading to the side is very dark, and you can't see far ahead of you.")
  choice1 = (input ("\n> Press W to head deeper into the cave, Press A to head down the side path, Press E to further examine your surroundings and equipment: "))
  if choice1 == "W":
    path1()
  elif choice1 == "A":
    path2()
  elif choice1 == "E":
    path3()
'''
choice one 
'''
def path1():
  print("\n\nAs you head deeper into the cave, you notice a straight tunnel ahead that seems to lead into a clearing. \nYou can vaguely make out wooden beams that seem to be holding up the tunnel. \nThe beams look rotted but you can't see much in the dim light. \nAs you head further down the cave, you realize you are in an abandoned mineshaft.")
  choice2_1 = (input("\n> Press W to head deeper into the cave, press S to head back to start: "))
  if choice2_1 == "W":
    path1_1()
  elif choice2_1 == "S":
    path1_2()

def path2():
  print ("\n\nThe left path is very dark. \nAs you walk further, you notice that the ground is very slippery with ice, and the air has gotten considerably colder. \nAfter descending through a narrow passage way you hit a wall. \nThe path may continue in another direction, but you still can't see anything. \nIt would be beneficial to find a light source.\nWhat will you do?")
  choice2_2 = (input("\n> Press F to feel around for a deeper path, Press S to go back to the start: "))
  if choice2_2 == "F":
    path2_1()
  if choice2_2 == "S":
    start()

def path3():
  print ("Y\n\nou open your backpack and look inside. \nThere is a small flashlight with batteries, a half-empty flask of water and a whistle.")
  choice2_3 = input("\n> Press F to take out the flashlight, press W to take out the water, and press X to take out the whistle: ")
  if choice2_3 == "F":
    path3_1()
  if choice2_3 == "W":
    path3_2()
  if choice2_3 == "X":
    path3_3()
    

"""
choice two
"""
def path1_1():
  print("\n\nAs you head deeper down the mineshaft, you come into the clearing. \nBy the entrance to the cave, you see a light switch, which is currently off. \nOn the other side of the cave, you see an elevator, which seems to be functioning. \nOn the right, you see a tightly sealed door, but you can't see whats behind it.")
  choice3_1 = (input ("\n> Press L to turn on the lights, Press E to try to turn on the elevator, Press D to open the door: "))
  if choice3_1 == "L":
    print("\n\nYou flip the switch, and the lights start to slowly flicker on. You hear a roar, but you can't tell where it's coming from. Suddenly, a yeti jumps on you and tears out your throat. Waking yetis is a bad idea.")
  if choice3_1 == "E":
    print ("\n\nThe elevator starts to open slowly, and as it opens, you start smelling a faint scent, but you can't quite recognize it. Your vision starts to get blurry and you collapse to the ground, unable to breathe. Inhaling toxic gasses is a bad idea."),
  if choice3_1 == "D":
    print ("\n\nYou manage to open the door after an immense amount of effort, but as you look inside, it seems to be a dead end. You step back into the clearing, and try to look for another way out.")
    choice3_1_1 = (input("\n> Press L to turn on the lights, Press E to try to turn on the elevator: "))
    if choice3_1_1 == "L": 
      print ("\n\nYou flip the switch, and the lights start to slowly flicker on. \nYou hear a roar, but you can't tell where it's coming from. \nSuddenly, a yeti jumps on you and tears out your throat. \nWaking yetis is a bad idea.")
    if choice3_1_1 == "E":
      print ("\n\nThe elevator starts to open slowly, and as it opens, you start smelling a faint scent, but you can't quite recognize it. \nAfter a few minutes, nothing happens and the smell starts to clear. \nSuddenly, you hear a weak groan and a thud from somewhere nearby.")
      global yetidead
      yetidead = True
      choiceheadback = input("\n> Press S to head back to the beginning: ")
      if choiceheadback == "S":
        pathrestart()
        
def pathrestart():
  print ("\n\nYou climb back up to the entrance.")
  newchoice = (input("\n> Press A to head down the side path, Press E to further examine your surroundings and equipment: "))
  if newchoice == "A":
    path2_1()
  if newchoice == "E":
    path3()

  
def path2_1():
  print("\n\nAs you search for a deeper path, you move slowly and keep your center of gravity low to avoid slipping on the icy ground. \nThere is another small opening behind you in the lowermost section of the narrow cave.\nWill you go down the hole or will you go back to the start?")
  choice3_2 = (input("\n> Press F to go down the hole, press S to go back to the start: "))
  if choice3_2 == "F":
    print("\n\nYou slip through the small hole, but as you lower yourself, your fingertips lose grip on the cold, icy rock and you fall far down to the bottom of the dark cavern you have entered, snapping both of your legs. You go into a state of shock and freeze to death.")
  if choice3_2 == "S":
    start()

def path3_1():
  print("You turn on the flashlight, and you can now see better in dark caves!")
  path4()

def path3_2():
  print("A half-full flask of water. Refreshing!")
  path3()

def path3_3():
  print("A small, orange translucent whistle with a plastic ball inside. Very loud. Will you blow it?")
  choice3_3 = (input("> Press X to blow the whistle, press P to put it away: "))
  if choice3_3 == "X":
    print("You hear a very loud rumbling, and see chunks of ice crumbling off the walls. Out from the front path you see a large white furry hand grab the ground from below and you black out and die.")
  if choice3_3 == "P":
    path3()
"""
choice three
"""

"""
Path 4!!!!
"""
def path4():
  print("With your flashlight in hand, you look ahead and see the main path and the side path. Which will you go down?")
  choice1alt = (input("> Press W to head deeper into the cave, Press A to head down the side path: "))
  if choice1alt == "W":
    path4_1()
  if choice1alt == "A":
    path4_2()

"""
path 4 choice 1
"""
def path4_1():
  print("")

def path4_2():
  print("The left path is very dark. As you walk further, you notice that the ground is very slippery with ice, and the air has gotten considerably colder. After descending through a narrow passage way you hit a wall. The path may continue in another direction, but you still can't see anything. Good thing you have a light source!\nWhat will you do?")
  choice2alt = (input("> Press F to look around for a deeper path, Press S to go back to the start: "))
  if choice2alt == "F":
    path4_2_1()
  if choice2alt == "S":
    start()

"""
path 4 choice 2
"""
def path4_2_1():
  print("You see a small opening behind you in the lowermost section of the narrow cave. You can also see a crevice above you that is illuminated by your flashlight. \nWill you go down the hole or will you go through the crevice above?")
  choice3alt = (input("> Press W to go through the above path, Press D to go down the small hole in the lowermost section, Press S to go back to the start: "))
  if choice3alt == "W" and yetidead == True:
    print("You climb up and slip through the crevice, and as you walk along the path you stumble into a suspicious-looking clearing. Huddled against the corner you see a dead pile of white fur. Upon further inspection, you see that it appears to be a yeti. It does not seem to be breathing. You look to your right and see a translucent wall of ice covering a hole that leads to the outside. You can feel that you are close to escaping. What will you do?")
    finalchoice = (input("Input answer here: "))
    if finalchoice == "X":
      print("You blow the ear-piercing whistle and soon after you hear a very loud rumbling, and see chunks of ice crumbling off the walls. As the ice starts to fall away, you see sunlight start to come through the cracks. Eventually thet rubble clears, and you can see the outside world. Congratulations on surviving.")
    if finalchoice != "X":
      print ("Try checking your bag to see if you have anything you can use.")
    if finalchoice == "X":
      print("You blow the ear-piercing whistle and soon after you hear a very loud rumbling, and see chunks of ice crumbling off the walls. As the ice starts to fall away, you see sunlight start to come through the cracks. Congratulations on surviving.")
  if choice3alt == "W" and yetidead == False:
    print("You climb up and slip through the crevice, and as you walk along\nthe path you stumble into a suspicious-looking clearing. \nSuddenly, you hear movement behind you, and all of a sudden, a yeti jumps out and kills you.")
  if choice3alt == "D":
    print("\n\nYou slip through the small hole, but as you lower yourself, your fingertips lose grip on the cold, icy rock and you fall far down to the bottom of the cavern you have entered, snapping both of your legs. You go into a state of shock and freeze to death.")
  if choice3alt == "S":
    start()

start()

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
