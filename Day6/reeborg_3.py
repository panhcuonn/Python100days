from shutil import move

def keep_going():
    move()
    find_right_way()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def find_right_way():
    while wall_on_front():
        turn_left()
    while wall_on_right():
        move()
while not at_goal():
    if wall_on_right():
        find_right_way()
    if front_is_clear():
        keep_going()      
    
        
    