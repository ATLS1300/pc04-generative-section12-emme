#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:10:40 2021

@author: emmefredericks
"""
#my code uses two versions of a spirograph to place them on my page using random coordinates and colors.
#this was based off of my pseudocode but I decided not to add the stems or clouds anymore and instead use two different flower sizes
import random, turtle



flower_1 = turtle.Turtle() #this turtle is for my two larger spirograph flowers 
flower_2 = turtle.Turtle() #this turtle is for my 5 smaller spirographs. Used to adjust and tell the smaller flower turtles what to do

turtle.colormode(255) 

#setting up panel 
panel=turtle.Screen()
w = 700
h = 700
panel.setup(width=w, height=h)

panel.bgcolor(135,206,250)
flower_1.pensize(10) #set two different pen sizes for each flower turtle, different from my pseudocode 
flower_2.pensize(5)
turtle.speed(10)


colors=['pink', 'yellow', 'purple', 'red', 'green','orange']

myListCoordinates = [[-250,-200],[-100,-100],[10,100],[100,-10],[250,250]]
myListCoordinates_2= [[-250,200],[250,-200]]

flower_1.penup()
flower_1.goto(random.choice(myListCoordinates)) #random choice is used to select a random coordinate from my created list 
flower_1.pencolor(random.choice(colors)) #random choice is used to pick a random color from my list of colors 
flower_1.pendown()


inc = 50 # angle increment between shapes in pattern
numIt = int(360/inc) # the number of reps to make a complete circle. 
innerCirc = 10 # radius of inner circle
radius = 25 # radius of circles drawn to make petals

for m in range(2): # nested for loop repeats my spirograph loop two times
    for i in range(numIt): #loop to create a single spirograph
        flower_1.circle(radius)
        flower_1.forward(innerCirc)
        flower_1.right(inc) 
    flower_1.penup()
    flower_1.goto(myListCoordinates_2[m]) #take turtle to one of my coordinates in my list
    flower_1.pencolor(random.choice(colors)) #use color chosen from my list
    flower_1.pendown()
    
inc = 50 
numIt = int(360/inc) 
innerCirc = 25 
radius = 15 

for k in range(5): #nested loop that repeats my smaller spirograph 5 times 
    for i in range(numIt): #for loop to create my single small spirograph 
        flower_2.circle(radius)
        flower_2.forward(innerCirc)
        flower_2.right(inc) 
    flower_2.penup()
    flower_2.goto(myListCoordinates[k])
    flower_2.pencolor(random.choice(colors))
    flower_2.pendown()