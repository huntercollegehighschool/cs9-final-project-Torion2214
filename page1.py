#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.
def start():
print(“There are two doors. Choose either door A or door B.”)
choice = input(“Enter A for door A or B for door B”)
if choice == “A”:
doorA()
elif choice == “B”:
doorB()
def doorA():
print(“The room is dark. You can either turn on the light, wander aimlessly in the
dark, or go back to the start.”)
choice = input(“Enter L to turn on the light, W to wander aimlessly, or S to go
back to the start.”)
if choice == “L”:
lighton()
elif choice == “W”:
wanderindark()
elif choice == “S”:
start()