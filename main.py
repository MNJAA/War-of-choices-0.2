# modules going to be used in this file
from time import sleep
import stories 
import random
from ANSI import SL, B, un, C, CR, Y, Blue

# takes the user_name
user_name =""
def greet():
	user_name = input("Hello, what is your name: ")
	print(C,CR)
	print(f"{SL}Nice name")
	sleep(1), print(C,CR)
	print(f"{SL}{user_name}, WELCOME {B}TO WAR OF CHOICES{un}. ")
	sleep(1.5)
	return user_name

# prints the story menu
story_select = ""
def story_select(): 
	print(C,CR)
	print(f"{Blue}{SL}Stories list: {un}{SL}")
	stories.stories_listing()
	story_select = input(f"{SL}{user_name}, select a story: {SL}")
	print(C,CR)
	return story_select


# print the story and the choices
def story_go(ss):
	print(C,CR)
	if ss == "1":
		print(stories.story_1["Chapters"]["Intro"])
		sleep(1.5)
		cn = input(f"{user_name}, do you wanna continue? Y/N: ").upper()
		print (C, CR)
		if cn == "Y":
			print("Cool, let's continue")
			sleep(1.5)
			print(C,CR)
			print(stories.story_1['chapters']['chapter1'])
		else:
			selected = story_select()
			story_go(selected)

greet()
selected = story_select()
story_go(selected)