import turtle
import random

# assighining colors to the snake:
turtle.hideturtle()
turtle.penup()
snake = turtle.clone()
snake.shape("square") 

# snake and background color:
bg_color = input("choose a background color, or die ")
turtle.bgcolor(bg_color)
snake_color = input("choose a snake color, or don't, i don't care, jees! ")
snake.color(snake_color)
 # screen size:
screen_size = input("choose your preferd screen size:) or burn in hell ")

# game difficulty:
game_diff = input("choose gmae difficulty noobbbbbbb ") 
# turtle movement spped:
TIME_STEP = 105
turtle.tracer(0,0.5)   #This helps the turtle move smoothly.

# defining SIZE_X and SIZE_Y:
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)                           
turtle.penup() 

SQUARE_SIZE = 20
START_LENGTH = 5    # the starting length of the snake.

# Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1]
    x_pos+= SQUARE_SIZE #increases the x_pos by SQUARE_SIZE(by 20)advances 20 to the right.   
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos) # adds my_pos to pos_list.           
    z = snake.stamp()
    stamp_list.append(z)
        
# keyboard shortcuts
UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"

# assigning values to the variables:UP,DOWN,LEFT,RIGHT:
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

# setting the limits of the game area: RIGHT, LEFT, UP AND DOWN.
# for small screen:
if screen_size == "small" or screen_size == "tiny" or screen_size == "not too big":   
    UP_EDGE = 260
    DOWN_EDGE = -260
    RIGHT_EDGE = 400
    LEFT_EDGE = -400

# for big screeen:
elif screen_size ==  "big" or screen_size == "huge" or screen_size == "enormous":
    UP_EDGE = 520
    DOWN_EDGE = -520
    RIGHT_EDGE = 840
    LEFT_EDGE = -840

def up():
    global direction   # global changes the variable direction.
    direction = UP    # changes the direction to up.
    print("Up key")

def down():
    global direction
    direction = DOWN 
    print( "Down key")

def left():
    global direction
    direction = LEFT
    print("Left key")

def right():
    global direction
    direction = RIGHT    
    print("Right key")

# telling snake what to do when a key is pressed:
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)

turtle.listen()

#creates food turtle for make_food
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")

# making food appear randomly
def make_food():
    min_x =- int(RIGHT_EDGE/SQUARE_SIZE) +1
    max_x = int(RIGHT_EDGE/SQUARE_SIZE) - 1
    min_y =- int(UP_EDGE/SQUARE_SIZE) + 1
    max_y = int(UP_EDGE/SQUARE_SIZE) - 1

    # pick a position that is a multiple of SQUARE_SIZE:
    food_x = random.randint(min_x , max_x)*SQUARE_SIZE
    food_y = random.randint(min_y , max_y)*SQUARE_SIZE

     # make the food go to the randomly-generated position:
    food.goto(food_x, food_y)
    stamp_id = food.stamp() 
    food_stamps.append(stamp_id)
    stamp_pos_tuple = (food_x, food_y)
    food_pos.append( stamp_pos_tuple)
         
#moves the snake in the direction sset by global var
direction = RIGHT # point right at start of game
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if snake.pos() in pos_list[0:-1]:
        quit()
    # changing the snake's location:
    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
    elif direction ==  UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)

    # grab pos of snake;
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # checking if the snake is hitting the edges:
     # for playing without infinite walls 
    if game_diff == "hard" or game_diff == "torture" or game_diff == "why???":
        if new_x_pos >= RIGHT_EDGE:
            print("Sorry, you hit the right corner, GAME OVER!")
            quit()
        if new_x_pos <= LEFT_EDGE:
            print("Sorry, you hit the lrft corner, GAME OVER!")
            quit()
        if new_y_pos >= UP_EDGE:
            print("Sorry, you hit the upper edge, GAME OVER!")
            quit()
        if new_y_pos <= DOWN_EDGE:
            print("Sorry, you hit the downer edge, GAME OVER!")
            quit()

    # for playing with infinite walls == game diif == easy
    if game_diff == "easy" or game_diff == "ebmbarrassing" or game_diff == "light":
        if new_x_pos >= RIGHT_EDGE:
            snake.goto(LEFT_EDGE , new_y_pos)
        if new_x_pos <= LEFT_EDGE:
            snake.goto(RIGHT_EDGE , new_y_pos)
        if new_y_pos >= UP_EDGE:
            snake.goto(new_x_pos,DOWN_EDGE)
        if new_y_pos <= DOWN_EDGE:
            snake.goto(new_x_pos,UP_EDGE )
   
    # the snake's position changed so we stamp it again.
    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp() 
    stamp_list.append(new_stamp) # keep stamp ids so i can delete them later.

    # poping the food that was consumed by the snake:
    global food_stamps, food_pos
    if snake.pos() in food_pos:  # snake is on top of food item
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])  # removes eaten food stamp
        food_pos.pop(food_ind)   # removes eaten food position
        food_stamps.pop(food_ind)
        print("Yummy.....")
    #the snake gets longer
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    if len(food_stamps) < 3:
        make_food()
        
    # moves snake automatically in a chosen refresh rate:
    turtle.ontimer(move_snake,TIME_STEP)

move_snake()


turtle.mainloop()

   

