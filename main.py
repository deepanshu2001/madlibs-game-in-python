# python program to create a madlibs game
import random
size=int(input("Enter size of list:"))
ra=random.randint(0,size)
li=[]
for i in range(size):
    a=input("Enter random words:")
    li.append(a)
print(f"The story begins with {li[ra]} who is known to be the {li[ra]} surviver of the mission.He was sent to {li[ra]} to fight a {li[ra]}.There after defeating him he became the immortal {li[ra]}.His sole purpose is to defeat the {li[ra]} to protect the world.He successfully {li[ra]} {li[ra]} withe the help of {li[ra]},{li[ra]},{li[ra]} and {li[ra]}.Now he is {li[ra]} to become the best {li[ra]} there ever was!.This is the end of story")

