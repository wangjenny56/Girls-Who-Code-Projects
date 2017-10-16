from turtle import *
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640,480))


# START WRITING YOUR CODE HERE
def square(size, color):
	pencolor(color)
	pendown()
	for i in range(4):
		forward(size)
		right(90)
        
def triangle(size, color):
	pencolor(color)
	pendown()
	for i in range(3):
		left(120)
		forward(size)



def house(size, color):
	square(size, color)
	penup()
	forward(70)
	triangle(size, color)
	door(size, color)
	#Recommended functions: fillcolor(...), triange(...), square(...), and door()
	

def door(size, color):
	penup()
	goto(x+19, y-40)
	pendown()
	fillcolor("Gold")
	begin_fill()
	square(30, color)
	end_fill()
	#remember you will have to adjust your pen because it just finished drawing 
	#your house
	#Recommended functions: penup(), color(...), forward(...), square(...)



#-----MAIN CODE HERE -----
#This code will run first!

for i in range(5):
	penup()
	goto(70, 0) #REPLACE ... WITH A NUMBER YOU WANT
	fillcolor("green")
	begin_fill()
	circle(20)
	end_fill()
	fillcolor("aliceblue")
	begin_fill()
	house(70,"blue1")
	end_fill()
	
	fillcolor("aliceblue")
	begin_fill()
	door(70, "blue1")
	end_fill()
	
	penup()
	x+=70
	


#this keeps the window open!
while True:
	#this allows for the window to remain open
	for event in pygame.event.get():
		# it listens for events or changes in the program
		if event.type == pygame.QUIT:
			'''if the change in the program is the user
			hitting the X button, then it will quit
			the game and exit the system.'''
			pygame.quit(); sys.exit();








