#this code works on creating a dotted painting which creates random colored dots 
'''
ABOUT THE LIBRARY USED
colorgram.py is a Python library that lets you extract colors from images.
Compared to other libraries, the colorgram algorithm’s results are more intense.

'''
import colorgram
import turtle as t
import random 
tim=t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.penup()
tim.hideturtle()
#object of class turtle which will acces the dot() method inside it 
# Extract 6 colors from an image.
colors = colorgram.extract('D:\drive d\Gitprojects\Turtle library\download.jpg',25)
#the below format can be more processed in the form of tuples as 
rgb_values=[]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
#rgb_values = [color.rgb for color in colors]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new=(r,g,b)
    rgb_values.append(new)
print(rgb_values) 
dot_count=100
#the result = list of tuples as follows 
color_list= [(248, 245, 235), (238, 249, 244), (250, 238, 246), (235, 242, 249), (234, 224, 94), (207, 159, 111), (121, 174, 209), (215, 133, 172), (225, 61, 132), (197, 7, 63), (186, 77, 27), (44, 105, 162), (129, 187, 161), (235, 163, 195), (191, 165, 17), (39, 186, 111), (12, 23, 60), (18, 27, 166), (196, 36, 123), (230, 224, 5), (16, 183, 209), (49, 129, 76), (143, 217, 200), (43, 17, 12), (131, 217, 232)]
for dots in range(1,dot_count+1):
  tim.dot(20,random.choice(color_list))
  tim.forward(50)
  if dots%10==0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    
