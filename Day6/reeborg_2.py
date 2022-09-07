def turn_right():
    turn_left()
    turn_left()
    turn_left()
def stage1():
    move()
    turn_left()
    move()
    turn_right()
def stage2():
    move()
    turn_right()
    move()
    turn_left()
def walk():
    stage1()
    stage2()
for i in range(0,6):
    walk()


