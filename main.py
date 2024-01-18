from turtle import Turtle,Screen
import random
#getting the turtle window on screen, turtle object created 
color_list=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directionlist=[0,90,180,270]
timmy_the_turtle=Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.shapesize(2,2,1)


timmy_the_turtle.fillcolor('Red')
#drawing a square using for loop 
def drawsquare():
  for i in range(0,4):
     timmy_the_turtle.forward(300)
     timmy_the_turtle.heading()
     timmy_the_turtle.right(90)
     timmy_the_turtle.heading()
def draw_pattern(num):
    angle=360/num
    for i in range(num):
      timmy_the_turtle.forward(100)
      timmy_the_turtle.right(angle)
    
def random_walk():
  for i in range(300):
    timmy_the_turtle.pensize(15)
    timmy_the_turtle.forward(30) 
    direction=random.choice(directionlist)
    timmy_the_turtle.setheading(direction)
    colour=random.choice(color_list)
    timmy_the_turtle.color(colour) 
    
def draw_spirograph():
  timmy_the_turtle.color(colour)
  timmy_the_turtle.circle(100)
  heading=timmy_the_turtle.heading()
  timmy_the_turtle.setheading(heading+10)  
user_choice=int(input("How many number of shapes should be displayed forming a pattern ?")) 
for i in range(3,user_choice+1):
  draw_pattern(i) 
  colour=random.choice(color_list)  
  timmy_the_turtle.color(colour) 
  
screen=Screen()
user_choice2=input("Do you want to reset the screen(y/n?)")
if user_choice2.lower()=="y":
   screen.resetscreen()
random_walk()
user_choice2=input("Do you want to reset the screen(y/n?)")
if user_choice2.lower()=="y":
   screen.resetscreen()
draw_spirograph()   
screen.exitonclick()
