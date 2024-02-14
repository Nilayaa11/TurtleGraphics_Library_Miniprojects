'''this program will let you play with some doodling with the turtle tim 
high order functions have been used in this .'''
from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()
tim.shape('turtle')
def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def right():
    newheading=tim.heading()+10  
    tim.setheading(newheading)  
def left():
    newheading=tim.heading()-10  
    tim.setheading(newheading) 
#Refer Documentation as clear() method is defined for both screen and the turtle       
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
#high order functions are always defined with the functions inside it without parenthesis
    
screen.listen()
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()    
        
      
        
