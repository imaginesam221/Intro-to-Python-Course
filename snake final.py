#modules 
import turtle
import time
import random

delay = 0.1 

#score
score = 0
high_score = 0


 

#window for snake
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) 
#turns off screen animation

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup() #so turtle module does not draw lines while moving
head.goto(0,0) #center turtle on screen
head.direction = 'stop' #turtle does not move unless there is keybinding input

#food
food = turtle.Turtle()
colors = random.choice(['red', 'orange', 'yellow'])
shapes = random.choice(['square', 'circle']) 
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100) 

#score board
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("times", 20, "bold")) 

#functions for movement
#key directions for playing 
#if statements prevent reverse directional movement so that snake 
#does not collide with itself when changing direction one way or the other
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
     head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right" 

#move function to determine speed of movement
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#assigning keys to play with
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

segments = []

#gameplay mechanics/Main Loop
while True: 
    wn.update() #allows loop to continually update in the window
   
   #collision with game window borders 
   #window is 600 by 600
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        #hiding segments after collision
        for segment in segments:
            segment.goto(1000, 1000) #out of range of window borders
       
       #clearing segments from board
        segments.clear()
        
        #score reset
        score = 0
        
        #delay reset
        delay = 0.1
        
        #score reset part 2 electric boogaloo
        pen.clear()
        pen.write("Score: {}  High Score: {} ".format(
            score, high_score), align="center", font=("times", 20, "bold"))
    
    #NOM on Food, randomizing location within the window boundaries
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

#add segment to snake
#every segment is its own turtle
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
#tail color
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
#shorten delay, because ur not a real gamer if it's not challenging 
#dark souls who? elden whatever???
        delay -= 0.01
#increase score
        score +=10 
        #if new score is better, replaces high score on score board
        if score > high_score:
            high_score = score
        #clear previous score from screen so that there is no overlap
        pen.clear()
        pen.write("Score: {}  High Score: {} ".format(
            score, high_score), align="center", font=("times", 20, "bold"))


#moving segments relative to head 
#segments move as a list relative to head and if there is more than 0
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    #segment immediately behind head follows head
    #other segments follow first non-head segment
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    #collision with snek body; silly snek, you can't commit cannibalism 
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

        #score clearing part three, 
        #because cannibalism isn't free [real estate]
            score = 0
            delay = 0.1
            
            pen.clear()
            pen.write("Score : {}  High Score : {} ".format(
            score, high_score), align="center", font=("times", 20, "bold"))

    time.sleep(delay)
 
wn.mainloop()
